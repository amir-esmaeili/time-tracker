from datetime import date, datetime, timedelta
from time_tracker.api.tracker.models import Task
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import connection


class ReportView(APIView):

    def get_object(self, **kwargs):
        start_date = date.today() - timedelta(days=kwargs['day'])
        tasks = Task.objects.filter(start_time__gt=start_date, user=kwargs['user'])
        return tasks

    def pie_chart(self, start, end):
        curs = connection.cursor()
        curs.execute('''
            select  project_id, name, sum(CAST((julianday(end_time)-julianday(start_time))*24 AS real)) 
            from (select * from tracker_task, tracker_project where
             tracker_task.project_id = tracker_project.id ) group by project_id;
        ''')
        result = curs.fetchall()
        return result

    def get(self, request, start, end):

        pie_chart = self.pie_chart(start, end)

        if not end:
            end = date.today()

        work_hours = dict()

        start = datetime.strptime(start, '%Y-%m-%d')
        end = datetime.strptime(end, '%Y-%m-%d')

        now = start

        while now != end:
            user = request.user
            task = Task.objects.filter(start_time__date=now, user=user)
            if len(task) > 0:
                time_in_hour = 0
                for t in task:
                    time_in_hour += (t.end_time - t.start_time).total_seconds()/3600
                work_hours[now.strftime('%b-%d')] = time_in_hour.__round__(2)
            else:
                work_hours[now.strftime('%b-%d')] = 0

            now += timedelta(days=1)

        return Response({
            'work_hours': work_hours,
            'project_base': pie_chart,
            'total': sum(work_hours.values())
        }, status=status.HTTP_200_OK)




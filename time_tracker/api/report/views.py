from datetime import date, timedelta
from time_tracker.api.tracker.models import Task
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class ReportView(APIView):

    def get_object(self, days):
        start_date = date.today() - timedelta(days=days)
        tasks = Task.objects.filter(start_time__gt=start_date)
        return tasks

    def get(self, request, period):

        if period == 'day':
            days = 1
        elif period == 'week':
            days = 7
        elif period == 'month':
            days = 30
        else:
            return Response({'message': 'Chosen period must be day/week/month.'}, status=status.HTTP_400_BAD_REQUEST)

        work_hours = dict()

        start_date = date.today() - timedelta(days=days-1)

        while start_date != date.today() + timedelta(days=1):
            task = Task.objects.filter(start_time__date=start_date)
            if len(task) > 0:
                time_in_hour = 0
                for t in task:
                    time_in_hour += (t.end_time - t.start_time).total_seconds()/3600
                work_hours[start_date.strftime('%b-%d')] = time_in_hour.__round__(2)
            else:
                work_hours[start_date.strftime('%b-%d')] = 0

            start_date += timedelta(days=1)

        return Response({
            'work_hours': work_hours,
            'total': sum(work_hours.values())
        }, status=status.HTTP_200_OK)



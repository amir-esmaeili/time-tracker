# Time-tracker
Time Tracker is an open-source application based on python/django for managing 
your work hours and tasks easily.

## What's new
* Project field for task
* Auto create start time

## How to run
Simply just move into project directory where you can find **manage.py** 
and then run the following command
``$ python manage.py runserver [port]``  
port is optional.

## API
``[ip]:[port]/api/v1/tasks/``  
**GET**  
Fetches all tasks  
**POST**  
Adds a new task  
``body = {"title": string, "project": int, tag: string }``  
**DELETE**  
Deletes all tasks

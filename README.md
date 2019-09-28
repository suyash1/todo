#### About
This is a demo project to create, update, delete and read tasks

#### Prerequisites
* Python 3.6+

#### Running the service
* Create a virtual environment with python 3x
* Go to `src` and install the requirements in virtul env `pip install -r requirements.txt`
* Apply migrations `./manage.py migrate`
* Create a superuser `./manage.py createsuperuser`
* Run the development server `./manage.py runserver`
* Login to `/admin` with superuser to check if everything is fine

#### APIs
You can use Postman to try out APIs. For testing the below, copy cURL requests and import in Postman.=


##### Get a single task by task id
```
    curl -X GET \
        http://localhost:8000/task/1
```

##### Get all the tasks
```
    curl -X GET \
        http://localhost:8000/task
```

##### Create a task 
```
    curl -X POST \
        http://localhost:8000/task \
        -F title=something \
        -F due_date=yyyy-mm-dd
```
##### Update a task
```
curl -X PUT \
  http://localhost:8000/task/1 \
  -F 'title=new title' \
  -F due_date=2019-10-01
  ```
##### Delete a task
```
curl -X DELETE \
  http://localhost:8000/task/2
```

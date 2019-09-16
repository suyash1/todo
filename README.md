#### About
This is a demo project to create user, policies and subscribe a user to policy.

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

##### Create a customer
```
    curl -X POST \
    http://localhost:8000/customer \
    -F first_name=john \
    -F last_name=doe \
    -F dob=1989-11-17 \
    -F email=john@xyz.com
```

##### Get a single customer by customer id
```
    curl -X GET \
  http://localhost:7000/customer/5
```

##### Get all the customers
```
    curl -X GET \
  http://localhost:7000/customer/5
```


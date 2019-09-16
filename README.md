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
You can use Postman to try out APIs. For testing the below, copy cURL requests and import in Postman.=

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
        http://localhost:8000/customer/1
```

##### Get all the customers
```
    curl -X GET \
        http://localhost:8000/customer
```

##### Create a Policy product
```
    curl -X POST \
        http://localhost:8000/policy \
        -F policy_type=personal-health \
        -F premium=100 \
        -F cover=10000
```

##### Get a policy info by policy id
```
    curl -X GET \
        http://localhost:8000/policy/1
```

##### Get all the policy products
```
    curl -X GET \
        http://localhost:8000/policy
```

##### Create a Customer Policy subscription
```
    curl -X POST \
        http://localhost:8000/policy_subscription \
        -F customer=1 \
        -F policy=1
```

##### Get a policy subscription info by subscription id
```
    curl -X GET \
        http://localhost:8000/policy_subscription/1
```

##### Get all the policy subscriptions
```
    curl -X GET \
        http://localhost:8000/policy_subscription
```


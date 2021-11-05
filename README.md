# interview-sheduler
Django application to find available time slots for interview

## Project description
It's a simple django application to find the available timeslots to conduct interview based on the availability of
candidate and interviewer.

### Functionalities
- Both candidate and interviewer can upate their availability time
- Can fetch interview timeslots based on the availability time of both candidate and interviewer

## Instructions to install application
- Clone the repo and install the requirements
  - `$ pip3 install -r requirements.txt`
- Migrate the models
  - `$ python3 manage.py makemigrations scheduler`
  - `$ python3 manage.py migrate`
- Create a superuser
  - `$ python3 manage.py createsuperuser`

## Run application
- `$ python3 manage.py runserver 0:8000`
- After running the application 4 users will be generated automatically
  - smith (username: smith, password: smith123, role: interviewer)
  - mariya (username: mariya, password: smith123, role: interviewer)
  - john (username: john, password: john123, role: candidate)
  - julia (username: julia, password: julia123, role: hr)

## Test application
Three api endpoints have been added
- Login
- Add available timeslots
- Find interview timeslots
    
### Login
- Endpoint: `http://localhost:8000/api-auth/`
- POST request
- Request body: `{
    "username": "john",
    "password": "john123"
}`
- Response body: `{
    "token": "93c6f78889956d0e23f503c1b6d9451cc12d0d07",
    "user_id": 6,
    "email": "john@gmail.com"
}`
### Add available timeslots
- Endpoint: `http://localhost:8000/timeslot/`
- POST request
- Request body: `{
    "start_time": "2021-10-06 10:00:00",
    "end_time": "2021-10-06 13:00:00"
}`
- Response body: `{
    "success": true,
    "message": "Successfully saved available time slot",
    "data": {}
}`
- Request header: `{"Authorization": "Token 93c6f78889956d0e23f503c1b6d9451cc12d0d07"}` 
### Find interview timeslots
- Endpoint: `http://localhost:8000/available-timeslot/?candidate_id=6&interviewer_id=7`
- GET request
- Response body: `{
    "success": true,
    "message": "Successfully fetched common available interview timeslots",
    "data": [
        [
            "2021-11-06 11:00:00",
            "2021-11-06 12:00:00"
        ],
        [
            "2021-11-06 14:00:00",
            "2021-11-06 15:00:00"
        ]
    ]
}`
- Request header: `{"Authorization": "Token 93c6f78889956d0e23f503c1b6d9451cc12d0d07"}` 
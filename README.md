# query-app-ai

A web application providing syntax for keywords in various languages

## Running the application using docker

Use the following command to create the docker container

```
docker-compose up --build
```

To destroy the container run

```
docker-compose down
```

## Running the applicatiom

make sure you have django , python 3.9 and openai library installed else install those using below

1. pip install django
2. pip install openai

3. create an API key on this site : https://beta.openai.com
4. Open views.py in QueryForm directory and paste the API key in variable API_KEY. check this path : GetQuery/QueryForm/views.py
5. If you can't find the views.py file, open the folder in pycharm and click on TODO tab at bottom of pycharm then paste the key
6. open terminal at the level where manage.py is present
7. hit command : python3 manage.py runserver

<img width="1271" alt="Screenshot 2022-12-30 at 7 44 39 PM" src="https://user-images.githubusercontent.com/49924204/210079637-c3a09c6a-b1a2-4f5f-80d7-62abd1a2f80e.png">

https://user-images.githubusercontent.com/49924204/210131810-5186e552-b24c-4655-b4b3-f9142a1b6156.mp4

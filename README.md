# Popeye

## Description
A simple DevOps project

<!-- ABOUT THE PROJECT -->
## About The Project
You will have to containerize and define the deployment of a simple web poll application.
There are five elements constituting the application:
* **Poll**, a Flask Python web application that gathers votes and push them into a Redis queue.
* **Redis queue**, which holds the votes sent by the Poll application, awaiting for them to be consumed bythe Worker.
* The **Worker**, a Java application which consumes the votes being in the Redis queue, and stores them intoa PostgreSQL database.
* **PostgreSQL** database, which (persistently) stores the votes stored by the Worker.
* **Result**, a Node.js web application that fetches the votes from the database and displays the result.

## Usage:

```
>> sudo docker-compose build
>> sudo docker-compose run
```

#### To close your containers
```
>> sudo docker-compose down -v
```

Made at Epitech Lyon in 2022
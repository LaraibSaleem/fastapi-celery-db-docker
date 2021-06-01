# fastapi-celery-db
project saves records to mysql from fastapi as background task using celery, and is dockerized.

Python framework: fastapi <br/>
Worker: Celery <br/>
Message broker: RabbitMQ <br/>
Database: MySQL <br/>
Container: Docker

**Setup:**
- Clone the repository using <br/>
`git clone https://github.com/LaraibSaleem/fastapi-celery-db.git`
- In the repository directory, run below command for building docker images <br/>
`docker-compose build`
- Finally run <br/>
`docker-compose up`

And you are all done!


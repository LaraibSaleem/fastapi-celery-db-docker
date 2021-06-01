from celery import Celery

# Initialize celery
celery = Celery('celery', broker='amqp://user:password@broker:5672//', include=['backend.celery.tasks'])

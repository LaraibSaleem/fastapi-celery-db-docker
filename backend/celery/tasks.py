from celery.utils.log import get_task_logger
from starlette.responses import JSONResponse
import logging
from backend.database import SessionLocal, engine
from backend.models.user_model import User
from backend.models import user_model
from .worker import celery


user_model.Base.metadata.create_all(bind=engine)


LOGGER = logging.getLogger(__name__)
# Create logger - enable to display messages on task logger
celery_log = get_task_logger(__name__)



# Add USer to Database - Run Asynchronously with celery
# Example process of long running task
@celery.task(name="save_data")
def save_data(self, *user):
    #print(f"{user}___________________\n\t")
    print("**********THIS IS USER OF TASK************", user)
    '''
    print(user[0], user[1], user[2], user[3], user[4], user[5],
                    user[6], user[7], user[8], user[9], user[10])
    '''

    try:
        db = SessionLocal()
        db_user = User(id=user[0], index=user[1], guid=user[2], balance=user[3], age=user[4], eyeColor=user[5],
                                  company=user[6], address=user[7], about=user[8], greeting=user[9], favoriteFruit=user[10])
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
    except Exception as ex:
        print(f"\n\t_____*****_____{ex}_____*****_____\n\t")
    return JSONResponse(status_code=200, content={"message": "User record has been added."})
    #return {"msg": "Hello!"}
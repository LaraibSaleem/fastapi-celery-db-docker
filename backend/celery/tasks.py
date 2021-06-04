from celery.utils.log import get_task_logger
#from starlette.responses import JSONResponse
import logging
from backend.database import SessionLocal, engine
from backend.models.user_model import User
from backend.models import user_model
from .worker import celery
from datetime import datetime


user_model.Base.metadata.create_all(bind=engine)


LOGGER = logging.getLogger(__name__)
# Create logger - enable to display messages on task logger
celery_log = get_task_logger(__name__)



# Add USer to Database - Run Asynchronously with celery
# Example process of long running task
@celery.task(name="save_data", serializer='json')
def save_data(self, *user):
    #print(f"{user}___________________\n\t")
    print("**********THIS IS USER OF TASK************", user)
    '''
    print(user[0], user[1], user[2], user[3], user[4], user[5],
                    user[6], user[7], user[8], user[9], user[10])
    '''

    try:
        date = datetime.now()
        print("**********DATE************", date)

        '''
        format_date = datetime.strptime(date, '%M %d, %Y')
        print("**********FORMAT DATE************", format_date)
        '''
        print("**********THIS IS DATA TYPES OF USER OF TASK************")
        print("user.id", type(user[0]))
        print("user.index", type(user[1]))
        print("user.guid", type(user[2]))
        print("user.isActive", type(user[3]))
        print("user.balance", type(user[4]))
        print("user.picture", type(user[5]))
        print("user.age", type(user[6]))
        print("user.eyeColor", type(user[7]))
        #print("user.name", type(user[8]))
        print("user.company", type(user[8]))
        print("user.email", type(user[9]))
        print("user.phone", type(user[10]))
        print("user.address", type(user[11]))
        print("user.about,", type(user[12]))
        print("user.latitude", type(user[13]))
        print("user.longitude", type(user[14]))
        print("user.tags", type(user[15]))
        print("USER TAGS", user[15])
        print("user.range", type(user[16]))
        #print("user.friends", type(user[0]))
        print("user.greeting", type(user[17]))
        print("user.favoriteFruit", type(user[18]))

        '''
        for i in user:
            print(f"{i}\n\t*****************_____________________ {type(i)}_______****************")
        '''

        db_user = User(id=user[0], index=user[1], guid=user[2], isActive=user[3], balance=user[4],
                       picture=user[5], age=user[6], eyeColor=user[7],
                        #name=user[8],
                        company=user[8], email=user[9], phone=user[10], address=user[11], about=user[12], registered=date, latitude=user[13], longitude=user[14],
                        tags=user[15],
                        range=user[16],
                        #friends=user[18]
                        greeting=user[17], favoriteFruit=user[18])
        db = SessionLocal()
        db.add(db_user)
        db.commit()
        db.refresh(db_user)

    except Exception as ex:
        print(f"\n\t_____*****_____{ex}_____*****_____\n\t")
        raise ex
    #return JSONResponse(status_code=200, content={"message": "User record has been added."})
    return {"msg": "Hello!"}
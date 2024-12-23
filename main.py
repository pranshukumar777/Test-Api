from fastapi import FastAPI
import uvicorn
from models.user import User
from models.event import Event
from services.userService import UserService
from services.eventService import EventService
from services.event_participationService import Event_ParticipationService
from repos.event_participationRepo import Event_ParticipationRepo

from fastapi.encoders import jsonable_encoder
from mysql.connector import Error

from repos.userRepo import UserRepo
from repos.eventRepo import EventRepo


app = FastAPI()
userRepo = UserRepo()
userService = UserService(userRepo)


@app.get("/home/{id}")
def getHome(id: int):
    return {"message": "welcome to fastapi {id}"}


@app.get("/participant/{id}")
def getUser(id: int):
    resultUser = userService.getbyid(id)
    return jsonable_encoder(resultUser)


@app.post("/participant/create")
def createUser(user: User):
    userService.createUser(user)
    return {"message": "created!"}


@app.put("/participant/update/{id}")
def updateUser(id: int, user: User):
    result = userService.updateUser(id, user)
    return jsonable_encoder(result)


@app.delete("/participant/delete/{id}")
def deleteUser(id: int):
    try:
        userService.deleteUser(id)
        return {"message": "user deleted!"}
    except Error as err:
        print(f"Error :{err}")


eventRepo = EventRepo()
eventService = EventService(eventRepo)


@app.get("/event/{id}")
def getEvent(id: int):
    result = eventService.getbyid(id)
    return jsonable_encoder(result)


@app.post("/event/create")
def createEvent(event: Event):
    eventService.createEvent(event)
    return {"message": "created!"}


@app.put("/event/update/{id}")
def updateEvent(id: int, event: Event):
    result = eventService.updateEvent(id, event)
    return jsonable_encoder(result)


@app.delete("/event/delete/{id}")
def deleteEvent(id: int):
    try:
        eventService.deleteEvent(id)
        return {"message": "event deleted from events!"}
    except Error as err:
        print(f"Error :{err}")

event_participationRepo = Event_ParticipationRepo()
event_participationService = Event_ParticipationService(event_participationRepo)


@app.post("/event/{eventid}/participant/{participantid}")
def createEvent_Participation(eventid: int, participantid: int):
    event_participationService.createEvent_Participation(eventid, participantid)
    return {"message": "created!!"}


@app.delete("/event/participant/delete/{event_participationid}")
def deleteEvent_Participation(event_participationid: int):
    event_participationService.deleteEvent_Participation(event_participationid)
    return {"message": "deleted from Event_Participation!!"}

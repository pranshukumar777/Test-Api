from models.event_participation import Event_Participation
from .baseRepo import BaseRepo
from models.event import Event
from models.user import User
from mysql.connector import Error

from sqlalchemy import text, create_engine


class Event_ParticipationRepo(BaseRepo):
    def __init__(self):
        super().__init__()

    def create(
        self, event_participation: Event_Participation, eventid: int, participantid: int
    ):
        try:
            with self.engine.connect() as conn:
                query = f"insert into Event_Participation (eventid,participationid)values ({eventid},{participantid})"
                conn.execute(text(query))
                conn.commit()
        except Error as err:
            print(f"Error : {err}")

    def delete(self, id):
        try:
            with self.engine.connect() as conn:
                query = f"delete from event_participation where id={id}"
                conn.execute(text(query))
                conn.commit()
        except Error as err:
            print(f"Error : {err}")

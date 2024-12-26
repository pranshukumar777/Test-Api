import sqlalchemy
from sqlalchemy.exc import IntegrityError

from .baseRepo import BaseRepo
from mysql.connector import Error

from sqlalchemy import text


class EventParticipationRepo(BaseRepo):
    def __init__(self):
        super().__init__()

    def create(self, eventId: int, participantId: int):
        with self.engine.connect() as conn:
            query = f"""INSERT INTO Event_Participation 
            (eventid,participantid) 
            VALUES ({eventId},{participantId})"""
            data = conn.execute(text(query))
            conn.commit()

    def delete(self, id):

        with self.engine.connect() as conn:
            query = f"delete from event_participation where id={id}"
            conn.execute(text(query))
            conn.commit()

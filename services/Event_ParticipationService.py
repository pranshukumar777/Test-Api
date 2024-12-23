from models.event_participation import Event_Participation
from repos.event_participationRepo import Event_ParticipationRepo


class Event_ParticipationService:
    event_participationRepo: Event_ParticipationRepo

    def __init__(self, event_participationRepo: Event_ParticipationRepo):
        self.event_participationRepo = event_participationRepo

    def createEvent_Participation(self, eventid, participantid):
        return self.event_participationRepo.create(
            Event_Participation, eventid, participantid
        )

    def deleteEvent_Participation(self, id):
        return self.event_participationRepo.delete(id)

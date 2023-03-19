from datetime import datetime

from src.domain.entities.event import Event
from src.domain.ports.events_service import EventsService


class Create:
    def __init__(self, event_service: EventsService):
        self.event_service = event_service
    
    def execute(
            self,
            user_id: str, 
            title: str, 
            datetime: datetime, 
            description: str
        ):
        event = self.event_service.create(
            user_id, 
            Event(None, title, datetime, description, 0, user_id)
        )
        if event != None: return event.as_dict()

from datetime import datetime

from src.domain.entities.event import Event
from src.domain.ports.events_service import EventsService


class Update:
    def __init__(self, event_service: EventsService):
        self.event_service = event_service
    
    def execute(
            self,
            user_id: str, 
            id: str, 
            title: str = None, 
            datetime: datetime = None, 
            description: str = None,
        ):
        event = self.event_service.update(
            user_id, 
            id, 
            title,
            datetime,
            description
        )
        if event != None: return event.as_dict()

from datetime import datetime

from src.domain.entities.event import Event
from src.domain.ports.events_service import EventsService


class FetchByDay:
    def __init__(self, event_service: EventsService):
        self.event_service = event_service
    
    def execute(
            self,
            user_id: str, 
            datetime: datetime
        ):
        all_events = self.event_service.fetch_by_day(
            user_id, 
            datetime
        )
        return list(
            map(
                lambda event: event.as_dict(),
                all_events
            )
        )

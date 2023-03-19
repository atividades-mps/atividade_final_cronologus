from datetime import datetime

from src.domain.entities.event import Event
from src.domain.ports.events_service import EventsService


class FetchByRangeDate:
    def __init__(self, event_service: EventsService):
        self.event_service = event_service
    
    def execute(
            self,
            user_id: str, 
            start_date: datetime,
            end_date: datetime
        ):
        all_events = self.event_service.fetch_by_range_date(
            user_id, 
            start_date,
            end_date
        )
        return list(
            map(
                lambda event: event.as_dict(),
                all_events
            )
        )

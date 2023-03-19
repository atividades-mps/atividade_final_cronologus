from src.domain.ports.events_service import EventsService


class FetchAll:
    def __init__(self, events_service: EventsService):
        self.events_service = events_service

    def execute(self, user_id: str):
        all_events = self.events_service.fetch_all(user_id) 
        return list(map(lambda event: event.as_dict(), all_events))
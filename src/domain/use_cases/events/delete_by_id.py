from src.domain.ports.events_service import EventsService


class DeleteById:
    def __init__(self, event_service: EventsService):
        self.event_service = event_service
    
    def execute(
            self,
            user_id: str, 
            id: str, 
        ):
        return self.event_service.delete_by_id(
            user_id, 
            id
        )

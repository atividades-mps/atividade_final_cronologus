from datetime import datetime

from src.domain.entities.event import Event


class EventsService:
    def create(self, user_id: str, new_event: Event) -> Event:
        pass
    def fetch_all(self, user_id: str)-> list[Event]:
        pass
    def update(
            self, 
            user_id: str, 
            id: str, 
            title:str = None, 
            datetime:datetime = None, 
            description: str = None, 
            status: int = None) -> Event:
        pass
    def delete_by_id(self, user_id: str, id: str) -> bool:
        pass
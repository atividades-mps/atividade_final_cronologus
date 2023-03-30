from datetime import datetime
from uuid import uuid1

from src.domain.entities.event import Event
from src.domain.ports.events_service import EventsService


class MockEventsService(EventsService):
    def __init__(self):
        self.data: dict[str, list[Event]] = {}

    def create(self, user_id: str, new_event: Event) -> Event:
        if not(user_id in self.data):
            self.data[user_id] = []
        new_event.id = str(uuid1())
        self.data[user_id].append(new_event)
        return new_event

    def fetch_all(self, user_id: str)-> list[Event]:
        if not(user_id in self.data):
            self.data[user_id] = []
        return self.data[user_id]
        
    def update(
            self, 
            user_id: str, 
            id: str, 
            title:str = None, 
            datetime:datetime = None, 
            description: str = None, 
            status: int = None) -> Event:
        for [index, event] in enumerate(self.data[user_id]):
            if event.id == id:
                found_event = self.data[user_id][index]
                found_event.title = title if title else found_event.title
                found_event.datetime = datetime if datetime else found_event.datetime
                found_event.description = description if description else found_event.description
                found_event.status = status != None if status else found_event.status
                self.data[user_id][index] = found_event
                return found_event


    def delete_by_id(self, user_id: str, id: str) -> bool:
        new_list = []
        for event in self.data[user_id]:
            if event.id != id:
                new_list.append(event) 
        self.data[user_id] = new_list
        return True

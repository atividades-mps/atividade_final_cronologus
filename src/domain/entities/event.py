from datetime import datetime

from src.domain.entities.as_dict import EntityAsDict


class Event(EntityAsDict):
    def __init__(self, id: str, title: str, datetime: datetime, description: str, status: int, user_id: int):
        self.id = id 
        self.title = title 
        self.datetime = datetime 
        self.description = description 
        self.status = status 
        self.user_id = user_id
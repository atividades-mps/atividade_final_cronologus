from src.api.services.mysql_events_service import MySQLEventsService
from src.domain.use_cases.events.create import Create
from src.domain.use_cases.events.delete_by_id import DeleteById
from src.domain.use_cases.events.fetch_all import FetchAll
from src.domain.use_cases.events.update import Update

event_service = MySQLEventsService()

def fetch_all(user_id):
    fetch_all_UC = FetchAll(event_service)
    return fetch_all_UC.execute(user_id)

def create(user_id, event):
    create_UC = Create(event_service)
    return create_UC.execute(
        user_id, 
        event['title'], 
        event['datetime'], 
        event['description']
    )

def delete(user_id, event_id):
    delete_UC = DeleteById(event_service)
    return delete_UC.execute(user_id, event_id)

def update(user_id, event_id, event):
    update_UC = Update(event_service)
    return update_UC.execute(
        user_id, 
        event_id, 
        event['title'], 
        event['datetime'], 
        event['description']
    )
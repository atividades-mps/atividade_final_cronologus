from datetime import datetime
from uuid import uuid1

from src.api.services.mysql_connection import get_mysql_connection
from src.domain.entities.event import Event
from src.domain.ports.events_service import EventsService


class MySQLEventsService(EventsService):
    def __init__(self):
        self.db = get_mysql_connection()
    
    def create(self, user_id: str, new_event: Event) -> Event:
        cursor = self.db.cursor()
        new_event.id = str(uuid1())
        query = "INSERT INTO agenda_eventos(evento_id, evento_titulo, evento_data_hora, evento_descricao, evento_status, usuario_id) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(
            query, 
            (new_event.id, new_event.title, new_event.datetime, new_event.description, new_event.status, user_id)
        )
        self.db.commit()
        return new_event

    def fetch_all(self, user_id: str)-> list[Event]:
        cursor = self.db.cursor()
        query = "SELECT * FROM agenda_eventos WHERE usuario_id = %s"
        cursor.execute(query, (user_id,))
        all_events = []
        result = cursor.fetchall()
        for (evento_id, evento_titulo, evento_data_hora, evento_descricao, evento_status, usuario_id) in result:
            all_events.append(
                Event(
                    evento_id, 
                    evento_titulo, 
                    evento_data_hora, 
                    evento_descricao, 
                    evento_status, 
                    usuario_id
                )
            )
        return all_events

    def _mount_update_query(self, fields: list[tuple[str, str | int | None]]) -> str:
        update_this = ""
        for (key, value) in fields:
            if value != None:
                update_this += key + ","
        return update_this[:-1]
    
    def update(
            self, 
            user_id: str, 
            id: str, 
            title:str = None, 
            datetime:datetime = None, 
            description: str = None, 
            status: int = None) -> Event:
        cursor = self.db.cursor()
        query = " UPDATE agenda_eventos SET " + self._mount_update_query([
                ("evento_titulo = %s", title), 
                ("evento_data_hora = %s", datetime), 
                ("evento_descricao = %s", description), 
                ("evento_status = %s", status)
            ]) + " WHERE evento_id = %s AND usuario_id = %s"
        values = ()
        for value in [title, datetime, description, status, id, user_id]:
            if value != None:
                values = values + (value,)
        cursor.execute(
            query, 
            values
        )
        self.db.commit()
        return Event(id, title, datetime, description, status, user_id)

    def delete_by_id(self, user_id: str, id: str) -> bool:
        cursor = self.db.cursor()
        query = """
            DELETE FROM agenda_eventos 
            WHERE eventos_id = %s AND usuario_id = %s
        """
        cursor.execute(
            query, 
            (id,user_id)
        )
        self.db.commit()
        return True
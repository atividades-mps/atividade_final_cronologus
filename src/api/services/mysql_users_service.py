from uuid import uuid1

from src.api.services.mysql_connection import get_mysql_connection
from src.domain.entities.user import User
from src.domain.ports.users_service import UsersService


class MySQLUsersService(UsersService):
    def __init__(self):
        self.db = get_mysql_connection()


    def create(self, new_user: User) -> User:
        cursor = self.db.cursor()
        new_user.id = str(uuid1())
        query = "INSERT INTO agenda_usuario(usuario_id, usuario_nome, usuario_email, usuario_senha, usuario_status) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(
            query, 
            (new_user.id, new_user.name, new_user.email, new_user.password, new_user.status)
        )
        self.db.commit()
        return new_user

    def fetch_all(self)-> list[User]:
        cursor = self.db.cursor()
        query = "SELECT * FROM agenda_usuario"
        cursor.execute(query)
        all_users = []
        result = cursor.fetchall()
        for (usuario_id, usuario_nome, usuario_email, usuario_senha, usuario_status) in result:
            all_users.append(User(usuario_id, usuario_nome, usuario_email, usuario_senha, usuario_status))
        return all_users

    def find_by_name_and_password(
            self, 
            name:str, 
            password: str) -> User:
        cursor = self.db.cursor()
        query = "SELECT * FROM agenda_usuario WHERE usuario_nome = %s AND usuario_senha = %s"
        cursor.execute(query, (name, password))
        result = cursor.fetchone()
        if result != None:
            (usuario_id, usuario_nome, usuario_email, usuario_senha, usuario_status) = result
            return User(usuario_id, usuario_nome, usuario_email, usuario_senha, usuario_status)
        return None

    def find_by_id(self, id: str) -> User:
        cursor = self.db.cursor()
        query = "SELECT * FROM agenda_usuario WHERE usuario_id = %s"
        cursor.execute(query, (id,))
        result = cursor.fetchone()
        if result != None:
            (usuario_id, usuario_nome, usuario_email, usuario_senha, usuario_status) = result
            return User(usuario_id, usuario_nome, usuario_email, usuario_senha, usuario_status)
        return None

    def _mount_update_query(self, fields: list[tuple[str, str | int | None]]) -> str:
        update_this = ""
        for (key, value) in fields:
            if value != None:
                update_this += key + ","
        return update_this[:-1]
    
    def update(
            self, 
            id: str, 
            name:str=None, 
            email:str=None, 
            password:str=None, 
            status:int=None) -> User:
        cursor = self.db.cursor()
        query = " UPDATE agenda_usuario SET " + self._mount_update_query([
                ("usuario_nome = %s", name), 
                ("usuario_email = %s", email), 
                ("usuario_senha = %s", password), 
                ("usuario_status = %s", status)
            ]) + " WHERE usuario_id = %s"
        values = ()
        for value in [name, email, password, status, id]:
            if value != None:
                values = values + (value,)
        cursor.execute(
            query, 
            values
        )
        self.db.commit()
        return User(id, name, email, password, status)

    def delete_by_id(self, id: str) -> bool:
        cursor = self.db.cursor()
        query = """
            DELETE FROM agenda_usuario 
            WHERE usuario_id = %s
        """
        cursor.execute(
            query, 
            (id,)
        )
        self.db.commit()
        return True
        


from uuid import uuid1

from src.domain.entities.user import User
from src.domain.ports.users_service import UsersService


class MockUsersService(UsersService):
    def __init__(self):
        self.data: list[User] = []
    
    def create(self, new_user: User) -> User:
        new_user.id = str(uuid1())
        self.data.append(new_user)
        return new_user

    def fetch_all(self)-> list[User]:
        return self.data

    def find_by_name_and_password(
            self, 
            name:str, 
            password: str) -> User:
        for user in self.data:
            if user.name == name and user.password == password:
                return user
        return None

    def find_by_id(self, id: str) -> User:
        for user in self.data:
            if user.id == id:
                return user

    def update(
            self, 
            id: str, 
            name:str=None, 
            email:str=None, 
            password:str=None, 
            status:int=None) -> User:
        for [index, user] in enumerate(self.data):
            if user.id == id:
                user.name = name if name else user.name
                user.email = email if email else user.email
                user.password = password if password else user.password
                user.status = status != None if status else user.status
                self.data[index] = user
                return user

    def delete_by_id(self, id: str) -> bool:
        new_list = []
        for user in self.data:
            print(user.id == id)
            if user.id != id:
                new_list.append(user) 
        self.data = new_list
        return True
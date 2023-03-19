from src.domain.entities.user import User


class UsersService:
    def create(self, new_user: User) -> User:
        pass
    def fetch_all(self)-> list[User]:
        pass
    def find_by_name_and_password(
            self, 
            name:str, 
            password: str) -> User:
        pass
    def find_by_id(self, id: str) -> User:
        pass
    def update(
            self, 
            id: str, 
            name:str=None, 
            email:str=None, 
            password:str=None, 
            status:int=None) -> User:
        pass
    def delete_by_id(self, id: str) -> bool:
        pass
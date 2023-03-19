from src.domain.entities.user import User
from src.domain.ports.users_service import UsersService


class Create:
    def __init__(self, user_service: UsersService):
        self.user_service = user_service
    
    def execute(self, name: str, email: str, password: str):
        user = self.user_service.create(User(None, name, email, password, 0))
        if user != None: return user.as_dict()
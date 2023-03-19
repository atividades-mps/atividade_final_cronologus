from src.domain.entities.user import User
from src.domain.ports.users_service import UsersService


class Login:
    def __init__(self, user_service: UsersService):
        self.user_service = user_service
    
    def execute(self, name: str, password: str):
        user = self.user_service.find_by_name_and_password(name, password)
        if user != None:
            self.user_service.update(user.id, status=1)
            return True
        return False

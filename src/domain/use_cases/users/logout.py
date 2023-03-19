from src.domain.entities.user import User
from src.domain.ports.users_service import UsersService


class Logout:
    def __init__(self, user_service: UsersService):
        self.user_service = user_service
    
    def execute(self, id: str):
        user = self.user_service.find_by_id(id)
        if user != None:
            self.user_service.update(id, status=0)
            return True
        return False

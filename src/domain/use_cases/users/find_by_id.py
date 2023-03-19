from src.domain.entities.user import User
from src.domain.ports.users_service import UsersService


class FindById:
    def __init__(self, user_service: UsersService):
        self.user_service = user_service
    
    def execute(self, id: str):
        user = self.user_service.find_by_id(id)
        if user != None: return user.as_dict()
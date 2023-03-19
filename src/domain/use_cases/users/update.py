from src.domain.entities.user import User
from src.domain.ports.users_service import UsersService


class Update:
    def __init__(self, user_service: UsersService):
        self.user_service = user_service
    
    def execute(
            self,
            id: str, 
            name: str = None, 
            email: str= None, 
            password: str = None, 
        ):
        user = self.user_service.update(
            id, 
            name, 
            email, 
            password
        )
        if user != None: return user.as_dict()
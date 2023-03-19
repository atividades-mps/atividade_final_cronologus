from src.domain.ports.users_service import UsersService


class DeleteById:
    def __init__(self, user_service: UsersService):
        self.user_service = user_service
    
    def execute(self, id: str):
        return self.user_service.delete_by_id(id)
from src.domain.ports.users_service import UsersService


class FetchAll:
    def __init__(self, user_service: UsersService):
        self.users_service = user_service

    def execute(self):
        all_users = self.users_service.fetch_all() 
        return list(map(lambda user: user.as_dict(), all_users))
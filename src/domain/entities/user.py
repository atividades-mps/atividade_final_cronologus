from src.domain.entities.as_dict import EntityAsDict


class User(EntityAsDict):
    def __init__(self, id: str, name: str, email: str, password: str, status: int):
        self.id = id 
        self.name = name 
        self.email = email 
        self.password = password
        self.status = status 
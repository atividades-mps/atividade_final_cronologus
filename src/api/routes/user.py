from src.api.services.mock_users_service import MockUsersService
from src.domain.use_cases.users.create import Create
from src.domain.use_cases.users.delete_by_id import DeleteById
from src.domain.use_cases.users.fetch_all import FetchAll
from src.domain.use_cases.users.find_by_id import FindById
from src.domain.use_cases.users.login import Login
from src.domain.use_cases.users.logout import Logout
from src.domain.use_cases.users.update import Update

user_service = MockUsersService()

def create(user):
    create_UC = Create(user_service)
    return create_UC.execute(user["name"], user['email'], user['password'])

def delete(user_id):
    delete_UC = DeleteById(user_service)
    return delete_UC.execute(user_id)

def login(user):
    login_UC = Login(user_service)
    return login_UC.execute(user['name'], user['password'])

def logout(user_id):
    logout_UC = Logout(user_service)
    return logout_UC.execute(user_id)

def fetch_all():
    fetch_all_UC = FetchAll(user_service)
    return fetch_all_UC.execute()

def find_by_id(user_id):
    find_by_id_UC = FindById(user_service)
    return find_by_id_UC.execute(user_id)

def update(user_id, user):
    update_UC = Update(user_service)
    return update_UC.execute(user_id, user['name'], user['email'], user['password'])
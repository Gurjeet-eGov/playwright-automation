import pytest
from api_clients.users_api import UsersAPI

@pytest.mark.api
def test_get_users():
    api = UsersAPI("https://reqres.in")
    response = api.get_users()
    assert response.status_code == 200

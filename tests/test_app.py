from app import create_app
import pytest
from create_db import create_db_table
import os
@pytest.fixture(scope="session", autouse=True)
# tmp_path_factory = default  fixture
def create_test_database(tmp_path_factory):
    # Temporary directory
    tmp_dir = tmp_path_factory.mktemp("tmp")
    database_filename = tmp_dir / "test_database.db"
    create_db_table(database_filename)
    # Envirement variable
    os.environ["DATABASE_FILENAME"] = str(database_filename)

@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app(__name__)
    testing_client = flask_app.test_client(use_cookies=False)
    context = flask_app.app_context()
    context.push()
    yield testing_client
    context.pop()


def test_api_add_user(test_client):
    expected_status_code = 200
    expected_message= "User added Successefully"
    response = test_client.post('/api/users/add', json={
        "name": "Yasmine Cherif",
        "email": "yasmine@gmail.com",
        "phone": "00000000",
        "address": "La Marsa Tunis",
        "country": "Tunisia"
    })
    assert expected_status_code == response.json['code']
    assert expected_message == response.json['message']

def test_api_add_user2(test_client):
    expected_status_code = 200
    expected_message= "User added Successefully"
    expected_body_keys = ["user_id", "name", "email","phone","address","country"]
    response = test_client.post('/api/users/add', json={
        "name": "Hela Cherif",
        "email": "hela@gmail.com",
        "phone": "00000000",
        "address": "La Marsa Tunis",
        "country": "Tunisia"
    })
    assert expected_status_code == response.json['code']
    assert expected_message == response.json['message']
    assert set(expected_body_keys) == response.json["user"].keys()
    assert int == type(response.json["user"]["user_id"])

def test_api_add_user3(test_client):
    expected_status_code = 200
    expected_message= "User added Successefully"
    expected_body_keys = ["user_id", "name", "email","phone","address","country"]
    response = test_client.post('/api/users/add', json={
        "name": "Melek Elloumi",
        "email": "melek@gmail.com",
        "phone": "00000000",
        "address": "sfax",
        "country": "Tunisia"
    })
    assert expected_status_code == response.json['code']
    assert expected_message == response.json['message']
    assert set(expected_body_keys) == response.json["user"].keys()
    assert int == type(response.json["user"]["user_id"])

def test_get_all_users(test_client):
    # Given
    expected_response = [
        {
            "name": "Yasmine Cherif",
            "email": "yasmine@gmail.com",
            "phone": "00000000",
            "address": "La Marsa Tunis",
            "country": "Tunisia",
            "user_id":1
        },
        {
            "name": "Hela Cherif",
            "email": "hela@gmail.com",
            "phone": "00000000",
            "address": "La Marsa Tunis",
            "country": "Tunisia",
            "user_id":2
        },
        {
            "name": "Melek Elloumi",
            "email": "melek@gmail.com",
            "phone": "00000000",
            "address": "sfax",
            "country": "Tunisia",
            "user_id":3
        }
    ]
    expected_status_code = 200

    # When
    response = test_client.get("/api/users")

    # Then
    assert expected_status_code == response.status_code
    assert expected_response == response.json

def test_delete_existing_user(test_client):
    # Given
    id_to_delete = 2
    expected_body = {
        "code": 201,
        "status": "User deleted successfully"
    }

    # When
    response = test_client.delete(f'/api/users/delete/{id_to_delete}')

    # Then
    assert expected_body == response.json

def test_get_all_users_after_delete(test_client):
    # Given
    expected_response = [
        {
            "name": "Yasmine Cherif",
            "email": "yasmine@gmail.com",
            "phone": "00000000",
            "address": "La Marsa Tunis",
            "country": "Tunisia",
            "user_id":1
        },
        {
            "name": "Melek Elloumi",
            "email": "melek@gmail.com",
            "phone": "00000000",
            "address": "sfax",
            "country": "Tunisia",
            "user_id":3
        }
    ]
    expected_status_code = 200

    # When
    response = test_client.get("/api/users")

    # Then
    assert expected_status_code == response.status_code
    assert expected_response == response.json

def test_delete_not_existing_user(test_client):
    # Given
    id_to_delete = 100
    expected_body = {
        "code": 404,
        "status": "Cannot delete user: user does not exist"
    }   

    # When
    response = test_client.delete(f'/api/users/delete/{id_to_delete}')

    # Then
    assert expected_body == response.json

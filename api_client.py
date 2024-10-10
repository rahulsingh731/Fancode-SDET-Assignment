import requests

Base_URL = "https://jsonplaceholder.typicode.com"


def get_users():
    """Fetch all users from /users endpoint."""
    response = requests.get(Base_URL + "/users")
    response.raise_for_status()
    return response.json()


def get_todos():
    """Fetch all todo list from /todos endpoint."""
    response = requests.get(Base_URL + "/todos")
    response.raise_for_status()
    return response.json()

def filter_fancode_users(users):
    """Filter users belonging to the FanCode city (lat: -40 to 5, lng: 5 to 100)."""
    fancode_users = [
        user for user in users
        if -40 <= float(user['address']['geo']['lat']) <= 5 and 5 <= float(user['address']['geo']['lng']) <= 100
    ]
    return fancode_users


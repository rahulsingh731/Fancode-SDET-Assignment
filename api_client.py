import requests

Base_URL = "https://jsonplaceholder.typicode.com"


def get_users(url):
    """Fetch all users from /users endpoint."""
    response = requests.get(url + "/users")
    response.raise_for_status()
    return response.json()


def filter_users(users):
    fancode_list = [user for user in users
                    if -40 <= float(user['address']['geo']['lat']) <= 5 and 5 <= float(
            user['address']['geo']['lng']) <= 100]
    return fancode_list


def get_todos(url):
    response = requests.get(url + "/todos")
    response.raise_for_status()
    return response.json()


def filter_todos(user, todos):
    user_todos = [i for i in todos if i['userId'] == user['id']]
    completed_todos = [todo for todo in user_todos if todo['completed']]
    if len(completed_todos) == 0:
        return 0
    return (len(completed_todos) / len(user_todos)) * 100


users = filter_users(get_users(Base_URL))
todos = get_todos(Base_URL)
# print(len(users))
# print(todos[1]['userId'])

for user in users:
    print(filter_todos(user, todos))

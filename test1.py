import requests
# from selenium import webdriver
# from selenium

Base_URL = "https://jsonplaceholder.typicode.com"

def get_users(URL):
    """Fetch all users from /users endpoint."""
    response = requests.get(URL+"/users")
    response.raise_for_status()
    return response.json()
users = get_users(Base_URL)
print(users[0]['address']['geo']['lat'])
FanCode City Todo Task Automation
Overview
This project automates checking if all users from the FanCode city have completed more than 50% of their todo tasks. It fetches user and task data from a mock API (JSONPlaceholder) and validates the task completion percentage based on the location of the users.

Setup Instructions
Prerequisites:
Python 3.x
Libraries:
requests
behave
pytest
Install the required libraries using pip:

bash
Copy code
pip install requests pytest behave
Installation:
Clone this repository to your local machine.
Navigate to the project folder and install dependencies:
bash
Copy code
pip install -r requirements.txt
How to Run the Tests:
You can run the tests using pytest for unit tests or behave for BDD tests.

For Unit Tests:

bash
Copy code
pytest test_fancode.py
For BDD Tests:

bash
Copy code
behave
How It Works
The validation process follows these steps:

Fetch Users: Retrieve all users from the /users API.
Filter FanCode Users: Identify users from FanCode city based on their geographical location:
Latitude between -40 and 5
Longitude between 5 and 100
Fetch Todos: Retrieve all tasks from the /todos API.
Check Task Completion: Calculate the task completion percentage for each user from FanCode.
Validate: Ensure that all users from FanCode city have completed more than 50% of their assigned tasks.

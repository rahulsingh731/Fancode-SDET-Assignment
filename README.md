
# FanCode City Todo Task Automation

## Overview
This project automates checking if all users from the **FanCode** city have completed more than **50%** of their todo tasks. It fetches user and task data from a mock API (JSONPlaceholder) and validates the task completion percentage based on the location of the users.

---

## Setup Instructions

### Prerequisites:
- **Python 3.x**
- **Libraries**: 
  - `requests`
  - `behave`
  - `pytest`

Install the required libraries using pip:

```bash
pip install requests pytest behave
```

### Installation:
1. Clone this repository to your local machine.
2. Navigate to the project folder and install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### How to Run the Tests:
<<<<<<< HEAD

You can run the tests using **`pytest`** for unit tests or **`behave`** for BDD tests.

- **For Unit Tests**:
   ```bash
   pytest test_fancode.py
   ```

- **For BDD Tests**:
   ```bash
   behave
   ```

---

## How It Works

The validation process follows these steps:

1. **Fetch Users**: Retrieve all users from the `/users` API.
2. **Filter FanCode Users**: Identify users from **FanCode city** based on their geographical location:
   - Latitude between **-40** and **5**
   - Longitude between **5** and **100**
3. **Fetch Todos**: Retrieve all tasks from the `/todos` API.
4. **Check Task Completion**: Calculate the task completion percentage for each user from **FanCode**.
5. **Validate**: Ensure that all users from **FanCode city** have completed more than **50%** of their assigned tasks.

---

### Example Scenario (BDD - Gherkin Syntax):

```gherkin
Feature: Validate todo completion for FanCode users

  Scenario: All users from FanCode city should have completed more than 50% of their tasks
    Given I have the list of users
    And I filter users from FanCode city
    When I fetch their todos
    Then I should see that all users from FanCode have more than 50% of tasks completed
```

---

=======

You can run the tests using **`pytest`** for unit tests or **`behave`** for BDD tests.

- **For Unit Tests**:
   ```bash
   pytest test_fancode.py
   ```

- **For BDD Tests**:
   ```bash
   behave
   ```

---

## How It Works

The validation process follows these steps:

1. **Fetch Users**: Retrieve all users from the `/users` API.
2. **Filter FanCode Users**: Identify users from **FanCode city** based on their geographical location:
   - Latitude between **-40** and **5**
   - Longitude between **5** and **100**
3. **Fetch Todos**: Retrieve all tasks from the `/todos` API.
4. **Check Task Completion**: Calculate the task completion percentage for each user from **FanCode**.
5. **Validate**: Ensure that all users from **FanCode city** have completed more than **50%** of their assigned tasks.

---

### Example Scenario (BDD - Gherkin Syntax):

```gherkin
Feature: Validate todo completion for FanCode users

  Scenario: All users from FanCode city should have completed more than 50% of their tasks
    Given I have the list of users
    And I filter users from FanCode city
    When I fetch their todos
    Then I should see that all users from FanCode have more than 50% of tasks completed
```

---

### Example Output

After running the validation script, the following output is possible:

1. **Success Case**:
   ```
   All users from FanCode city have more than 50% of their tasks completed.
   ```

2. **Failure Case** (when some users do not meet the task completion threshold):
   ```
   Users with low task completion: [('John Doe', 40.0), ('Jane Smith', 30.0)]
   ```
>>>>>>> 1c40e02e8cd92a3be2c1a7cd9fe0b8feda6200ae

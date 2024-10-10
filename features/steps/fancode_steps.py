from behave import given, when, then

import api_client
import logics


@given('I have the list of users')
def step_impl(context):
    context.users = api_client.get_users()

@given('I filter users from FanCode city')
def step_impl(context):
    context.fancode_users = api_client.filter_fancode_users(context.users)

@when('I fetch their todos')
def step_impl(context):
    context.todos = api_client.get_todos()

@then('I should see that all users from FanCode have more than 50% of tasks completed')
def step_impl(context):
    users_with_low_completion = logics.filter_users_fc(context.fancode_users, context.todos)
    assert len(users_with_low_completion) == 0, f"Users with low task completion: {users_with_low_completion}"

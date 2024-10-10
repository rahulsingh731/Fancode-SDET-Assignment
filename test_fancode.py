import api_client
import logics

def fancode_users_completion():
    users = api_client.get_users()
    fc_users = api_client.filter_fancode_users(users)
    todos = api_client.get_todos()
    user_with_loss_completion = logics.filter_users_fc(users,todos)

    assert len(user_with_loss_completion) == 0, f"Users with low task completion: {user_with_loss_completion}"
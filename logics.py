def calc_percentage(users,todos):
    """Calculate the percentage with status as completed"""
    user_todos = [i for i in todos if i['userId']==users['id']]
    completed_todos = [i for i in user_todos if i['completed']]

    if len(completed_todos)==0:
        return 0
    return (len(completed_todos)/len(user_todos))*100
def filter_users_fc(users,todos):
    """Return the users with low completion percentage"""
    users_with_low_completion = []
    for user in users:
        comp_percentage = calc_percentage(user,todos)
        if comp_percentage<50:
            users_with_low_completion.append((user['name'],comp_percentage))
    return users_with_low_completion
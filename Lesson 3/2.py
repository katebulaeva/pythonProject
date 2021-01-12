def create_user():
    user = {'name':'', 'surname':'', 'date of birth':'', 'city':'', 'email':'', 'phone number':''}
    for key, value in user.items():
        value = input(f'input {key} ')
        user [key] = value
    return user
print(create_user())
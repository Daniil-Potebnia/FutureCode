def add_dict(where, login, password):
    assert login not in [d.get('login') for d in where] or len(str(password)) < 8
    where.append([{'login': login, 'password': password}])

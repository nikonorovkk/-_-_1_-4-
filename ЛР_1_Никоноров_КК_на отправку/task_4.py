users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

Dict_ = {
    "Общее количество": 0,
    "Уникальные посещения": 0
}

count_of_users = len(users)
uniq_users = set(users)
count_of_uniq_users = len(uniq_users)

Dict_["Общее количество"] = count_of_users
Dict_["Уникальные посещения"] = count_of_uniq_users

print(Dict_)

# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений

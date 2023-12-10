users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']
whole= len(users)
unique = len(set(users))
dictionary = {
    "Общее количество": whole,
    "Уникальные посещения": unique
}
print(dictionary)
# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений

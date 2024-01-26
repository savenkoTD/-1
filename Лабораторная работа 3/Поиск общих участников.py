# TODO Напишите функцию find_common_participants
def find_common_participants(first, second, delimiter=','):
    first_set = set(first.split(delimiter))
    second_set = set(second.split(delimiter))

    common = first_set & second_set
    return sorted(list(common))

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

common_participants = find_common_participants(participants_first_group, participants_second_group, delimiter='|')
print(f"Общие участники: {common_participants}")
# TODO Провеьте работу функции с разделителем отличным от запятой

# Задание 1
# Необходимо вывести имена всех учеников из списка с новой строки

names = ['Оля', 'Петя', 'Вася', 'Маша']
# ???
for item in names:
    print(item)


# Задание 2
# Необходимо вывести имена всех учеников из списка, рядом с именем показать количество букв в нём
# Пример вывода:
# Оля: 3
# Петя: 4

names = ['Оля', 'Петя', 'Вася', 'Маша']
# ???
for item in names:
    print(f'{item}: {len(item)}')

# Задание 3
# Необходимо вывести имена всех учеников из списка, рядом с именем вывести пол ученика

is_male = {
    'Оля': False,  # если False, то пол женский
    'Петя': True,  # если True, то пол мужской
    'Вася': True,
    'Маша': False,
}
names = ['Оля', 'Петя', 'Вася', 'Маша']
# ???
for item in names:
    gender = "мужской" if is_male[item] else "женский"
    print(f'{item}: {gender}')


# Задание 4
# Даны группу учеников. Нужно вывести количество групп и для каждой группы – количество учеников в ней
# Пример вывода:
# Всего 2 группы.
# Группа 1: 2 ученика.
# Группа 2: 4 ученика.

groups = [
    ['Вася', 'Маша'],
    ['Вася', 'Маша', 'Саша', 'Женя'],
    ['Оля', 'Петя', 'Гриша'],
]
# ???
print(f'Всего {len(groups)} группы.')

group_number = 1
for group in groups:
    print(f'Группа {group_number}: {len(group)} ученика')
    group_number += 1

# Задание 5
# Для каждой пары учеников нужно с новой строки перечислить учеников, которые в неё входят
# Пример вывода:
# Группа 1: Вася, Маша
# Группа 2: Оля, Петя, Гриша

groups = [
    ['Вася', 'Маша'],
    ['Оля', 'Петя', 'Гриша'],
    ['Вася', 'Маша', 'Саша', 'Женя'],
]
# ???
group_number = 1
for group in groups:
    print(f'Группа {group_number}: {", ".join(group)}')
    group_number += 1
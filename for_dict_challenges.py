# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

from collections import Counter

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]
# ???
temp_list = [student['first_name'] for student in students]

count = Counter(temp_list)
for key, value in count.items():
    print(f'{key}: {value}')

# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]
# ???
temp_list = [student['first_name'] for student in students]
count = Counter(temp_list)
max_value = max(count.values())
for k, v in count.items():
    if v == max_value:
        print(f'Самое частое имя среди учеников: {k}')

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]
# ???
grade_number = 1
for grade in school_students:
    group = [student['first_name'] for student in grade]
    dict = Counter(group)
    max_in_group = max(dict.values())
    for k, v in dict.items():
        if v == max_in_group:
            print(f'Самое частое имя в классе {grade_number}: {k}')
    grade_number += 1

# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2б', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}
# ???
temp_dict = {}

for line in school:
    students = line['students']
    students_list = [student['first_name'] for student in students]

    existing_key = temp_dict.get(line['class'])
    if existing_key != None:
        existing_key += students_list
    else:
        temp_dict[line['class']] = students_list

for key, value in temp_dict.items():
    boys = 0
    girls = 0
    for student in value:
        if is_male.get(student):
            boys += 1
        else:
            girls += 1
    print(f'Класс {key}: девочки {girls}, мальчики {boys}')

# print(temp_dict) 

# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}
# ???
temp_dict = {}

for line in school:
    students = line['students']
    students_list = [student['first_name'] for student in students]

    existing_key = temp_dict.get(line['class'])
    if existing_key != None:
        existing_key += students_list
    else:
        temp_dict[line['class']] = students_list

result_boys = {'boys': 0, 'grade': ''}
result_girls = {'girls': 0, 'grade': ''}

for key, value in temp_dict.items():
    boys = 0
    girls = 0
    for student in value:
        if is_male.get(student):
            boys += 1
        else:
            girls += 1
    
    if girls > result_girls.get('girls', 0):
        result_girls['girls'] = girls
        result_girls['grade'] = key

    if boys > result_boys.get('boys', 0):
        result_boys['boys'] = boys
        result_boys['grade'] = key
    

print(f"Больше всего мальчиков в классе {result_boys['grade']}")
print(f"Больше всего девочек в классе {result_girls['grade']}")
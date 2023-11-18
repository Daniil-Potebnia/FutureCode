import names
import random


def create_people(n):  # люди, собирающиеся в поход
    people = []
    for _ in range(n):
        name = names.get_first_name()
        reg = random.choice('Москва Санкт-Петербург Рязань Псков Пермь Челябинск Казань Краснодар Ростов-на-Дону '
                            'Якутск Тюмень'.split())
        age = random.randint(15, 75)
        sal = random.randint(50, 200) * 1000
        exp = random.randint(0, age - 15)
        people.append({'Name': name, 'Region': reg, 'Age': age, 'Desired salary': sal,
                       'English': random.choice([True, False]), 'Work experience': exp,
                       'Stack': [random.choice(['палатка', 'топор', 'зажигалка', 'консервы', 'нож', 'запасная одежда',
                                                'верёвка', 'аэрозоль от насековмых', 'книга по выживанию',
                                                'медицинский набор']),
                                 random.choice(['палатка', 'топор', 'зажигалка', 'консервы', 'нож', 'запасная одежда',
                                                'верёвка', 'аэрозоль от насековмых', 'книга по выживанию',
                                                'медицинский набор']),
                                 random.choice(['палатка', 'топор', 'зажигалка', 'консервы', 'нож', 'запасная одежда',
                                                'верёвка', 'аэрозоль от насековмых', 'книга по выживанию',
                                                'медицинский набор'])]})
    return people


def delete_useless(people):  # удаление неподходящих людей
    new_list = []
    for person in people:
        if (18 < person['Age'] < 60 and person['Desired salary'] < 135_000 and
                person['English'] and person['Work experience'] > 1):
            new_list.append(person)
    return new_list


def find_the_best_one(people):  # сравнение по баллам, начисляемых в зависимости от возраста, 
    max_ = 0  # опыта работы и оборудования
    best = None
    for person in people:
        counter = 0
        if person['Age'] > 25:
            counter += (75 - person['Age']) // 2
        else:
            counter += 50 - (25 - person['Age'])

        counter += person['Work experience'] * 2

        for i in ['палатка', 'топор', 'зажигалка', 'консервы', 'нож', 'запасная одежда', 'верёвка',
                  'аэрозоль от насековмых', 'книга по выживанию', 'медицинский набор']:
            if i in person['Stack']:
                if i == 'палатка':
                    counter += 5
                elif i == 'топор':
                    counter += 7
                elif i == 'зажигалка':
                    counter += 4
                elif i == 'консервы':
                    counter += 2
                elif i == 'нож':
                    counter += 7
                elif i == 'запасная одежда':
                    counter += 5
                elif i == 'верёвка':
                    counter += 3
                elif i == 'аэрозоль от насековмых':
                    counter += 1
                elif i == 'книга по выживанию':
                    counter += 1
                elif i == 'медицинский набор':
                    counter += 6
        if counter > max_:
            max_ = counter
            best = person
    return best

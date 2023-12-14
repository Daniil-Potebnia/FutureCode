import json


class Person:
    def __init__(self, name, age, computer):
        self.name = name
        self.age = age
        self.computer = computer

    def to_json(self):
        with open('persons.json', mode='w') as f:
            f.write(json.dumps({'name': self.name, 'age': self.age, 'computer': self.computer.get_json()}))

    def __str__(self):
        return f'{self.name} {self.age}'


class Computer:
    def __init__(self, tip):
        self.tip = tip

    def to_json(self):
        with open('computers.json', mode='w') as f:
            f.write(json.dumps({'tip': self.tip}))

    def get_json(self):
        return {'tip': self.tip}


def create_from_json(struct):
    if struct == 'person':
        with open('persons.json', mode='r') as f:
            text = json.loads(f.read())
            return Person(text['name'], text['age'], Computer(text['computer']['tip']))
    elif struct == 'computer':
        with open('computers.json', mode='r') as f:
            text = json.loads(f.read())
            return Computer(text['computer']['tip'])

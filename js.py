import json


class Person:
    def __init__(self, name, age, computer):
        self.name = name
        self.age = age
        self.computer = computer

    def to_json(self):
        with open('persons.json', mode='w') as f:
            f.write(json.dumps({'name': self.name, 'age': self.age, 'computer': self.computer.get_json()}))


class Computer:
    def __init__(self, tip):
        self.tip = tip

    def to_json(self):
        with open('computers.json', mode='w') as f:
            f.write(json.dumps({'tip': self.tip}))

    def get_json(self):
        return {'tip': self.tip}

import random


class Warrior:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def attack(self, enemy):
        enemy.health -= self.damage


class Thief(Warrior):
    def __init__(self, name, health, damage, crit_chance):
        super().__init__(name, health, damage)
        self.crit_chance = crit_chance

    def attack(self, enemy):
        crit = True if random.randint(0, 100) < 16 else False
        enemy.health -= self.damage * 2 if crit else self.damage


if __name__ == '__main__':
    warrior_1 = Thief('Петя', 50, 9, 15)
    warrior_2 = Warrior('Васы', 75, 4)
    while warrior_1.health > 0 and warrior_2.health > 0:
        step = random.randint(0, 1)
        if not step:
            warrior_1.attack(warrior_2)
            print(f'{warrior_1.name} атаковал {warrior_2.name} и оставил ему {warrior_2.health} здоровья')
        else:
            warrior_2.attack(warrior_1)
            print(f'{warrior_2.name} атаковал {warrior_1.name} и оставил ему {warrior_1.health} здоровья')
    if warrior_1.health <= 0:
        print(f'{warrior_2.name} победил!!!')
    else:
        print(f'{warrior_1.name} победил!!!')

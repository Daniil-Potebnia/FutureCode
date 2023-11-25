import random
from abc import ABC, abstractmethod


class BaseWarrior(ABC):
    @abstractmethod
    def attack(self, enemy):
        pass

    @abstractmethod
    def spec_attack(self, enemy):
        pass

    @abstractmethod
    def protect(self):
        pass


class Warrior(BaseWarrior):
    def __init__(self, name, health, weapon, speed=5, armor=None, recharge=5):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.armor = armor
        self.protection = False
        self.max_speed = speed
        self.speed = speed
        self.dodge_chance = 0
        self.crit_chance = 0
        self.recharging = 0
        self.max_recharge = recharge
        self.debuff = None

    def attack(self, enemy):
        if self.recharging != 0:
            self.recharging -= 1
            self.weapon.simple_attack(self, enemy)
        else:
            self.spec_attack(enemy)
        if self.debuff == 'огонь':
            self.health -= 12
            self.debuff = None

    def spec_attack(self, enemy):
        print(f'{self.name} использует усиленную атаку')
        if self.recharging != 0:
            self.recharging -= 1
        if self.debuff == 'ветер':
            self.health -= 5
            self.protection = False
            self.debuff = None
        self.weapon.special_attack(self, enemy)

    def protect(self):
        if self.recharging != 0:
            self.recharging -= 1
        if self.debuff != 'лёд':
            self.protection = True
            if self.max_speed != self.speed:
                self.speed -= 1
        else:
            self.speed += 2
            self.debuff = None

    def __str__(self):
        return self.name


class Thief(Warrior):
    def __init__(self, name, health, dagger, crit_chance, speed=3, armor=None, recharge=3):
        super().__init__(name, health, dagger, speed=speed, armor=armor, recharge=recharge)
        self.crit_chance = crit_chance

    def __str__(self):
        return f"{self.name}-вор"


class Mage(Warrior):
    def __init__(self, name, health, staff, dodge_chance, speed=7, armor=None, recharge=2):
        super().__init__(name, health, staff, speed=speed, armor=armor, recharge=recharge)
        self.dodge_chance = dodge_chance

    def __str__(self):
        return f"{self.name}-маг"


class BaseWeapon(ABC):
    @abstractmethod
    def simple_attack(self, hero, enemy):
        pass

    @abstractmethod
    def special_attack(self, hero, enemy):
        pass


class Weapon(BaseWeapon):
    def __init__(self, damage, spec_skill=None, add_crit=0):
        self.damage = damage
        self.spec_skill = spec_skill
        self.add_crit = add_crit

    def simple_attack(self, hero, enemy):
        damage = (self.damage + self.damage * (hero.armor.damage_increase / 100))
        damage = round(damage - damage * (enemy.armor.defense / 100))
        if random.randint(0, 100) < hero.dodge_chance:
            hero.protection = True
        crit = True if random.randint(0, 100) < hero.crit_chance + self.add_crit else False
        if crit:
            enemy.health -= damage
        enemy.health -= damage if not enemy.protection else 0
        enemy.protection = False
        if enemy.health < 0:
            enemy.health = 0

    def special_attack(self, hero, enemy):
        self.simple_attack(hero, enemy)


class Staff(Weapon):
    def __init__(self, damage, element='огонь'):
        super().__init__(damage, spec_skill=element)

    def special_attack(self, hero: Warrior, enemy: Warrior):
        if not hero.recharging:
            enemy.debuff = self.spec_skill
            hero.recharging = hero.max_recharge
            self.spec_skill = random.choice(['огонь', 'лёд', 'ветер'])
        self.simple_attack(hero, enemy)


class Dagger(Weapon):
    def __init__(self, damage, add_crit):
        super().__init__(damage, add_crit=add_crit)

    def special_attack(self, hero: Warrior, enemy: Warrior):
        if not hero.recharging:
            usual_add = self.add_crit
            self.add_crit += 30
            self.simple_attack(hero, enemy)
            self.add_crit = usual_add
            hero.recharging = hero.max_recharge
        else:
            self.simple_attack(hero, enemy)


class Armor:
    def __init__(self, defense, damage_increase):
        self.defense = defense
        self.damage_increase = damage_increase


if __name__ == '__main__':
    warrior_1 = Thief('Петя', 40, Dagger(12, 5), 15, armor=Armor(20, 30), speed=4)
    warrior_2 = Mage('Вася', 65, Staff(11, element=random.choice(['огонь', 'лёд', 'ветер'])), 30,
                     armor=Armor(40, 10), speed=6)
    counter = 0
    while True:
        if not counter % warrior_1.speed:
            if warrior_1.health <= 0:
                print(f'{warrior_2} победил!!!')
                break
            action = random.randint(0, 1)
            if action or warrior_1.protection:
                warrior_1.attack(warrior_2)
                print(f'{warrior_1} атаковал {warrior_2} и оставил ему {warrior_2.health} здоровья')
            else:
                warrior_1.protect()
                print(f'{warrior_1.name} решил защититься')
        if not counter % warrior_2.speed:
            if warrior_2.health <= 0:
                print(f'{warrior_1} победил!!!')
                break
            action = random.randint(0, 1)
            if action or warrior_2.protection:
                warrior_2.attack(warrior_1)
                print(f'{warrior_2} атаковал {warrior_1} и оставил ему {warrior_1.health} здоровья')
            else:
                warrior_2.protect()
                print(f'{warrior_2} решил защититься')
        counter += 1

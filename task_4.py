import random
import matplotlib.pyplot as mt


class Weapon:
    def __init__(self, name: str, damage: int):
        self.name = name
        self.damage = damage
        self.special = True

    def attack(self, enemy):
        enemy.health -= self.damage

    def special_attack(self, enemy, me):
        pass

    def __repr__(self):
        return f'{self.name}(способность{" не" if self.special else ""} использована)'


class Bow(Weapon):
    def special_attack(self, enemy, me):
        enemy.health -= self.damage * 2
        if enemy.health <= 0:
            enemy.alive = False


class Sword(Weapon):
    def special_attack(self, enemy, me):
        me.defence = True
        enemy.health -= self.damage
        if enemy.health <= 0:
            enemy.alive = False


class Warrior:
    def __init__(self, name: str, health: int, weapon):
        while True:
            new_id = random.randint(1, 500)
            if new_id in ids:
                new_id = random.randint(1, 500)
            else:
                break
        self.id = new_id
        self.name = name
        self.health = health
        self.start_health = health
        self.weapon = weapon
        self.inventory = []
        self.defence = False
        self.can_def = True
        self.alive = True

    def reset(self):
        self.health = self.start_health

    def has_special_attack(self):
        return self.weapon.special

    def set_special_attack_false(self):
        self.weapon.special = False

    def hit(self, enemy):
        if not enemy.defence:
            self.weapon.attack(enemy)
            enemy.can_def = True
            if enemy.health <= 0:
                enemy.alive = False
        else:
            enemy.defence = False

    def defence_yourself(self):
        self.defence = True
        self.can_def = False

    def is_alive(self):
        return self.alive

    def add_weapon(self, new_weapon: Weapon):
        self.inventory.append(self.weapon)
        self.weapon = new_weapon

    def swap_weapon(self):
        weapons = list(map(lambda x: x.name, self.inventory))
        while True:
            new_weapon = input(f"Выберите - {', '.join(weapons)}:\n")
            if new_weapon not in weapons:
                print('Такого оружия нет')
                continue
            else:
                break
        for item in self.inventory:
            if item.name == new_weapon:
                self.weapon = item

    def __str__(self):
        return f'{self.name.capitalize()} - {self.health} здоровья, {"может" if self.can_def else "не может"} ' \
               f'защищаться, сейчас {"" if self.defence else "не"} под защитой, наносит {self.weapon.damage} ' \
               f'урона с удара, оружие - {self.weapon}'


class Battle:
    def __init__(self, first, second: Warrior):
        self.warriors = [first, second]
        self.step = 0
        self.wins = []

    def battle_loop(self, amount_of_games=1):
        count = 0
        while count < amount_of_games:
            self.warriors[0].reset()
            self.warriors[1].reset()
            self.step = random.randint(1, 2)
            while True:
                print('(Также напоминаем, что в любой момент боя вы можете поменять оружие, если у вас их больше 1, '
                      'используя действие "Поменять оружие" или добавить новое - "Добавить оружие")')
                print(self.warriors[0])
                print(self.warriors[1])
                print(self.warriors[self.step - 1].name.capitalize(), 'ходит')
                if self.step == 1:
                    active_player = self.warriors[0]
                    inactive_player = self.warriors[1]
                else:
                    active_player = self.warriors[1]
                    inactive_player = self.warriors[0]
                while True:
                    if not active_player.can_def:
                        step = input('Введите действие: удар\n')
                    else:
                        step = input('Введите действие: удар, защита\n')
                    if step not in ['удар', 'защита', 'Поменять оружие', 'Добавить оружие'] or \
                            not active_player.can_def and step == 'защита':
                        print(f'{step} - недопустимый ход')
                    else:
                        break
                if step == 'удар':
                    if active_player.has_special_attack():
                        answer = input(f'Хотите использовать способность "{active_player.weapon.name}"(да/нет):\n')
                        if answer == 'да':
                            active_player.set_special_attack_false()
                            active_player.weapon.special_attack(inactive_player, active_player)
                        else:
                            active_player.hit(inactive_player)
                    else:
                        active_player.hit(inactive_player)
                elif step == 'защита':
                    active_player.defence_yourself()
                elif step == 'Поменять оружие':
                    active_player.swap_weapon()
                elif step == 'Добавить оружие':
                    active_player.add_weapon(create_new_weapon())
                if not inactive_player.is_alive():
                    print(f'Победитель - {active_player.name}\n\n')
                    self.wins.append(active_player.id)
                    break
                self.step = 1 if self.step == 2 else 2
            count += 1

    def show_diagrams(self):
        x = list(range(1, len(self.wins) + 1))
        y = []
        count = 0
        for win in self.wins:
            if win == warrior_1.id:
                count += 1
            y.append(count)
        mt.xlabel('Игры')
        mt.ylabel(self.warriors[0].name)
        mt.plot(x, y, color='green', marker='o')
        mt.show()


def create_new_weapon():
    name = input('Введите название оружия:\n')
    while True:
        damage = input('Введите урон оружия:\n')
        if not damage.isdigit():
            print('Урон не числового типа')
        else:
            damage = int(damage)
            break
    while True:
        type_ = input('Введите тип оружия(лук, меч):\n')
        if type_ not in ['лук', 'меч']:
            print('Нет данного типа')
        else:
            if type_ == 'лук':
                return Bow(name, damage)
            elif type_ == 'меч':
                return Sword(name, damage)


ids = []


if __name__ == '__main__':
    warrior_1 = Warrior('Людвиг', 1, Bow('Зелёный лук', 6))
    warrior_2 = Warrior('Даниил', 1, Sword('Огненный клинок', 10))
    battle = Battle(warrior_1, warrior_2)
    while True:
        n = input('Введите количсетво битв:\n')
        if n.isdigit():
            n = int(n)
            break
        print('Это не число')
    battle.battle_loop(n)
    battle.show_diagrams()

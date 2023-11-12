import random


class Warrior:
    def __init__(self, name: str, health, damage: int):
        self.name = name
        self.health = health
        self.damage = damage
        self.defence = False
        self.can_def = True
        self.alive = True

    def hit(self, enemy):
        if not enemy.defence:
            enemy.health -= self.damage
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

    def __str__(self):
        return f'{self.name.capitalize()} - {self.health} здоровья, {"может" if self.can_def else "не может"} ' \
               f'защищаться, сейчас {"" if self.defence else "не"} под защитой, наносит {self.damage} урона с удара'


class Battle:
    def __init__(self, first, second: Warrior):
        self.warriors = [first, second]
        self.step = 0

    def battle_loop(self):
        self.step = random.randint(1, 2)
        while True:
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
                if step not in ['удар', 'защита'] or not active_player.can_def and step == 'защита':
                    print(f'{step} - недопустимый ход')
                else:
                    break
            if step == 'удар':
                active_player.hit(inactive_player)
            elif step == 'защита':
                active_player.defence_yourself()
            if not inactive_player.is_alive():
                print(f'Победитель - {active_player.name}')
                break
            self.step = 1 if self.step == 2 else 2


if __name__ == '__main__':
    warrior_1 = Warrior('Людвиг', 50, 6)
    warrior_2 = Warrior('Даниил', 37, 8)
    battle = Battle(warrior_1, warrior_2)
    battle.battle_loop()

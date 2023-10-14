
class Warrior:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.damage = 20

    def attack(self, enemy):
        damage = self.damage
        enemy.health -= damage
        print(f"{self.name} атакует {enemy.name} и наносит {damage} урона.")
        print(f"{enemy.name} осталось {enemy.health} здоровья.")

    def is_alive(self):
        return self.health > 0

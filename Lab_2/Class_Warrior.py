
class Warrior:
    def __init__(self, name):
        # Конструктор класса Warrior, инициализирует объект воина с заданным именем.
        self.name = name
        self.health = 100  # Устанавливаем начальное здоровье в 100 очков.
        self.damage = 20   # Устанавливаем урон, который наносит воин при атаке, в 20 очков.

    def attack(self, enemy):
        # Метод attack позволяет воину атаковать другого воина (передается как аргумент enemy).
        damage = self.damage  # Определяем урон воина.
        enemy.health -= damage  # Уменьшаем здоровье врага на величину damage.
        print(f"{self.name} атакует {enemy.name} и наносит {damage} урона.")
        print(f"{enemy.name} осталось {enemy.health} здоровья.")

    def is_alive(self):
        # Метод is_alive проверяет, жив ли воин, основываясь на его текущем здоровье.
        return self.health > 0
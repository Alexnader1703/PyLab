
class Warrior:
    def __init__(self, name,health,damage):
        # Конструктор класса Warrior, инициализирует объект воина с заданным именем.
        self.name = name
        self.health = health  # Устанавливаем начальное здоровье .
        self.damage = damage   # Устанавливаем урон, который наносит воин при атаке.

    def attack(self, enemy):
        # Метод attack позволяет воину атаковать другого воина (передается как аргумент enemy).
        enemy.health -= self.damage  # Уменьшаем здоровье врага на величину damage.
        print(f"{self.name} атакует {enemy.name} и наносит {self.damage} урона.")
        print(f"{enemy.name} осталось {enemy.health} здоровья.")

    def is_alive(self):
        # Метод is_alive проверяет, жив ли воин, основываясь на его текущем здоровье.
        return self.health > 0
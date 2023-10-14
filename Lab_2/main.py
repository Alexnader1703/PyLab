from Class_Warrior import Warrior
import random
hero1 = Warrior("Воин 1")  # Создаем первого воина.
hero2 = Warrior("Воин 2")  # Создаем второго воина.

while hero1.is_alive() and hero2.is_alive():#пока оба воина живы.
    attacker = random.choice([hero1, hero2])  # Случайным образом выбираем, кто атакует.
    enemy = hero2 if attacker == hero1 else hero1  # Определяем, кто является врагом атакующего.
    attacker.attack(enemy)  # Вызываем метод атаки для атакующего воина.

if hero1.is_alive():#Определяем победителя
    print(f"{hero1.name} победил!")
else:
    print(f"{hero2.name} победил!")
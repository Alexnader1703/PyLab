from Class_Warrior import Warrior
import random
hero1 = Warrior("Воин 1")
hero2 = Warrior("Воин 2")

while hero1.is_alive() and hero2.is_alive():
    attacker = random.choice([hero1, hero2])
    enemy = hero2 if attacker == hero1 else hero1
    attacker.attack(enemy)

if hero1.is_alive():
    print(f"{hero1.name} победил!")
else:
    print(f"{hero2.name} победил!")
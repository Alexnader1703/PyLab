import random
def R_Input():
    n = int(input("Кол-во чисел: "))

    s = ""
    for i in (range(n)):
        s += str(random.randint(-10000, 10000)) + ','

    file = open('Input.txt', 'w')
    file.write(str(s[:-1]))
R_Input()
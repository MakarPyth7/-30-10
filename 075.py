import random

number = [random.randint(100, 999), random.randint(100, 999), random.randint(100, 999)]

for num in number:
    print(num)

unumber = int(input("Введите число из трёх чисел:"))

try:
    s = number.index(unumber)
    print(s)
except ValueError:
    print("That is not in the list")
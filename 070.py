list = ("Россия", "Америка", "Беларусь", "Украина", "Испания")

for contries in list:
    print(contries)

contryID = int(input("Напишите ID страны:"))
try:
    print(list[contryID])
except IndexError:
    print("Не найдено")

list = ("Россия", "Америка", "Беларусь", "Украина", "Испания")

for contries in list:
    print(contries)

fcontry = input("Введите страну:").capitalize()

print(list.index(fcontry))


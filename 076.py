people = input("Ведите имя человека, которого хотите пригласить на вечеринку:").capitalize()
people1 = input("Ведите имя второго человека, которого хотите пригласить на вечеринку:").capitalize()
people2 = input("Ведите имя третьего человека, которого хотите пригласить на вечеринку:").capitalize()

party = [people, people1, people2]
while True:
    u = input("Хотите добавить ещё когото?").capitalize()
    if u == "Да":
        us = input("Кого вы хотите добавить?").capitalize()
        party += us
    elif u == "Нет":
        print("Вы пригласили", len(party), "людей")
        break
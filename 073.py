food = input("Введите ваше любимое блюдо:").capitalize()
food1 = input("Введите ваше любимое блюдо:").capitalize()
food2 = input("Введите ваше любимое блюдо:").capitalize()
food3 = input("Введите ваше любимое блюдо:").capitalize()
al = ""
foodlikes = [al, food, food1, food2, food3]

print(foodlikes)

fol = input("Какое блюдо вы хотите убрать:").capitalize()

foodlikes.remove(fol)

foodlikes.sort()

print(foodlikes)

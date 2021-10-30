fsports = ["football", "tennis"]

userfsport = input("Любимый спорт:").capitalize()

fsports.append(userfsport)

fsports.sort()

for sport in fsports:
    print(sport)
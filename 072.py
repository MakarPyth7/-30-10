subjects = ["Алгебра", "Химия", "Русский", "Белоруский", "Физра", "Биология"]

for sub in subjects:
    print(sub)

subID = input("Введите не любимый предмет:").capitalize()

subjects.remove(subID)

print(subjects)

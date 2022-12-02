import random
number = random.randint (1, 100)

if number < 45:
    print("common")
elif number >= 45 and number < 70:
    print("uncommon")
elif number >= 70 and number < 90:
    print("rare")
elif number >= 90 and number < 100:
    print("epic")
elif number == 100:
    print("legendary")

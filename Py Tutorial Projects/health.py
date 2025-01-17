import random

health = 50
diff = input("Enter difficulty level (easy, mid or hard): ").capitalize()

if (diff == "Easy" or diff == "E"):
    potion = random.randint(1,50)

elif (diff == "Mid" or diff == "M"):
    potion = random.randint(1,30)

elif (diff == "Hard" or diff == "H"):
    potion = random.randint(1,10)


health += potion

final_health = health
print(final_health)
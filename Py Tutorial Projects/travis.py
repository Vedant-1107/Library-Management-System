known_users = ["Alice", "Dan", "Bob", "Candice", "Ron", "Eve"]

print(len(known_users))
flag = True

while flag == True:
    print("Hi! My name is Travis.")
    name = input("What's your name? ").capitalize()
    if name in known_users:
        print(f"Welcome back, {name}!")
        ask = input("Would you like to remove yourself from the list?(y/n): ").capitalize()
        if ask == "Y" or ask == "Yes":
            known_users.remove(name)
        else:
            flag = False
    else:
        print(f"Hello {name}, I don't think we have met before.")
        ask = input("Would you like to add yourself to the list?(y/n): ").capitalize()
        if ask == "Y" or ask == "Yes":
            known_users.append(name)
        else:
            flag = False
#{film name : [min age, no. of tickets]}

films = {"Avengers": [12, 34],
         "Batman" : [15, 50],
         "Pirates of Carribean" : [10, 12],
         "Cars" : [5, 2]
        }

while True:
    movie = input("Which Movie would you like to watch? ").capitalize().strip()

    if movie in films:
        age = int(input("How old are you? "))

        if age >= films[movie][0]:
            print(f"You can buy tickets for {movie}")
            tickets = input("How many Tickets would you like to buy? ")

            if int(tickets) <= films[movie][1]:
                print(f"You have successfully bought {tickets} tickets for {movie}")
                films[movie][1] = films[movie][1] - 1

            else:
                print(f"Sorry we are HOUSEFULL for {movie}")
                break

        else:
            print(f"You are too young to watch {movie}")
            break

    else:
        print(f"{movie} is not in our database. Please try again.")
        break
email = input("Enter your E-mail id: ")


user = email[:email.index("@")]
domain = email[email.index("@") + 1:]

print(f"Your User Name is {user} and your domain is {domain}")
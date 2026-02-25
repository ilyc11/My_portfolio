import random
print("Hello, World!")
print("Learning about commits today!")
print("I understand how to commit a change now, and push it to GitHub.")

greetings = [
    "Hello, Git!",
    "Greetings, developer!",
    "Welcome to branching!",
    "Hi there, coding friend!",
    "Happy coding!"
]


def get_random_greeting():
    return random.choice(greetings)


print(get_random_greeting())
print("Learning about branches today!")

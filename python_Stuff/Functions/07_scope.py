counter = 1

while counter <= 10:
     text = f"Iteration {counter}"
     print(text)
     counter += 1

print(f"Outside: {text}") # The loop variable remains available outside the loop in Python


def greet_somebody(name):
    greeting = f"Hello, {name}! You the man!"
    return greeting

greet_somebody(greet_somebody("Cristiano Ronaldo"))

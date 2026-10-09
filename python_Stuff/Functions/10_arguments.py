def average(*args):
    return sum(args) / len(args)

print(average(1,2,5,8,10)) 



def greet(**kwargs): # Keyword args
    for key, value in kwargs.items():
        print(f"{key}: {value}")

greet(name="Cristian Ronaldo", age=42, city="Madrid")
greet(name="Lionel Messi", country="Argentina")


print("d", "e", "w", "q", sep="---") # Concatenation of two lists
name = "Ishaan"
age = 24
is_learning = True
skills = ["Python", "Django", "ML"]

print(f"Hey, I'm {name}, {age} years old, learning {skills[0]}")


quote = "learning python is fun"
print(quote.title())
print(quote.replace("python", "AI"))
print(f"Reversed: {quote[::-1]}")


numbers = [1, 2, 3, 4, 5]
squares = [n**2 for n in numbers]
for n in numbers:
    print(f"{n} squared is {n**2}")


def greet(user):
    return f"Hello, {user}! Keep learning."

print(greet("Ishaan"))


def greet(user):
    return f"Hello, {user}! Keep learning."

print(greet("Ishaan"))

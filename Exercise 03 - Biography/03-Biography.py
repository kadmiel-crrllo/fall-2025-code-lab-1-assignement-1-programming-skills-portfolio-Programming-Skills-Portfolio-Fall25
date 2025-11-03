print("Welcome! Let's create a biography.")
name = input("What is your full name? ")
city = input("Which city do you live in? ")
while True:
    age_input = input("How old are you? ")
    try:
        age = int(age_input)
        break
    except ValueError:
        print("Please enter a valid integer for your age. e.g., 25 instead of twenty-five.")
bio = {
    "name": name,
    "hometown": city,
    "age": age
}

print(f"Name: {bio['name']}\nHometown: {bio['hometown']}\nAge: {bio['age']}")
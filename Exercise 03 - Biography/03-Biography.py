# say hi to the user
print("Welcome! Let's create a biography.")

# ask for their name and store it in "name"
name = input("What is your full name? ")

# ask which city they live in and store it in "city"
city = input("Which city do you live in? ")

# keep asking for age until the user types a number
while True:
    age_input = input("How old are you? ")
    try:
        # try changing the input into an integer
        age = int(age_input)
        break  # stop the loop if it works
    except ValueError:
        # if it fails, tell them to type a number
        print("Please enter a valid integer for your age. e.g., 25 instead of twenty-five.")

# make a small dictionary to store all the info
bio = {
    "name": name,
    "hometown": city,
    "age": age
}

# show the stored info nicely
print(f"Name: {bio['name']}\nHometown: {bio['hometown']}\nAge: {bio['age']}")
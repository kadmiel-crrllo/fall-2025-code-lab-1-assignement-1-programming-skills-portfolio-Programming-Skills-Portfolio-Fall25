# make a list (dictionary) of countries and their capitals
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
    "Italy": "Rome",
    "Spain": "Madrid",
    "United Kingdom": "London",
    "Portugal": "Lisbon",
    "Netherlands": "Amsterdam",
    "Sweden": "Stockholm",
    "Poland": "Warsaw",
    "Greece": "Athens"
}

# start the score at 0
score = 0

# loop through each country and its capital
for country, capital in capitals.items():
    # ask the user for the capital of each country
    answer = input(f"What is the capital of {country}? ")

    # check if the user’s answer is correct (ignores spaces and letter case)
    if answer.strip().lower() == capital.lower():
        print("Correct!")
        score += 1  # add one point for correct answer
    else:
        # show the right answer if the user got it wrong
        print(f"Wrong! The correct answer is {capital}.")

# show the final score after all questions
print(f"\nQuiz completed! Your score: {score}/10")

# wait for the user to press Enter before closing the program
input("Press Enter to close...")
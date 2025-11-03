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

score = 0

for country, capital in capitals.items():
    answer = input(f"What is the capital of {country}? ")
    
    if answer.strip().lower() == capital.lower():
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The correct answer is {capital}.")

print(f"\nQuiz completed! Your score: {score}/10")
input("Press Enter to close...")
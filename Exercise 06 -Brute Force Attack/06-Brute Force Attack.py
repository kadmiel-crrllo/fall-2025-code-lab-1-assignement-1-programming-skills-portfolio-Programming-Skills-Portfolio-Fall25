correct_pw = "12345"
attempts = 0
max = 5

while attempts < max:
    password = input("Enter password: ")
    
    if password == correct_pw:
        print("Access granted!")
        break
    else:
        attempts += 1
        remaining = max - attempts
        print(f"Wrong password. {remaining} attempts remaining.")
        
        if attempts == max:
            print("You've entered the wrong password more than 5 times. Try to reset your password or contact support.")
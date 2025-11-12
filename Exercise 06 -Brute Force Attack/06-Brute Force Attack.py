# set the correct password
correct_pw = "12345"

# start counting attempts
attempts = 0

# max number of tries allowed
max = 5

# keep asking for password until user gets it or runs out of tries
while attempts < max:
    password = input("Enter password: ")

    # if the password is correct
    if password == correct_pw:
        print("Access granted!")
        break
    else:
        # add one to the number of wrong tries
        attempts += 1
        remaining = max - attempts
        print(f"Wrong password. {remaining} attempts remaining.")

        # show message if user runs out of tries
        if attempts == max:
            print("You've entered the wrong password more than 5 times. Try to reset your password or contact support.")

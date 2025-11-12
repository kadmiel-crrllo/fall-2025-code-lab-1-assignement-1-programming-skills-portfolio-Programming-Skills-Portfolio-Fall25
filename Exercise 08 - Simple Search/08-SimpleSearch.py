# list of names
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

# ask the user who they’re searching for
search_name = input("Input the name of who you are looking for: ")

# check if the name is in the list
if search_name in names:
    # find where the name is in the list (add 1 to make it seat number)
    seat = names.index(search_name) + 1
    print(f"Found {search_name}! they are at seat {seat}.")
else:
    # if the name isn’t there, show a message
    print(f"Sorry, {search_name} is not in the list.")
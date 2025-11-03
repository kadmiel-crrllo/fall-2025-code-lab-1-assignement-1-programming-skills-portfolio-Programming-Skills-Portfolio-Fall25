names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

search_name = input("Input the name of who you are looking for:")

if search_name in names:
    seat = names.index(search_name) + 1
    print(f"Found {search_name}! they are at seat {seat}.")
else:
    print(f"Sorry, {search_name} is not in the list.")
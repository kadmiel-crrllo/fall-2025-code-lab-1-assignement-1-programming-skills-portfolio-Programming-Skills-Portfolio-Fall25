# function that checks if a number is even or odd
def even_odd_messages(num):
    if num % 2 == 0:
        return f"{num} is even"
    else: 
        return f"{num} is odd"

# main function to get input and show result
def main():
    o = int(input("enter a number: "))  # get number from user
    message = even_odd_messages(o)      # call the function and store result
    print(message)                      # print the message

# run the main function
main()

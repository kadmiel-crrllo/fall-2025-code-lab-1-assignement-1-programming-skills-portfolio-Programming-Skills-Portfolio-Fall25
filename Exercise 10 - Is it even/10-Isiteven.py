def even_odd_messages(num):
    if num % 2 == 0:
        return f"{num} is even"
    else: 
        return f"{num} is odd"
    
def main():
    o = int(input("enter a number: "))
    message = even_odd_messages(o)
    print(message)

main()    
print("----- Even or Odd -----")

# while True:
#     num = int(input("Enter a number and I will tell you whether it is even or odd: "))

#     if num % 2 == 0:
#         print("This is an even number.")
#     else:
#         print("This is an odd number.")

def even_or_odd(number):
    if number % 2 == 0:
        print("This is an even number.")
    else:
        print("This is an odd number.")
while True:
    number = int(input("Enter a number: "))
    even_or_odd(number)

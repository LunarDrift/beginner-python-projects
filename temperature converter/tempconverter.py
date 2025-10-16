print("-----TEMPERATURE CONVERTER-----\n")
#THE CODE I CAME UP WITH

while True:
    temp = int(input("Enter the temperature: "))
    conversion_type = int(input("Choose a conversion type (1 for Farenheit to Celcius, 2 for Celcius to Farenheit): "))

    if conversion_type == 1:
        new_temp = (temp - 32) * 5/9
        print(f"{temp}°Farenheit is {new_temp}°Celcius")

    elif conversion_type == 2:
        new_temp = (temp * 9/5) + 32
        print(f"{temp}°Celcius is {new_temp}°Farenheit")

    else:
        print("Please enter a valid input. '1' for °F to °C. '2' for °C to °F")


#W3RESOURCE SOLUTION CODE:

def f_to_c(f):
    c = (f-32) * 5/9
    return round(c, 3)

def c_to_f(c):
    f = (c * 9/5) + 32
    return round(f, 3)
while True:
    try:

        temp = float(input("Enter temperature: "))

        conversion_type = int(input("Select a conversion type. 1 for Farenheit to Celcius, 2 for Celcius to Farenheit: "))

        if conversion_type == 1:
            new_temp = f_to_c(temp)
            print(f"{temp}°F is {new_temp}°C")

        elif conversion_type == 2:
            new_temp = c_to_f(temp)
            print(f"{temp}°C is {new_temp}°F")

        else:
            print("Invalid selection. Please choose 1 or 2")
    except ValueError:
        print("Invalid input. Please enter a valid number for the temperature.")
    
    run_again = input("Do you want to convert another temperature? (yes/no): ")
    if run_again.lower() not in ["yes", "y"]:
        print("Exiting program")
        break
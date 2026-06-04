print("---WELCOME TO MY MULTI-USE CALCULATOR---")
print("---BUILT BY STRIDER/OWEN---")
print("                                 Github: CodeWithOwen20")


def standard_calculator():
    print("\n--- STANDARD CALCULATOR---")

def miles_to_km():
    print("\n--- MILES TO KM CONVERTER---")

def celcius_to_fahrenheit():
    print("\n---CELCIUS TO FAHRENHEIT CALCULATOR")

while True:
    print("\n==============================")
    print("     STRIDERS ALL AROUND CALC V1     ")
    print("================================")
    print("1. Standard Calculator")
    print("2. Miles to Kilometers Converter")
    print("3. Celcius to Fahrenheit Converter")
    print("4. Exit Calculator")
    print("5. More Information")

    choice = input("Please select the relevant option (1-4): ")

    if choice == "1":

        num1 = float(input("Please enter your first number: "))
        num2 = float(input("Please enter your second number: "))

        print("\nChoose an Operation:")
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiply (*)")
        print("4. Divide (/)")


        calc_choice = input("Select an option (1-4): ")
        if calc_choice == "1":
            output_addition = num1 + num2
            print(output_addition)

        elif calc_choice == "2":
            output_subtraction = num1 - num2
            print(output_subtraction)

        elif calc_choice == "3":
            output_multiplication = num1 * num2
            print(output_multiplication)

        elif calc_choice == "4":
            if num2 == 0:
                print("[ERROR] You cant divide by Zero! Please pick another number...")
            else:
                output_division = num1 / num2
                print(output_division)

        
        standard_calculator()


    elif choice == "2":
        miles = float(input("Please enter the Miles:  "))

        kilometers = miles * 1.60934

        print(f"{miles} is equivalent to {kilometers}.")

        miles_to_km()

    elif choice == "3":
        celcius = float(input("Please enter the celcius: "))

        fahrenheit = (celcius * 1.8) + 32

        print(f"{celcius} Celcius is {fahrenheit} Fahrenheit.")

        celcius_to_fahrenheit()

    elif choice == "4":
        print("\nThank you for using my calculator:) Take care, bye!")
        break

    elif choice == "5":
        print("\nHiya, the calculator is my second official Python project that is entirely built by myself (Owen). I know")
        print("\nIts not much, but hopefully it becomes somewhat useful for someone learning the same as me or")
        print("\nfor general use:). Anyways, thank you for using my calculator and take care!")

    
    else:
        print("\n[ERROR] Your choice is not recognised. Please enter a number from 1 to 4.")






        #Second project complete
        
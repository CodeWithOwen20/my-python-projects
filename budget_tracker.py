import os
import tempfile
date_completed = "04/06/2026 at 23:39GMT+1"

def show_temporary_message():
    with tempfile.NamedTemporaryFile(delete=False, suffix=".txt", mode="w", encoding="utf-8") as temp_file:

        temp_file.write("=====================================\n")

        temp_file.write("        MADE BY CODEWITHOWEN20       \n")
        temp_file.write("=====================================\n\n")
        temp_file.write("\nHey there! Sorry for the disruption, this is just a test. Im still learning\n")
        temp_file.write("\nabout file I/O and handling in general. So dont worry, nothing has changed or been added,\n")
        temp_file.write("\nyou can safely close this file and carry on:) Enjoy!\n")
        
        temp_file_path = temp_file.name

    os.system(f'start "" "{temp_file_path}"')

     

def budget_calculator():

    print("\nIf you have used this program before, you will have already input your income and it is likely saved on your system.")
    print("\nThe text file is called: income_tracker.txt - Please check you have this before proceeding.")
    print("===============================================================")
    userinput = input("Have you already used this program before? (Y/N) ").lower()

    if userinput == "y":
        print("Ok. Getting file....")

        try:
            print("File found!")
            with open("income_tracker.txt", "r") as file:
                for line in file:
                    print(line.strip())
            print("Above is your Income.")
            print("\nYour income was not changed.")
        except FileNotFoundError:
            print("[ERROR] File not found! Are you sure you have a saved income? Please try again.")

    elif userinput == "n":

        income = float(input("Please enter your monthly income: "))

        needs = income * 0.50
        wants = income * 0.30
        savings = income * 0.20

        print(f"You need £{needs:.2f}, you want to spend £{wants:.2f} and realistically, you must save £{savings:.2f}")

        monthly_income = f"Income : £{income}"
        with open("income_tracker.txt", "a") as file:
            file.write(monthly_income)
            
        print("A file with the income you input has been saved to a text file.")
        print("Successfully saved income_tracker.txt! Check it out.")

    else:
        print("Choice not recognised. Please respond with Y (for Yes) or N (For no) ")



def expense_logger():
    purchased_item = input("What did you buy?: ")
    cost_of_item = float(input("How much did it cost?: "))
    
    log_entry = f"{purchased_item} : Cost £{cost_of_item:.2f}\n"
    
    with open("expenses_tracker.txt", "a") as file:
        file.write(log_entry)
        
    print("Item and Expenses logged successfully!")
    print("You can view them by selecting option 5 from the main menu.")

def savings_calculator():

    total_cost_of_item = float(input("What is the total cost of the item: "))
    money_saved_up = float(input("How much money do you currently have saved: "))
    money_put_away_weekly = float(input("How much money can you realistically put away each week: "))

    weeks_needed = (total_cost_of_item - money_saved_up) / money_put_away_weekly

    print(f"You need to save up for {weeks_needed:.2f} weeks (including spending your savings) to be able to afford the item in which you want to purchase.")

def view_manage_expenses():
    print("\n---YOUR LOGGED EXPENSES---")

    try:
        with open("expenses_tracker.txt", "r") as file:
            for line in file:
                print(line.strip())
            print("\nThe above is your expenses.")

    except FileNotFoundError:
        print("[ERROR] File not found! Did you forget to add something to your expenses?")
        return

    delete_expenses = str(input("Would you like to delete your expenses? (Y/N)").lower())
    if delete_expenses == "y":
        with open ("expenses_tracker.txt", "w") as file:
            pass

            print("All expenses have been successfully deleted!")

    elif delete_expenses == "n":
        print("You will now be re-routed to the main menu.")

    else:
        print("Your option is not recognised. Please input Y (For Yes) or N (For No) to continue.")



def view_manage_income():
    print("\n---YOUR LOGGED INCOME---")

    try:
        with open("income_tracker.txt", "r") as file:
            for line in file:
                print(line.strip())
            print("\nAbove is your Income.")
    except FileNotFoundError:
        print("\n[ERROR] File not found! Did you forget to add your income?")
        return
    
    change_or_delete_income = input("Would you like to change or delete your income? (Y/N): ").lower()
    if change_or_delete_income == "y":
        userinput_income = input("Change or Delete? (Change/Delete) ").lower()
        if userinput_income == "change": 
            new_income = float(input("Enter your new monthly income: "))

            with open ("income_tracker.txt", "w") as file:
                file.write(f"Income : £{new_income:.2f}")

            print("Income updated successfully!")

        elif userinput_income == "delete":
            with open("income_tracker.txt", "w") as file:
                pass

            print("Income has been deleted successfully!")

    elif change_or_delete_income == "n":
        print("\nNo changes made. Taking you back to the main menu.")
        pass
    else:
        print("\n[ERROR] Choice not recognised. Taking you back to the main menu.")

show_temporary_message()

while True:

    print("\n==============================")
    print("--- WELCOME TO MY BUDGET ENGINE ---")
    print("==============================")
    print("                                     Github: CodeWithOwen20           ")
    print(f"                                 {date_completed}")
    print("1. 30/50/10 Budget Splitter")
    print("2. Log a Daily Expense")
    print("3. Savings Target Calculator")
    print("4. Exit Program")
    print("5. View/Manage Expenses")
    print("6. View/Manage Income")
    print("7. Additional Information")
    print("------------------------------")

    choice = input("Please select a relevant option between 1-7: ")

    if choice == "1":
        budget_calculator()

    elif choice == "2":
        expense_logger()

    elif choice == "3": 
        savings_calculator()

    elif choice == "4":
        print("Thank you for using my Budget Tracker! I hope you enjoyed, bye now. Take care:)")
        break

    elif choice == "5":
        view_manage_expenses()

    elif choice == "6":
        view_manage_income()

    elif choice == "7":
        print("\n========================================================")
        print("This is a simple Budget Tracker created by CodeWithOwen20.")
        print("\nFor the income and expenses to be tracked safely, please ensure you do not already have files that are named the following:")
        print("\nexpenses_tracker.txt or income_tracker.txt, ")
        #Add other files to description
        print("\nIf you have the following files named and do not change or delete them, it may cause those named files to be corrupted")
        print("or add unwanted text to said files. If you already have the files named because of this program, this does not apply to you. ")
        print("========================================================")
    else:
        print("[ERROR] Your selection is unrecognised. Please type a number 1 to 7.")

        #Project 3 complete
import os
import time

def description():
    print("\n=====================================")
    print("             ----DESCRIPTION----")
    print("Hey there! Thank you for using my simple `Word Flagger`. Its nothing special and neither does it actually\n")
    print("look for harmful files (such as those containing malware or viruses), but hey, its fun!\n")
    print("This is basically a template for me to understand `File I/O` and utilising libraries such\n")
    print("as `os` and `time`! Im starting to find it interesting how Python is able to read, write and\n")
    print("manage files directly from a terminal (as silly as that sounds). I hope you enjoy this little\n")
    print("silly script and hopefully learnt something about File i/o :)\n")
    print("Take care!\n")
    print("\n=====================================")
    print("Github: CodeWithOwen20")
    print("\n=====================================")



def security_scanner():
    print("\n=====================================")
    print("---SYSTEM BANNED / FLAGGED WORD SCANNER---")
    print("=====================================")

    user_input = input("Please enter the system log or message to scan: ").lower()

    flagged = False

    try:
        with open("banned_words.txt", "r") as file:
            for line in file:
                banned_word = line.strip().lower()

                if banned_word in user_input:
                    print(f"\n[ALARM!] SECURITY THREAT DETECTED: Found Forbidden term {banned_word}")
                    flagged = True

        if not flagged:
            print("\n[SUCCESS] Scan complete. No security threat or flagged words detected.")

    except FileNotFoundError:
        print("[ERROR] Security database banned_words.txt is missing!")

def remove_banned_words():
    updated_words = []
    print("\n=====================================")
    print("---SYSTEM REMOVAL FUNCTION---")
    print("\n=====================================")

    word_to_remove = input("Please enter the word you wish to REMOVE: ").lower().strip()
    
    updated_words = []
    word_found = False

    try:
        
        with open("banned_words.txt", "r") as file:
            for line in file:
                cleaned_line = line.strip().lower()
                
                # If the line matches the target word, we skip it!
                if cleaned_line == word_to_remove:
                    word_found = True  # We flag that we successfully caught it
                else:
                    # If it's NOT the word to delete, save it to our temporary list
                    updated_words.append(cleaned_line)

        if word_found:
            # Open in "w" mode to instantly vaporize the old file text
            with open("banned_words.txt", "w") as file:
                for word in updated_words:
                    file.write(f"{word}\n") # Pour the clean list back in
            print(f"\n[SUCCESS] `{word_to_remove}` has been permanently erased from the database.")
        else:
            print(f"\n[ERROR] `{word_to_remove}` was not found in the database. Nothing was changed.")

    except FileNotFoundError:
        print("[ERROR] Database `banned_words.txt` not found!")


def add_banned_words():
    
    print("\n=====================================")
    print("---SYSTEM APPEND FUNCTION---")
    print("\n=====================================")

    banned_word = input("Please enter the word you wish to Flag: ").lower()
    already_exists = False
    try:
        with open ("banned_words.txt", "r") as file:
            for line in file:
                word_already_exists = line.strip().lower()

                if word_already_exists == banned_word:
                    print(f"\n[ALARM] {banned_word} already exists in banned_words.txt!")
                    already_exists = True

                    
        if not already_exists:
            with open("banned_words.txt", "a") as file:
                file.write(f"{banned_word}\n")
            print(f"Your banned word: `{banned_word}` has been added successfully!")
    except FileNotFoundError:
        print("[ERROR] File `banned_words.txt` not found!")

def view_banned_words():
    print("\n=====================================")
    print("---VIEW BANNED WORDS LIST---")
    print("=====================================")
    
    try:
            with open ("banned_words.txt", "r") as file:
                for line in file:
                    print(line.strip())
            print("\nSuccessfully printed banned_words.txt!")

    except FileNotFoundError:
        print("[ERROR] File `banned_words.txt` not found!")



#creating/finding file. Need to add to notes w examples
if os.path.exists("banned_words.txt"):
    print("File `banned_words.txt` found!")

else:
    print("Creating `banned_words.txt`, please wait one moment...")
    with open("banned_words.txt", "w") as file:
        pass
    print("[SUCCESS] File `banned_words.txt` created!")




while True:

    print("\n=====================================")
    print("---WELCOME TO STRIDERS/OWENS WORD SCANNER")
    print("                     Github: CodeWithOwen20")
    print("\n=====================================")

    print("             =-= MAIN DASHBOARD =-=")
    print("1. Add a Banned Word")
    print("2. Scan Sentence / Word")
    print("3. View Banned Words")
    print("4. Exit Program")
    print("5. Additional Information")
    print("6. Remove Banned Word/s")




    choice = str(input("Please choose an option from 1 to 6: "))

    if choice == "1":
        prewarn_user = input("Are you sure you wish to add a word? (Y/N) ").lower()
        if prewarn_user == "y":
            pass
            add_banned_words()

        elif prewarn_user == "n":
            print("Taking you back to the main screen..")
            continue

        else:
            print("[ERROR] Option not recognised! Please type Y (for Yes) or N (for No)")

    elif choice == "2":
        security_scanner()

    elif choice == "3":
        print("........=-= PRINTING YOUR BANNED WORDS =-=........")
        view_banned_words()


    elif choice == "4":
        print("Thank you for using my Security Scanner:) Take care!")

        print("Thank you for using my Word Flagger!")
        print("Take care!")
        for seconds in range(3, 0, -1):
            print(f"Exiting program in {seconds} seconds...", end="\r")

            time.sleep(1)

        break

    elif choice == "5":
        description()

    elif choice == "6":
        remove_banned_words()

    else:
        print("[ERROR] Choice not recognised! Please pick an option from 1 to 6")
    
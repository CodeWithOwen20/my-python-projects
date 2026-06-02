import random

userlogin = {
    "GBB1": "Toast1",
    "klr1": "French1",
    "bp1": "Bestpenguin1",
    "Blah1": "Bestone",
    "one": "one"
}

monster_class = ["Diabolical", "Rude", "Frighter", "Screamer", "Disciple", "The Devil", "Viper"]

print("----WELCOME TO THE MONSTER GAME V1.2----")
print("You can use `one` for the username and `one` for the password:)")
while True:
    username = input("Please enter your username: ")

    if username in userlogin:
        print("Successful!")
    else:
        print("Unrecognized username. Please try again")
        continue

    userpass = input("Please enter your password: ")

    if userpass == userlogin[username]:
        print("Password successful! Enjoy the game\n")
        break
    else:
        print("Password not recognized. Please try again")
        continue


def play_game(username):
    monster_health = 100
    monster_max_health = 100
    player_max_health = 100
    player_health = 100
    player_weapon = "Rusty Sword"
    chosen_monster = random.choice(monster_class)

    # MOVED OUTSIDE THE LOOP: Announce the monster exactly once at the start of battle
    print(f"\n[ALERT!] The monster is {chosen_monster}! Ready your sword!")

    while True:
        highest_damage = 20
        lowest_damage = 7

        print(f"\nWhat is your next move, {username}?")
        print("1. Attack")
        print("2. Defend")
        print("3. Drink Potion")
        print("4. Run away")
        print("5. Surrender")

        play_input = int(input("Please choose your option: "))

        # CHANGED TO ELIF: Clean, structured action handling
        if play_input == 1:
            damage = random.randint(lowest_damage, highest_damage)
            monster_health -= damage
            print(f"\nYou attacked the {chosen_monster} using the {player_weapon}! You dealt: {damage} Damage ")

            event_roll = random.randint(1, 30)
            monster_counter_attack = event_roll

            if monster_counter_attack <= 5:
                print(f"The {chosen_monster} has parried one of your attacks!")
                player_health -= monster_counter_attack
                print(f"The monster has dealt {monster_counter_attack} damage to you!")
                print(f"Your health is now {player_health}!")

            print(f"The monsters health is now: {monster_health}! ")

        elif play_input == 2:
            damage = random.randint(lowest_damage, highest_damage)
            player_health -= damage
            print(f"\nThe {chosen_monster} attacks!")
            print(f"You chose to Defend! Your health is now: {player_health}")

        elif play_input == 3:
            event_roll_potion_loss = random.randint(1, 15)
            monster_attack_potion = event_roll_potion_loss
            add_potion_hp = random.randint(1, 7)

            if monster_attack_potion <= 5:
                player_health -= monster_attack_potion
                print(f"\nUnlucky. The {chosen_monster} has attacked you!")
                print(f"Your health is now: {player_health}")
            else:
                print("\nYou've drank a potion!")
                player_health += add_potion_hp
                
                # FIX: Clamp health to max limit ceiling
                if player_health > player_max_health:
                    player_health = player_max_health
                    
                print(f"Your health is now {player_health}!")

        elif play_input == 4:
            print("\nYo - you ran away?...No way man come on, seriously? Dont play this again smh.")
            break

        elif play_input == 5:
            print(f"\nThe monster has captured you!")
            print(f"You are now a prisoner of war for the {chosen_monster}! Say your goodbyes!")
            break

        else:
            print("\nOption not recognized. Select a valid action.")
            continue

        # Check health states at the very end of the turn sequence
        if player_health <= 0:
            print(f"\nYou have been slain by {chosen_monster}")
            print("----YOU LOST THE GAME----")
            print("\nTHANK YOU FOR PLAYING")
            break

        elif monster_health <= 0:
            print(f"\nYou have slain {chosen_monster}!")
            print("----YOU BEAT THE GAME---")
            print("\nTHANK YOU FOR PLAYING")
            break


def mainmenu(username):
    while True:
        print("---MAIN SCREEN---")
        print("1. Play Game")
        print("2. Developed By")
        print("3. Exit")
        mainuserinput = int(input("Please select the relevant option(1-3): "))

        if mainuserinput == 1:
            print("--------------------")
            print("\nSTARTING GAME....")
            print("[WARNING]: ARENA ENTERED\n")
            print("--------------------")
            play_game(username) # FIX: Actually launches the battle sequence!
            break

        elif mainuserinput == 2:
            print("--------------------")
            print("\n---------DEVELOPED BY: STRIDER / OWEN---------")
            print("This is really just an experimental game. Kinda my first project lol. Ill add")
            print("things when i need to:)\n")
            print("--------------------")
            continue

        elif mainuserinput == 3:
            print("Exiting...")
            print(f"Goodbye {username}!")
            exit()
        else:
            print("Option not recognised. select a valid option.")
            continue

# Start the application engine
mainmenu(username)


        
# PROJECT COMPLETE

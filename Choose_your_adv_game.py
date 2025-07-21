#GETTING USER NAME !
name = input("Enter Your Name: ").capitalize()
print(f' Hello {name}, welocome to my game!')
should_we_play = input("Do you want to play? Type( yes or no)")
answer = should_we_play.lower()

#MAIN CONTENT !
if answer == 'yes' or answer == 'y':
    print("Let's Play")
    direction = input("Do you want to go Left or Right ").lower()
    if direction == 'left':
        print("We went Left....")
        print("You are infront of the river!")
        print("Do you wanna swim to cross the river or take the boat. Type ('Swim' or 'Boat)! ")
        river_choice = input().lower()
        if river_choice == 'swim':
            print("You are Swimming....")
            print(f"Hey {name}, you are killed my crocodile in the river, game over, try again!")
        elif river_choice == 'boat':
            print("You are Riding on the boat....")
            print(f"Hey {name} you have reached the other End,quickly")
            print("You founf the gold and you WON!!!")
        else:
            print("Enter Correct Option ")
    elif direction == 'right':
        print(" You chose Right!")
        print(" So, you fell of a cliff, game over, try again!")
    else:
        print("Please Enter LEFT or RIGHT..")

elif answer =='no' or answer =='n':
    print("You are out of the game...") 
else:
    print("Please Enter Yes or No")
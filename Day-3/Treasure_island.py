print("Welcome To Treasure Island\nYour mission is to find the Treasure")
choice=input("Enter choice:")
choice=choice.lower()
choice2=input("Enter choice 2:")
choice=choice2.lower()
color=input("Enter color:")
color=color.lower()
if(choice=="left"):
    if(choice2=="wait"):
        if(color=="yellow"):
            print("You Win")
        elif(color=="blue"):
            print("Game Over")
        elif(color=="red"):
            print("Game Over")
    elif(choice2=="swim"):
        print("Game Over")
elif(choice=="right"):
    print("Game Over")
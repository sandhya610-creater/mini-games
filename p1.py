import random
print('HELLOW ')
print('WELCOME TO THE GAME ZONE !')
while True:
    print("1== number guessing game!")
    print("2==dice rolling game")
    print("3==snack,water,gun")
    print("4==exit")
# number guessing game
    user_choice=input("which game you like to play")
    if user_choice=='1':
        number_to_guess=random.randint(1,100)
        while True:
            guess=int(input("guess the number from the 1 to 100: "))
            if guess<number_to_guess:
                print("to less ")
            elif guess>number_to_guess:
                print("to high")
            else:
                print("congratulation you guess it right")
                print("**************************************")
                break
#dice rolling game
    elif user_choice=='2':     
        while True:
            choice= input("Roll the dice? (y/n):").lower()
            if choice=="y":
                die1=random.randint(1,6)
                die2=random.randint(1,6)
                print(f'({die1},{die2})')
            elif choice=="n":
                print('Thanks for playing!')
                print("*************************************")
                break
            else:
                print('invalid choice!')
# snake water gun
    elif user_choice=='3':
        a=random.randint(1,3)
        d={1:"sanke",2:"gun",3:"water"}
        print("enter 1 if u want to choose snake")
        print("enter 3 if u want to choose water")
        print("enter 2 if u want to choose gun")
        b=int(input("enter your choice:-"))
        if d[a]==d[b]:
            print("its a tie")
            print("computer choose:-",d[a])

        elif d[a]==d[1] and d[b]==d[2]:
            print("you win")
            print("computer choose:-",d[a])

        elif d[a]==d[2] and d[a]==d[1]:
            print("computer wins")
            print("computer choose:-",d[a])

        elif d[a]==d[1] and d[b]==d[3]:
            print("computer wins")   
            print("computer choose:-",d[a])  

        elif d[a]==d[3] and d[b]==d[1]:
            print("you win")
            print("computer choose:-",d[a])

        elif d[a]==d[2] and d[b]==d[3]:
            print("you win")  
            print("computer choose:-",d[a])   

        elif d[a]==d[3] and d[b]==d[2]:
            print("computer wins") 
            print("computer choose:-",d[a])
        print("Thanking for playing")
        print("***************************************")

    elif user_choice=='4':
        print("I HOPE YOU ENJOY THE GAMES")
        print("******************************")
        break

    else:
        print("invalid input")

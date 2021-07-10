import random
# def play():
#     player = input("Choose one either 'Rock' 'Paper','Scissors'")
#     player = player.upper()

#      player1 = random.choice(['Rock','Paper','Scissors'])
#      if player == player1:
#          return "Hello you and player1 have both choosen the same thing {}. Its a tie".format(player1)

#      if winning(player,player1):
#          return "Hello, yu choose {} and player1 has choosen {}. You won!".format(player,player1) 

while True:
    print('Make a choice:')
    user = input()
    user = user.lower()

    print("My choice is", user)

    users = ["Rock","Paper","Scissors"]

    computer_choice = random.user(users)
    print("Computer choice is", computer_choice)
    if user in users:
        if user == computer_choice:
            print("It's a tie")
        if user == "Rock":
            if computer_choice == "Paper":
                print("Ooops you lose, Sorry:(") 
            else:
                print("Wow you won!!:) congratulations")
        if user == "Paper":
            if computer_choice =="Scissors":
                print("Ooops you lost, sorry :(")
            else:
                print("You won!!!:) congratulations")                   
        if user == "Scissors":
            if computer_choice =="Rock":
                print("You lose :( ,Sorry")
            else:
                print("You won yeeeii!! :) ,congratulations")
    else:
        print("Sorry invalid choice, try again :(")   
    print()  
         
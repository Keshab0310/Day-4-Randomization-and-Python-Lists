import random
rock = '''   
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
#Above figures are the representation of rock, paper and scissor and this was imported from  internet to make it look good in game.
images = [rock,paper,scissors] #this list contains the images of rock paper and scissors.
user_choice = int(input ("What do you want to choose? Type 0 for Rock, 1 for Paper and 2 for Scissors: "))
if user_choice>=3  or user_choice<0:  #This line of code is written here  just to make sure the user enters a valid number.
    print("Invalid input and you loose")
else:
    print(images[user_choice]) #prints the image of users choice.
    computer_choice = random.randint(0,2)
    print(images[computer_choice]) # prints the computers randomly generated image.

    if  user_choice == 0 and computer_choice == 2: #When user choose 0 it is rock and  the computer chose scissors so the computer loose.
        print(f"You win")
    elif computer_choice == 0 and  user_choice == 2: #when computer choose 0 it is rock and  when user chooses scissors.
        print("Computer wins")
    elif computer_choice > user_choice: #if the computer has a higher number than the user then it is a win for the computer.
        print("Computer wins")
    elif user_choice > computer_choice: #if the users choice is greater than computers then it means that the user has won so we will display.
        print("You win")
    elif computer_choice == user_choice: #if both players chose the same thing then it's a tie.
        print("It is a tie!")


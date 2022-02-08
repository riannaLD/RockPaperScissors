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
images = [rock, paper, scissors]
choice = int(input("What do you choose? Type 0 for Rock, 1 for paper or 2 for scissors. "))
if choice >= 3 or choice < 0:
    print("You typed an invalid number. You lose!")
else: 
     print(images[choice])

     game = random.randint(0, 2)
     print("Computer Chose: ")
     print(images[game])

     if choice == 0 and game == 0: 
        print("It's a draw.")
     elif choice == 1 and game == 1: 
        print("It's a draw.")
     elif choice == 2 and game == 2: 
        print("It's a draw.")
     elif choice == 0 and game == 1:
        print("You lose!")
     elif choice == 0 and game == 2:
        print("You win!")
     elif choice == 1 and game == 0:
        print("You Win!")   
     elif choice == 1 and game == 2:
        print("You lose!")    
     elif choice == 2 and game == 1:
        print("You Win!") 
     else:
          choice == 2 and game == 0
          print("You lose!")           

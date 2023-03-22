import random

random_users = '''


'''
   

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

#Write your code below this line 👇

options = [rock,paper,scissors]
random_option = round(random.randint(0,2))

# print(random_option)

user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))

if user_input > random_option :
    print(user_input)
    
    print(options[user_input])
    
    print("Computer chose: ")
    
    print(options[random_option])
    
    print("You win! ")
    
else :
    print("Draw")




# Rock wins against scissors 

# scissors win against 
# paper wins against rock




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

scissors ='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
list1=[
    rock,paper,scissors]
import random

print("What do you choose? 0 for Rock,1 for paper or 2 for scissors ")
your_choice=int(input("enter number:"))
computer_choice=random.randint(0,2)
if(your_choice==0):
    print(list1[0])
elif(your_choice==1):
    print(list1[1])
elif(your_choice==2):
    print(list1[2])
    
print("Computer Chose:")
print(list1[computer_choice])



if(your_choice==computer_choice):
    print("tie")
elif((your_choice==0 and computer_choice==2) or (your_choice==2 and computer_choice==1) or (your_choice==1 and computer_choice==0)):
    print("You Wins")
else:
    print("You lose ,Computer Wins")

    
    








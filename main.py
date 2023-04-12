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


import random
human = int(input("What is your choice? Type 0 for Rock, 1 for Paper, 2 for Scissors: "))
if human>2:
  print("You have entered an invalid number")
game = [rock, paper, scissors]
print(game[human])
pc = int(random.randint(0,2))
print(f"Computer chose: \n{game[pc]}")

if pc == human:
  print("Tie")
elif human == 0 and pc == 1:
  print("You loose")
elif human == 0 and pc == 2:
  print("You win")

elif human == 1 and pc == 2:
  print("You loose")
elif human == 1 and pc == 0:
  print("You win")

elif human == 2 and pc == 0:
  print("You loose")
elif human == 2 and pc == 1:
  print("You win")




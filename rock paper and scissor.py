import random
print("Welcome to the rock, paper and scissor game: Type 0 for rock, type 1 for paper and type 2 for scissors \n")
ip=input("Enter your choice:")
rock= ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
paper=("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
scissors=("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
     
cip=random.randint(0,2)
if ip=="0":
    print(rock)
    print("You chose rock")
     
    if cip==0:
        print(rock)
        print("Computer chose rock.\nYou both chose the same")
    elif cip==1:
        print(paper)
        print("Computer chose paper.\nYou lost the game")
    else:
        print(scissors)
        print("Computer chose scissors.\nYou won the game.")   
elif ip=="1":
    print(paper)
    print("You chose paper.")
    if cip==1:
        print(paper)
        print("Computer chose paper.\nYou both chose the same.")
    elif cip==0:
        print(rock)
        print("Computer chose rock.\nYou won the game.")
    else:
        print(scissors)
        print("Computer chose scissors.\nYou lost the game")        
elif ip=="2":
    print(scissors)
    print("You chose scissors.")
    if cip==1:
        print(paper)
        print("Computer chose paper.\nYou won the game.")
    elif cip==0:
        print(rock)
        print("Computer chose rock.\nYou lost the game.")
    else:
        print(scissors)
        print("Computer chose scissors.\nYou both chose the same.")        
else:
    print("Please enter a valid choice.")        
                     

 
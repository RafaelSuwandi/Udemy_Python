# NOTE Section 3 : Day 3 (Beginner)
print("DAY 3")
# in today's lesson you learn about basic if, elif, and else statement
# You also learn nested if and elif statement and 3 basic logical operator (AND,OR,NOT)

print("Welcome to the tressure island!")
print("You're mission is to find the tressure chest hidden in the island!")
choice = input("When you're first arrive you have two diffrent path to cross \"right\" and \"left\" what will you choose?").lower()

if choice == 'left' : 
    print("You fell into a hole! YOU DIED!")

elif choice == 'right' : 
    act = input("You came across a river! what will you do? 'wait' or 'swim' ").lower()
    if act == 'wait' :
        print("Suddenly there's a boat that appeared! you may hop into the boat and choose the 3 path avaiable")
        path = input("There's 'red', 'yellow', and 'blue' path enter your choice! ").lower()
        if path == 'red' : 
            print("Suddenly there's a fire that appeared from the sky that came flying to you! YOU DIED!")
        
        elif path == 'yellow' : 
            print("You arrived at the tressure! you win!")

        elif path == 'blue' : 
            print("There's a horde of mermaid that came to take you soul! YOU DIED!")

        else : 
            print("There's only 3 option to choose!")
    
    elif act == 'swim' : 
        print("There's a crocodile that appeared and you died because you din't analyze the situation patiently!")
    
    else : 
        print("There's only two option! choose between those two!")

else : 
    print("You only have 2 choice 'right' or 'left'!")
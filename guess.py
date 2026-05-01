secret = 10
attempts = 4

while attempts > 0:
    guess = int(input("Guess the number "))
    
    if guess == secret:
        print("you won")
        break # Exit the loop early since they won
        
    attempts -= 1 # Decrease the remaining attempts by 1

if attempts == 0:
    print("you failed try again")

import random  # Import the random module to generate random choices for the computer

def gamewin(comp, you):
    # This function determines the winner based on the choices of the computer and player
    if comp == you:  # If both choices are the same
        return None  # It's a tie
    elif comp == "w":  # If the computer chose Water
        if you == "s":  # If player chose Snake
            return True  # Player wins
        elif you == "g":  # If player chose Gun
            return False  # Player loses
    elif comp == "g":  # If the computer chose Gun
        if you == "w":  # If player chose Water
            return True  # Player wins
        elif you == "s":  # If player chose Snake
            return False  # Player loses
    elif comp == "s":  # If the computer chose Snake
        if you == "g":  # If player chose Gun
            return True  # Player wins
        elif you == "w":  # If player chose Water
            return False  # Player loses

while True:  # Start an infinite loop to keep the game running
    print("comp Turn: Snake(s) Water(w) or Gun(g)?")  # Prompt for computer's turn
    randomNo = random.randint(1, 3)  # Generate a random number between 1 and 3
    if randomNo == 1:
        comp = "s"  # Assign "s" (Snake) if random number is 1
    elif randomNo == 2:
        comp = "w"  # Assign "w" (Water) if random number is 2
    elif randomNo == 3:
        comp = "g"  # Assign "g" (Gun) if random number is 3

    while True:  # Inner loop to keep prompting the user until a valid input is received
        yourTurn = input("Play the game (Snake(s) Water(w) or Gun(g))? (Type 'exit' to stop) ").lower()  # Get player's choice
        
        if yourTurn == 'exit':  # Check if the player wants to exit
            print("Thanks for playing!")  # Thank the player for playing
            exit()  # Exit the game entirely

        try:
            # Input validation
            if yourTurn not in ['s', 'w', 'g']:  # Check if the player's input is valid
                raise ValueError("Invalid input. Please choose 's' for Snake, 'w' for Water, or 'g' for Gun.")  # Raise an error if invalid input
            break  # Break out of the inner loop if the input is valid

        except ValueError as e:  # Catch any ValueError raised in the try block
            print(e)  # Print the error message and continue to ask for valid input

    a = gamewin(comp, yourTurn)  # Determine the game result
    print(f"Comp chose {comp}")  # Print computer's choice
    print(f"You chose {yourTurn}")  # Print player's choice

    # Determine the outcome and print the result
    if a is None:  # If the result is None, it's a tie
        print("The game is tied")
    elif a:  # If the result is True, the player wins
        print("You win")
    else:  # If the result is False, the player loses
        print("You lose")

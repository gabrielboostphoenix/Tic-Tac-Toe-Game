# Declaring the functionality that creates the game graphic
def createGameGraphic(positions_X, positions_O):

    # Checking the players positions
    for position in range(1, 10):

        if position in positions_X:

            # Checking if the position is 3 or 6 or 9
            if position == 3 or position == 6 or position == 9:
                print(" X ")
                print("------------")
            else:
                print(" X |", end="")

        elif position in positions_O:

            # Checking if the position is 3 or 6 or 9
            if position == 3 or position == 6 or position == 9:
                print(" O ")
                print("------------")
            else:
                print(" O |", end="")

        else:

            # Checking if the position is 3 or 6 or 9
            if position == 3 or position == 6 or position == 9:
                print(f" {position} ")
                print("------------")
            else:
                print(f" {position} |", end="")

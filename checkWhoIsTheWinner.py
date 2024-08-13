# Declaring the functionality that checks who's the game winner
def checkWhoIsTheWinner(positions):

    # Checking the positions list length
    if len(positions) > 2:

        # List that contains all the possibilities
        possibilities = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
            [1, 4, 7],
            [2, 5, 8],
            [3, 6, 9],
            [3, 5, 7],
            [1, 5, 9]
        ]

        # Checking if the player has won
        for possibility in possibilities:
            if all(position in positions for position in possibility):

                # In this case, the player has won
                return True

        # In this case, the player hasn't won
        return False

    else:

        # In this case, the player hasn't won
        return False
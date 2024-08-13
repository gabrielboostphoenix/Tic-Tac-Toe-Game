# Importing the necessary functionalities
from showOptionsMenu import showStartOptionsMenu
from choiceTheFirstPlayer import choosingTheFirstPlayer
from collectAndValidateThePlayerPosition import collectAndValidatePlayerPosition
from checkWhoIsTheWinner import checkWhoIsTheWinner
from createGameGraphic import createGameGraphic

# Initializing the positions array of the players and other variables
positions_of_player_X = []
positions_of_player_O = []

# Collecting the start option
showStartOptionsMenu()
startOption = choosingTheFirstPlayer()

# Repeting 9 times until the game is over
for time in range(1, 6):

    message = f"Jogada {time}"
    print(f"{message:^80}")
    print("=" * 80)

    # Checking which player starts first
    if startOption == 1:

        # Showing the game graphic
        createGameGraphic(positions_of_player_X, positions_of_player_O)

        # In this case, the player X starts first
        # Collecting a valid position from the player X
        valid_position = collectAndValidatePlayerPosition(positions_of_player_O)

        # Adding the valid position in the player positions list
        positions_of_player_X.append(valid_position)

        # Showing the game graphic
        createGameGraphic(positions_of_player_X, positions_of_player_O)

        # Checking if the player X has won
        if checkWhoIsTheWinner(positions_of_player_X):

            # Showing a victory message
            print("O jogador X venceu. Parábens!")
            print("=" * 80)
            # Breaking the loop structure
            break

        # Checking the round
        if time == 5:
            # Showing a tie message
            print("O jogo deu empate portanto ninguém ganhou!")
            print("=" * 80)
            # Breaking the loop structure
            break

        # Collecting a valid position from the player O
        valid_position = collectAndValidatePlayerPosition(positions_of_player_X)

        # Adding the valid position in the player positions list
        positions_of_player_O.append(valid_position)

        # Checking if the player O has won
        if checkWhoIsTheWinner(positions_of_player_O):

            # Showing a victory message
            print("O jogador O venceu. Parábens!")
            print("=" * 80)
            # Breaking the loop structure
            break

    else:

        # Showing the game graphic
        createGameGraphic(positions_of_player_X, positions_of_player_O)

        # In this case, the player O starts first
        # Collecting a valid position from the player O
        valid_position = collectAndValidatePlayerPosition(positions_of_player_X)

        # Adding the valid position in the player positions list
        positions_of_player_O.append(valid_position)

        # Showing the game graphic
        createGameGraphic(positions_of_player_X, positions_of_player_O)

        # Checking if the player O has won
        if checkWhoIsTheWinner(positions_of_player_O):

            # Showing a victory message
            print("O jogador O venceu. Parábens!")
            print("=" * 80)
            # Breaking the loop structure
            break

        # Checking the round
        if time == 5:
            # Showing a tie message
            print("O jogo deu empate portanto ninguém ganhou!")
            print("=" * 80)
            # Breaking the loop structure
            break

        # Collecting a valid position from the player X
        valid_position = collectAndValidatePlayerPosition(positions_of_player_O)

        # Adding the valid position in the player positions list
        positions_of_player_X.append(valid_position)

        # Checking if the player X has won
        if checkWhoIsTheWinner(positions_of_player_X):

            # Showing a victory message
            print("O jogador X venceu. Parábens!")
            print("=" * 80)
            # Breaking the loop structure
            break

# Declaring the functionality that collects and validates the received player position
def collectAndValidatePlayerOPosition(positions_of_player_o: list, positions_of_player_x: list):

    # Repeat until the user provides a valid position
    while True:

        # Checking for any typing erros or value erros
        try:

            # Collecting a position from the player
            position = int(input("Informe uma posição de jogo: "))

            # Checking if the received player is valid in the game
            if not(position >= 1 and position <= 9):
                raise ValueError("Posição fornecida inválida devido não existir como opção no jogo!")

            # Checking if the received player position has already been chosen for player X
            for index in range(0, len(positions_of_player_x)):

                if positions_of_player_x[index] == position:
                    raise ValueError("Posição fornecida inválida devido já estar sendo ocupada pelo jogador X!")

            # Checking if the received player position has already been used for yourself
            for index in range(0, len(positions_of_player_o)):

                if positions_of_player_o[index] == position:
                    raise ValueError("Posição fornecida inválida devido já está sendo ocupada por você mesmo!")

            # Breaking the loop structure
            break

        except TypeError:

            print("Detalhes do erro: Informe números inteiros positivos como opção de posição!")
            print("=" * 80)

        except ValueError as error:

            print(f"Detalhes do erro: {error}")
            print("=" * 80)

    # Returning a valid position of the player
    return position

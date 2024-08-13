# Declaring the functionality that collects and validates the received player position
def collectAndValidatePlayerPosition(positions: list):

    # Repeat until the user provides a valid position
    while True:

        # Checking for any typing erros or value erros
        try:

            # Collecting a position from the player
            position = int(input("Informe uma posição de jogo: "))

            # Checking if the received player is valid in the game
            if not(position >= 1 and position <= 9):
                raise ValueError("Posição fornecida inválida devido não existir como opção no jogo!")

            # Checking if the received player position has already been chosen
            for playerPosition in range(0, len(positions)):

                if positions[playerPosition] == position:
                    raise ValueError("Posição fornecida inválida devido já estar sendo ocupada!")

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

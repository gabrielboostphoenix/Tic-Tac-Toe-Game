# Declaring the functionality that collects and validates the start option
def choosingTheFirstPlayer():

    # Repeat until the user provides a valid start option
    while True:

        # Checking for any int typing error or value error
        try:

            # Collecting a start option of user
            startOption = int(input("Informe quem irá começar o jogo primeiro: "))

            # Checking for invalid start option
            if startOption != 1 and startOption != 2:
                raise ValueError("Opção de começo de jogo inválida. Por favor informe opções do menu!")

            # Breaking the loop structure
            break

        except ValueError as error:

            print(f"Detalhes do erro: {error}")
            print("=" * 80)

        except TypeError:

            print("Detalhes do erro: Por favor informe números inteiros positivos como opção de começo!")
            print("=" * 80)

    # Returning the received start option
    return startOption

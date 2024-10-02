list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
empty_list = []
play = True


def print_board(list):
    print(f" {list[0]} | {list[1]} | {list[2]} \n----------- \n"
          f" {list[3]} | {list[4]} | {list[5]} \n----------- \n"
          f" {list[6]} | {list[7]} | {list[8]} ")


# def check_win(player):
def check_win(player):
    row1 = list[0] == player and list[1] == player and list[2] == player
    row2 = list[3] == player and list[4] == player and list[5] == player
    row3 = list[6] == player and list[7] == player and list[8] == player
    col1 = list[0] == player and list[3] == player and list[6] == player
    col2 = list[1] == player and list[4] == player and list[7] == player
    col3 = list[2] == player and list[5] == player and list[8] == player
    diag1 = list[0] == player and list[4] == player and list[8] == player
    diag2 = list[2] == player and list[4] == player and list[6] == player

    return bool(row1 or row2 or row3 or col1 or col2 or col3 or diag1 or diag2)


print("Welcome to Tic Tac Toe!")
print_board(list)

# Asking the user choice

choice = input("What is your choice player1 ? press 1 for 'X' or press 2 for 'O' : ")
player_1 = ''
player_2 = ''

if choice == '1':
    player_1 = 'X'
    player_2 = 'O'
else:
    player_1 = 'O'
    player_2 = 'X'
print(f"Player 1 is '{player_1}' and Player 2 is '{player_2}' \n")

print_board(list)

while play:
    print(f"Now it's player 1's turn(ie, '{player_1}' )")
    # Asking the user choice
    slot_choice = int(input(f"Enter the slot to place '{player_1}' : "))
    empty_list.append(slot_choice)

    # placing the choice in the list by player1

    list[slot_choice - 1] = player_1
    print_board(list)
    print("\n")

    # checking which player won or it's a draw
    if len(empty_list) == 9:
        print("The match is draw! \n")
        print("Thanks for playing the game! \n")
        break
    else:
        if check_win(player_1):
            print(f"Player 1 ie, ('{player_1}') wins the match! \n")
            break
        if check_win(player_2):
            print(f"Player 2 ie, ('{player_2}') wins the match! \n")
            break

    print(f"Now it's player 2's turn(ie,'{player_2}' )")
    # Asking the user choice
    slot_choice = int(input(f"Enter the slot to place '{player_2}' : "))
    empty_list.append(slot_choice)

    # placing the choice in the list by player2

    list[slot_choice - 1] = player_2
    print_board(list)
    print("\n")

print("\n")
print_board(list)
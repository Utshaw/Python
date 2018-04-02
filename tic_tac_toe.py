


board = [' ' for i in range(0, 9, 1)]

print(board)


def winCheck():
    if board[0] == board[1] and board[1] == board[2] and board[0] != ' ':
        return True
    if board[3] == board[4] and board[4] == board[5] and board[3] != ' ':
        return True
    if board[6] == board[7] and board[7] == board[8] and board[6] != ' ':
        return True
    if board[0] == board[3] and board[3] == board[6] and board[0] != ' ':
        return True
    if board[1] == board[4] and board[4] == board[7] and board[1] != ' ':
        return True
    if board[2] == board[5] and board[5] == board[8] and board[2] != ' ':
        return True
    if board[0] == board[4] and board[4] == board[8] and board[0] != ' ':
        return  True
    if board[2] == board[4] and board[4] == board[6] and board[2] != ' ':
        return  True
    return False



def print_board():
    row_1 = "|{}|{}|{}|".format(board[0], board[1], board[2])
    row_2 = "|{}|{}|{}|".format(board[3], board[4], board[5])
    row_3 = "|{}|{}|{}|".format(board[6], board[7], board[8])

    print()
    print(row_1)
    print(row_2)
    print(row_3)
    print()





print_board()

def print_board_wth_numbers():
    row_1 = "|0|1|2|"
    row_2 = "|3|4|5|"
    row_3 = "|6|7|8|"



    print()
    print(row_1)
    print(row_2)
    print(row_3)
    print()


print_board_wth_numbers()

player_1_move = True

while True:
    if player_1_move:
        player_1 = int(input('Player 1, Enter position: ').strip())
        if board[player_1] != ' ':
            print('Player 1 Invalid Position')
            continue
        board[player_1] = 'X'
        print_board()
        if winCheck():
            print('Player 1 Wins!!!')
            break
        player_1_move = False
    else:
        player_2 = int(input('Player 2, Enter position: ').strip())
        if board[player_2] != ' ':
            print('Player 2 Invalid Position')
            continue
        board[player_2] = 'O'
        print_board()
        if winCheck():
            print('Player 2 Wins!!!')
            break
        player_1_move = True











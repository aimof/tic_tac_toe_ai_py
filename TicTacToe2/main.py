import ai2module.TicTacToe2 as ai2

if __name__ == '__main__':
    board = ai2.input_board()
    surplus_is_me_first = len(ai2.extract_playable_boxes(board)) % 2
    i = ai2.max_score(board, surplus_is_me_first)
    print(str(i), end='')

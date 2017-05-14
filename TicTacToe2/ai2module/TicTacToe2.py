import json


lines = [
    [0, 1, 2],
    [3, 4, 5],
    [5, 6, 7],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]


def input_board():
    s = input()
    return json.loads(s)


# first: 1, second: 0
def is_me_first(initial_board):
    playable_boxes = extract_playable_boxes(initial_board)
    return len(playable_boxes) % 2


def max_score(board, surplus_is_me_first):
    if must_win(board) != -1:
        return must_win(board)
    else:
        scores = score(board, surplus_is_me_first)
        t = (-1, -1000)
        for box_score in scores:
            if box_score[1] > t[1]:
                t = box_score
        return t[0]


def must_win(board):
    for line in lines:
        line_sum = board[line[0]] + board[line[1]] + board[line[2]]
        if line_sum == 2:
            for box in line:
                if board[box] == 0:
                    return box
    return -1


def score(board, surplus_is_me_first):
    playable_boxes = extract_playable_boxes(board)
    scores = []
    for box in playable_boxes:
        box_score = 0
        is_my_turn = len(playable_boxes) % 2 == surplus_is_me_first
        next_board = make_next_board(board, box, is_my_turn)
        value, is_finished = check_win(next_board)
        box_score += -100
        if is_finished:
            box_score += value
        else:
            box_score += next_score(next_board, surplus_is_me_first)
        scores.append((box, box_score))
    return scores


def next_score(board, surplus_is_me_first):
    playable_boxes = extract_playable_boxes(board)
    if len(playable_boxes) == 0:
        value, _ = check_win(board)
        return value
    else:
        box_score = 0
        for box in playable_boxes:
            next_board = make_next_board(board, box, len(playable_boxes) % 2 == surplus_is_me_first)
            value, is_finished = check_win(next_board)
            box_score += value
            if not is_finished:
                box_score += next_score(next_board, surplus_is_me_first)
        return box_score


def make_next_board(board, box, is_my_turn):
    if is_my_turn:
        board[box] = 1
    else:
        board[box] = -1
    return board


def check_win(board):
    for line in lines:
        line_sum = board[line[0]] + board[line[1]] + board[line[2]]
        if line_sum == -3:
            return -10, True
        elif line_sum == 3:
            return 1, True
    if len(extract_playable_boxes(board)) == 0:
        return 0, True
    return 0, False


def extract_playable_boxes(board):
    playable_boxes = []
    for i, v in enumerate(board):
        if v == 0:
            playable_boxes.append(i)
    return playable_boxes

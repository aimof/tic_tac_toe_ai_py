import json
import itertools


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


def extract_playable_boxes(board):
    playable_boxes = []
    for i, v in enumerate(board):
        if v == 0:
            playable_boxes.append(i)
    return playable_boxes


def evaluate_lines(board):
    value_lines = []
    for i, line in enumerate(lines):
        line_sum = board[line[0]] + board[line[1]] + board[line[2]]
        value_lines.append((i, line, line_sum))
    return value_lines


def make_next_board(board, box, is_my_turn):
    if is_my_turn:
        board[box] = 1
    else:
        board[box] = -1
    return board


def play(board):
    playable_boxes = extract_playable_boxes(board)
    all_list = list(itertools.permutations(playable_boxes))
    for l in all_list:
        b = board[:]
        for i, box in enumerate(l):
            b = make_next_board(b, box, (len(playable_boxes) - i) % 2 == 1)
            value = evaluate_lines(board)
            if value[2] == -3:
                for m in all_list:
                    is_same = True
                    if m[0:i] == l[0:i]:
                        is_same = False
                    if is_same:
                        all_list.remove(m)
    return all_list[0][0]



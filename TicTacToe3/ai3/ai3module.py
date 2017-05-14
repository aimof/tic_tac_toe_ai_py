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


def evaluate_lines(board):
    value_lines = []
    for i, line in enumerate(lines):
        line_sum = board[line[0]] + board[line[1]] + board[line[2]]
        value_lines.append((i, line, line_sum))
    return value_lines


def play(board):
    playable_boxes = extract_playable_boxes(board)
    if len(playable_boxes) == 9:
        return 4
    value_lines = evaluate_lines(board)
    minus_lines = []
    for value in value_lines:
        if value[2] == 2:
            return find_blank_box_in_line(board, value[1])
        elif value[2] == -2:
            return find_blank_box_in_line(board, value[1])
        elif value[2] == -1:
            minus_lines.append(value)
    if board[4] == 0:
        return 4
    if len(minus_lines) != 0:
        for value in minus_lines:
            if value[0] % 2 == 0:
                box1 = find_blank_box_in_line(board, value[1])
                if box1 != -1:
                    return box1
    if len(minus_lines) != 0:
        for value in minus_lines:
            box2 = find_blank_box_in_line(board, value[1])
            if box2 != -1:
                return box2
    for box3 in playable_boxes:
        if box3 % 2 == 0:
            return box3
    return playable_boxes[0]


def find_blank_box_in_line(board, line):
    for box in line:
        if board[box] == 0:
            return box
    return -1


def extract_playable_boxes(board):
    playable_boxes = []
    for i, v in enumerate(board):
        if v == 0:
            playable_boxes.append(i)
    return playable_boxes

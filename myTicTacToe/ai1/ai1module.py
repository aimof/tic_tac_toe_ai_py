import json


def def_lines():
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
    return lines


def input_board():
    s = input()
    b = json.loads(s)
    return b


def extract_legal_boxes(b):
    legal_boxes = []
    for i, mark in enumerate(b):
        if mark == 0:
            legal_boxes.append(i)
    return legal_boxes


def find_blank_box(b, line):
    for i in range(3):
        if b[line[i]] == 0:
            return line[i]


def search_candidate(b, is_my_turn, lines):
    if is_my_turn:
        return search_my_playable_boxes(b, lines)
    else:
        return search_opponents_playable_boxes(b, lines)


def is_check(b, lines):
    my_check = []
    opponents_check = []
    for line in lines:
        play_sum = b[line[0]] + b[line[1]] + b[line[2]]
        if play_sum == 2:
            my_check.append(line)
        if play_sum == -2:
            opponents_check.append(line)
    return my_check, opponents_check


def search_check(b, lines):
    my_checks = []
    opponents_checks = []
    for _ in range(9):
        tmp = is_check(b, lines)
        my_check = tmp[0]
        opponents_check = tmp[1]
        my_checks.append(my_check)
        opponents_checks.append(opponents_check)
    return my_checks, opponents_checks


# return play: [int] or lost: [-2]
def search_my_playable_boxes(b, lines):
    my_checks, opponents_checks = search_check(b, lines)
    if len(my_checks) != 0:
        return [find_blank_box(b, my_checks[0])]
    elif len(opponents_checks) > 1:
        return [-2]
    elif opponents_checks == 1:
        return [find_blank_box(b, opponents_checks[0])]
    else:
        return extract_legal_boxes(b)


# return play[int], won: [-1] or lost: [-2]
def search_opponents_playable_boxes(b, lines):
    my_checks, opponents_checks = search_check(b, lines)
    if len(my_checks) > 1:
        return [-1]
    elif len(opponents_checks) != 0:
        return [-2]
    else:
        return extract_legal_boxes(b)


# return won: -1, lost: -2, draw: -3, not finished: 0
def recursion(b, lines, is_my_turn):
    playable_boxes = []
    if is_my_turn:
        playable_boxes = search_my_playable_boxes(b, lines)
    else:
        playable_boxes = search_opponents_playable_boxes(b, lines)
    if len(playable_boxes) == 0:
        return playable_boxes
    elif playable_boxes == [-2] or playable_boxes == [-3]:
        return playable_boxes
    else:
        isWon = []
        for box in playable_boxes:
            b1 = b[:]
            if is_my_turn:
               b1[box] = 1
            else:
                b1[box] = -1
            ary = recursion(b1, lines, not is_my_turn)
            if ary == [-2]:
                return ary


# play関数を書き換えることで、AIを, lines作成しよう！　デフォルトでは合法手の中からランダムでプレイを選択します
def play(b, lines):
    legal_boxes = extract_legal_boxes(b)
    if len(legal_boxes) == 0:
        return -1
    playable_boxes = legal_boxes[:]
    for playable_box in playable_boxes:
        state = recursion(b, playable_box, lines)
        if state[0] == -1:
            return playable_box
        elif state[0] == -2:
            playable_boxes.remove(playable_box)
    return playable_boxes[0]

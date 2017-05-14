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


def play(board):
    playable_boxes = extract_playable_boxes(board)
    all = list(itertools.permutations(playable_boxes))
    
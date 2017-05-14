# -*-encoding utf-8-*-
import json


class TicTacToe:

    def __init__(self):
        self.lines = [
            [0, 1, 2],
            [3, 4, 5],
            [5, 6, 7],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6]
        ]
        self.board = self.input_board()

    @staticmethod
    def input_board():
        s = input()
        b = json.loads(s)
        return b

    @staticmethod
    def extract_legal_boxes(board):
        legal_boxes = []
        for i in range(9):
            if board[i] == 0:
                legal_boxes.append(i)
        return legal_boxes

    @staticmethod
    def is_check(self, board):
        my_check = []
        opponents_check = []
        for line in self.lines:
            play_sum = board[line[0]] + board[line[1]] + board[line[2]]
            if play_sum == 2:
                my_check.append(line)
            if play_sum == -2:
                opponents_check.append(line)
        return my_check, opponents_check

    @staticmethod
    def search_my_play(self, board):
        legal_boxes = self.extract_legal_boxes(board)
        my_checks = []
        opponents_checks = []
        for _ in self.lines:
            my_check, opponents_check = self.is_check(board)
            my_checks.append(my_check)
            opponents_checks.append(opponents_check)

        for box in legal_boxes:

    @staticmethod
    def find_blank_box(b, line):
        for i in range(3):
            if b[line[i]] == 0:
                return line[i]


    # play関数を書き換えることで、AIを作成しよう！　デフォルトでは合法手の中からランダムでプレイを選択します




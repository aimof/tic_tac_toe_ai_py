# -*-encoding=utf-8-*-
import ai1

if __name__ == '__main__':
    lines = ai1.ai1module.def_lines()
    b = ai1.ai1module.input_board()
    print(str(ai1.ai1module.play(b, lines)), end='')
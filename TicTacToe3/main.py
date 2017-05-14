import ai3.ai3module as ai3module

if __name__ == '__main__':
    b = ai3module.input_board()
    print(str(ai3module.play(b)), end='')

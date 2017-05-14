import ai4.ai4module as ai4module

if __name__ == '__main__':
    b = ai4module.input_board()
    print(str(ai4module.play(b)), end='')

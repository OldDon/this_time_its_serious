def play():
    play_again = input('Do you want to play again? ((y)es or (n)o ?')
    if play_again == 'n':
        print('OK. Hope you had a good time. Thank and bye bye :)')
        sys.exit
    else:
        random_game()
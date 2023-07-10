import random


def guess_game():
    """
        this code develops a guessing game which will let the user guess a random number between 1 and 100.
        is user will only have 5 chances given, if the chances run out, its game over. when the user guess a wrong number its going to ask them to guess higher or lower
    """

    computer_guess = random.randrange(1, 100)
    chances = 5

    def game(chances):
        guess = input('take a guess: ')
        if chances > 1:
            try:
                guess = int(guess)
                if guess == computer_guess:
                    return (print('you win') and print(f'comp number: {computer_guess}'))
                elif guess > computer_guess:
                    chances -= 1
                    print('guess lower')
                    print(f'you have {chances} chances remaining')
                    return game(chances)
                else:
                    chances -= 1
                    print('guess higher')
                    print(f'you have {chances} chances remaining')
                    return game(chances)

            except:
                ValueError
                chances -= 1
                print('guess a number')
                print(f'you have {chances} chances remaining')
                return game(chances)
        else:
            return print('you are out of chances game over')

    print('** welcome to CLI guessing game **')
    print('you are given 5 chances to guess the number am thinking about')
    print('please know that the number is between 1 and 100')

    start_game = input('start? Y/N: ')

    if (start_game == 'y' or start_game == 'Y'):
        game(chances)
    elif (start_game == 'n' or start_game == 'N'):
        return print('thanks for play the game')
    else:
        print('stop waffling')


guess_game()

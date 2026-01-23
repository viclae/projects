from colorama import init, Style
init(autoreset = True)

def main():
    while True:
        print('\n' + Style.BRIGHT + 'This is a game of Rock Paper Scissors!')

        options = ['ROCK', 'PAPER', 'SCISSORS']

        while True:
            first_player = str(input('\nPlayer 1 ' + Style.BRIGHT + '(ROCK/PAPER/SCISSORS): ')).strip().upper()
            if first_player in options:
                break

        while True:
            second_player = str(input('\nPlayer 2 ' + Style.BRIGHT + '(ROCK/PAPER/SCISSORS): ')).strip().upper()
            if second_player in options:
                break

        print(f'\nPlayer 1 chose ' + Style.BRIGHT + f'{first_player}.')
        print(f'Player 2 chose ' + Style.BRIGHT + f'{second_player}.')

        p1_win = '\nPlayer 1 is the winner!'
        p2_win = '\nPlayer 2 is the winner!'

        if first_player == 'ROCK' and second_player == 'SCISSORS':
            print(Style.BRIGHT + p1_win)
        elif second_player == 'ROCK' and first_player == 'SCISSORS':
            print(Style.BRIGHT + p2_win)
        elif first_player == 'SCISSORS' and second_player == 'PAPER':
            print(Style.BRIGHT + p1_win)
        elif second_player == 'SCISSORS' and first_player == 'PAPER':
            print(Style.BRIGHT + p2_win)
        elif first_player == 'PAPER' and second_player == 'ROCK':
            print(Style.BRIGHT + p1_win)
        elif second_player == 'PAPER' and first_player == 'ROCK':
            print(Style.BRIGHT + p2_win)
        elif first_player == second_player:
            print(Style.BRIGHT + "\nIt's a tie!")

        play_again = str(input('\nWould you like to play again ' + Style.BRIGHT + '(y/n)' + Style.NORMAL + '? ')).strip().lower()
        if play_again != 'y':
            print(f'Goodbye!')
            break

if __name__ == '__main__':
    main()

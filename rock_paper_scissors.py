from colorama import init, Style
init(autoreset = True)

while True:
    print('\nThis is a game of Rock Paper Scissors!')
    play_or_not = str(input('\nWould you like to have a go ' + Style.BRIGHT + '(yes/no)' + Style.NORMAL + '? ')).strip().lower()
    if play_or_not != 'yes':
        break

    while True:
        first_player = str(input('\nPlayer 1 (ROCK/PAPER/SCISSORS): ')).strip().upper()
        if first_player in ['ROCK', 'PAPER', 'SCISSORS']:
            break
        print(f"You can't choose {first_player}!")

    while True:
        second_player = str(input('\nPlayer 2 (ROCK/PAPER/SCISSORS): ')).strip().upper()
        if second_player in ['ROCK', 'PAPER', 'SCISSORS']:
            break
        print(f"You can't choose {second_player}!")

    print(f'\nPlayer 1 chose ' + Style.BRIGHT + f'{first_player}.')
    print(f'Player 2 chose ' + Style.BRIGHT + f'{second_player}.')

    if first_player == 'ROCK' and second_player == 'SCISSORS':
        print(Style.BRIGHT + '\nPlayer 1 is the winner!')
    elif second_player == 'ROCK' and first_player == 'SCISSORS':
        print(Style.BRIGHT + '\nPlayer 2 is the winner!')
    elif first_player == 'SCISSORS' and second_player == 'PAPER':
        print(Style.BRIGHT + '\nPlayer 1 is the winner!')
    elif second_player == 'SCISSORS' and first_player == 'PAPER':
        print(Style.BRIGHT + '\nPlayer 2 is the winner!')
    elif first_player == 'PAPER' and second_player == 'ROCK':
        print(Style.BRIGHT + '\nPlayer 1 is the winner!')
    elif second_player == 'PAPER' and first_player == 'ROCK':
        print(Style.BRIGHT + '\nPlayer 2 is the winner!')

    play_again = str(input('\nWould you like to play again ' + Style.BRIGHT + '(yes/no)' + Style.NORMAL + '? ')).strip().lower()
    if play_again != 'yes':
        break
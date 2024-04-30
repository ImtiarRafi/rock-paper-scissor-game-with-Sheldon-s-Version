import random

def play():
    computer_strike = random.choice(['r','p','s','l','sp'])
    player_strike = input('\n r for Rock \n p for Paper \n s for Scissor\n l for Lizard \n sp for Spock\nWhat\'s Your Strike ?\n')

    print(computer_strike)


    if computer_strike == player_strike:
        return print('It is a tie. Play Again')

    if win(player_strike,computer_strike):
        return print('Player Wins')

    return print('Computer Wins')


def win(you,cpu):
    if (you == 'r' and cpu == 's') or (you == 's' and cpu == 'p') or (you == 'p' and cpu == 'r') \
            or (you == 'r' and cpu == 'l') or (you == 'l' and cpu == 'sp') or (you == 'sp' and cpu == 's') \
            or (you == 's' and cpu == 'l') or (you == 'l' and cpu == 'p') or (you == 'p' and cpu == 'sp') \
            or (you == 'sp' and cpu == 'r'):
        return True


print('-----------Welcome To The Rock Paper Scissor Game--------')
play()
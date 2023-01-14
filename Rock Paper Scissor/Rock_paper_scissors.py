import random

def play():
    you = input("What's your Choice? 'r' for rock, 'p' for paper, 's' for scissors \n")
    if you == 'r':
        user = 'rock'
    elif you == 's':
        user = 'scisor'
    else:
        user = 'paper'
    computer = random.choice(['rock','paper','scisor'])
    print(f'I chose {computer}')
    
    if user == computer:
        return "It's a Tie!"
    
    # r > s, s > p, p > r
    if is_win(user, computer):
        return 'You Won!'
    
    #if is_win(computer, user):
    return 'You Lost!'
    
def is_win(player, opponent):
    # return true if the player wins
    
    if (player ==  'rock' and opponent == 'scisor') or (player == 'scisor' and opponent == 'paper') \
        or (player == 'paper' and opponent == 'rock'):
        return True
    
print(play())
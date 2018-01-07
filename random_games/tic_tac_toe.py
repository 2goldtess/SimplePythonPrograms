"""
Python version of the classic tic tac toe game 
"""
class TicTacToe():

    ttt_board = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
                 'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
                 'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

    turn_options = ['X', 'O']

    move_options = ['top-L', 'top-M', 'top-R',
                    'mid-L', 'mid-M', 'mid-R',
                    'low-L', 'low-M', 'low-R']

    """Prints the current state of the board"""
    def print_board(self):
        print(' '.ljust(10), self.ttt_board['top-L'].center(3), '|'.center(3), self.ttt_board['top-M'].center(3), '|'.center(3), self.ttt_board['top-R'].center(3))
        print(' '.ljust(10),'_____|_______|______')
        print(' '.ljust(10),'     |       |')
        print(' '.ljust(10), self.ttt_board['mid-L'].center(3), '|'.center(3), self.ttt_board['mid-M'].center(3), '|'.center(3), self.ttt_board['mid-R'].center(3))
        print(' '.ljust(10),'_____|_______|______')
        print(' '.ljust(10),'     |       |')
        print(' '.ljust(10), self.ttt_board['low-L'].center(3), '|'.center(3), self.ttt_board['low-M'].center(3), '|'.center(3), self.ttt_board['low-R'].center(3))

    """Prints the configuration of the board"""
    def print_board_config(self):
        print(' '.ljust(10), self.move_options[0].center(3), '|'.center(3), self.move_options[1].center(3), '|'.center(3), self.move_options[2].center(3))
        print(' '.ljust(10),'_______|_________|_______')
        print(' '.ljust(10),'       |         |')
        print(' '.ljust(10),self.move_options[3].center(3), '|'.center(3), self.move_options[4].center(3), '|'.center(3), self.move_options[5].center(3))
        print(' '.ljust(10),'_______|_________|_______')
        print(' '.ljust(10),'       |         |')
        print(' '.ljust(10),self.move_options[6].center(3), '|'.center(3), self.move_options[7].center(3), '|'.center(3), self.move_options[8].center(3))

    """Returns a winner if any, None if otherwise"""
    def winner(self):
        # horizontal winning combinations for 'O'
        if self.ttt_board['top-L'] == 'O' and self.ttt_board['top-M'] == 'O' and self.ttt_board['top-R'] == 'O': return 'O'
        if self.ttt_board['mid-L'] == 'O' and self.ttt_board['mid-M'] == 'O' and self.ttt_board['mid-R'] == 'O': return 'O'
        if self.ttt_board['low-L'] == 'O' and self.ttt_board['low-M'] == 'O' and self.ttt_board['low-R'] == 'O': return 'O'

        # vertical winning combinations for 'O'
        if self.ttt_board['top-L'] == 'O' and self.ttt_board['mid-L'] == 'O' and self.ttt_board['low-L'] == 'O': return 'O'
        if self.ttt_board['top-M'] == 'O' and self.ttt_board['mid-M'] == 'O' and self.ttt_board['low-M'] == 'O': return 'O'
        if self.ttt_board['top-R'] == 'O' and self.ttt_board['mid-R'] == 'O' and self.ttt_board['low-R'] == 'O': return 'O'

        # diagonal winning combinations for 'O'
        if self.ttt_board['top-L'] == 'O' and self.ttt_board['mid-M'] == 'O' and self.ttt_board['low-R'] == 'O': return 'O'
        if self.ttt_board['top-R'] == 'O' and self.ttt_board['mid-M'] == 'O' and self.ttt_board['low-L'] == 'O': return 'O'

        # horizontal winning combinations for 'X'
        if self.ttt_board['top-L'] == 'X' and self.ttt_board['top-M'] == 'X' and self.ttt_board['top-R'] == 'X': return 'X'
        if self.ttt_board['mid-L'] == 'X' and self.ttt_board['mid-M'] == 'X' and self.ttt_board['mid-R'] == 'X': return 'X'
        if self.ttt_board['low-L'] == 'X' and self.ttt_board['low-M'] == 'X' and self.ttt_board['low-R'] == 'X': return 'X'

        # vertical winning combinations for 'X'
        if self.ttt_board['top-L'] == 'X' and self.ttt_board['mid-L'] == 'X' and self.ttt_board['low-L'] == 'X': return 'X'
        if self.ttt_board['top-M'] == 'X' and self.ttt_board['mid-M'] == 'X' and self.ttt_board['low-M'] == 'X': return 'X'
        if self.ttt_board['top-R'] == 'X' and self.ttt_board['mid-R'] == 'X' and self.ttt_board['low-R'] == 'X': return 'X'

        # diagonal winning combinations for 'X'
        if self.ttt_board['top-L'] == 'X' and self.ttt_board['mid-M'] == 'X' and self.ttt_board['low-R'] == 'X': return 'X'
        if self.ttt_board['top-R'] == 'X' and self.ttt_board['mid-M'] == 'X' and self.ttt_board['low-L'] == 'X': return 'X'

        return None

    """Returns turn options"""
    def get_turn_options(self):
        return self.turn_options

    """Returns  move options"""
    def get_move_options(self):
        return self.move_options


"""This is the main/driver for the program"""
def main():
    print('\n\n')
    ttt_game = TicTacToe()
    print('========= Welcome to Tic-Tac-Toe with Friends =========\n\n')

    print('                ~ Board Config ~ \n\n')
    ttt_game.print_board_config()
    print('\n\n')


    print('Who would you like to go first?   ')
    turn = ''


    while turn not in ttt_game.get_turn_options():
        try:
            turn = input('Please enter X or O:   ')[0].upper()
        except:
            continue

    print('\n')
    ttt_game.print_board()
    print('\n\n')


    for i in range(9):
        move = input('Turn for {}, which space would you like to move to?   '.format(turn))

        while move not in ttt_game.get_move_options() or ttt_game.ttt_board[move] != ' ' or move == '':

            if move in ttt_game.get_move_options() and ttt_game.ttt_board[move] != ' ':
                move = input('That space is already taken, try again:   ')
                continue

            move = input('Please enter a valid move corresponding to the board config:   ')

        ttt_game.ttt_board[move] = turn

        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

        print('\n')
        ttt_game.print_board()
        print('\n\n')

        # if more than 2 moves were recorded start checking for a winner
        if(i > 2):
            winner = ttt_game.winner()

            if winner:
                print('Player {} won!'.format(winner))
                print('Game over ...')
                exit(0)

    print('Draw!')
    print('Game over ...')


if __name__ == '__main__':
    main()











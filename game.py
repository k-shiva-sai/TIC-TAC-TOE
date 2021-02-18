import math
import random
import time
from player import HumanPlayer,Computer,SuperComputer
import pyttsx3 as p
class Tic_Tac_Toe:
    def __init__(self):
        self.board=[' ' for _ in range(9)]
        self.current_winner=None
    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| '+' | '.join(row)+' |')
    def print_number_board(self):
        number_board=[[str(i) for i in range(j*3,(j+1)*3)]for j in range(3)]
        for row in number_board:
            print('| '+' | '.join(row)+' |')
    def available_moves(self):
        return [i for i, x in enumerate(self.board) if x == " "]
    def make_move(self,square,letter):
        if self.board[square]==' ':
            self.board[square]=letter
            if self.winner(square,letter):
                self.current_winner=letter
            return True
        return False
    def winner(self,square,letter):
        row_indx=math.floor(square/3)
        r=self.board[row_indx*3:(row_indx+1)*3]
        if all([spot==letter for spot in r]):
            return True
        col_indx=square%3
        c=[self.board[col_indx+i*3] for i in range(3)]
        if all([spot==letter for spot in c]):
            return True
        if square%2==0:
            d1=[self.board[i] for i in [0,4,8]]
            if all([spot==letter for spot in d1]):
                return True
            d2=[self.board[i] for i in [2,4,6]]
            if all([spot==letter for spot in d2]):
                return True
        return False
    def empty_squares(self):
        return ' ' in self.board
    def num_empty_squares(self):
        return self.board.count(' ')
def play(game,x_player,o_player,print_game=True):
    if print_game:
        game.print_number_board()
    letter='X'
    while game.empty_squares():
        if letter=='O':
            square=o_player.get_move(game)
        else:
            square=x_player.get_move(game)
        if game.make_move(square,letter):
            if print_game:
                print(letter+' makes a move to {}'.format(square))
                game.print_board()
                print()
            if game.current_winner:
                if print_game:
                    print(letter+' wins!')
                return letter                
            if letter=='X':
                letter='O'
            else:
                letter='X'
        time.sleep(.8)
    if print_game:
        print("It's a Tie")
        p.speak("It's a Tie")
if __name__=='__main__':
    p.speak("hello welcome to TicTacToe by Shiva Sai")
    print("type 1 to play with computer(probability of wining is more)")
    print("type 2 to play with supercomputer(probability of wining is less)")
    print("type 3 for multiplayer")
    p.speak("choose the oponent")
    typ=input("choose the oponent")
    if int(typ)==1:
        p.speak("YOu have chosen to play with computer")
        x_player=HumanPlayer('X')
        o_player=Computer('O')
    elif int(typ)==2:
        p.speak("YOu have chosen to play with supercomputer")
        x_player=HumanPlayer('X')
        o_player=SuperComputer('O')
    elif int(typ)==3:
        p.speak("You have chosen multiplayer")
        x_player=HumanPlayer('X')
        o_player=HumanPlayer('O')
    game=Tic_Tac_Toe()
    play(game,x_player,o_player,True)
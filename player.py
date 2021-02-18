import math
import random
class Player:
    def __init__(self,letter):
        self.letter=letter
    def get_move(self,game):
        pass
class Computer(Player):
    def __init__(self,letter):
        super().__init__(letter)
    def get_move(self,game):
        square=random.choice(game.available_moves())
        return square
class HumanPlayer(Player):
    def __init__(self,letter):
        super().__init__(letter)
    def get_move(self,game):
        valid_square=False
        val=None
        while not valid_square:
            square=input(self.letter+'\'s turn. Input move(0-8) :')
            try:
                val=int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square=True
            except ValueError:
                print("Invalid Enter again")
        return val
class SuperComputer(Player):
    def __init__(self,letter):
        super().__init__(letter)
    def get_move(self,game):
        if len(game.available_moves())==9:
            square= random.choice(game.available_moves())
        else:
            square=self.minimax(game,self.letter)['pos']
        return square
    def minimax(self,state,player):
        max_player=self.letter
        other_player='O' if self.letter=='X' else 'X'
        if state.current_winner==other_player:
            return {'pos' : None,
                    'score': 1*(state.num_empty_squares()+1) if other_player==max_player else -1*(state.num_empty_squares()+1)}
        elif state.num_empty_squares()==0:
            return {'pos':None,'score':0}
        if player==max_player:
            best={'pos':None ,'score':-math.inf}
        else:
            best={'pos':None,'score':math.inf}
        for pos_mov in state.available_moves():
            state.make_move(pos_mov,player)
            sim_score=self.minimax(state,other_player)
            state.board[pos_mov]=' '
            state.current_winner=None
            sim_score['pos']=pos_mov
            if player==max_player:
                if best['score']<sim_score['score']:
                    best=sim_score
            else:
                if best['score']>sim_score['score']:
                    best=sim_score
        return best
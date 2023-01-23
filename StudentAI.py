from random import randint
from BoardClasses import Move
from BoardClasses import Board
from collections import defaultdict
#The following part should be completed by students.
#Students can modify anything except the class name and exisiting functions and varibles.

class Node():
    def __init__(self, color: int, move: Move =None):
        self.color: int = color
        self.move: Move = move
        self.priorityScore: int = 0
        self.children: [Node] = []




# def color(color):
#     return


class StudentAI():

    def __init__(self,col,row,p):
        self.col = col
        self.row = row
        self.p = p
        self.board = Board(col,row,p)
        self.board.initialize_game()
        self.color = ''
        self.opponent = {1:2,2:1}
        self.color = 2



    def get_move(self,move):
        """
        receiving the opponent move and producing the move.
        just one simple move
        """
        if len(move) != 0:
            self.board.make_move(move,self.opponent[self.color])
        else:
            self.color = 1

        # produce a random move
        """
        moves = self.board.get_all_possible_moves(self.color)
        index = randint(0,len(moves)-1)
        inner_index =  randint(0,len(moves[index])-1)
        move = moves[index][inner_index]
        self.board.make_move(move,self.color)
        """
        #moves = self.board.get_all_possible_moves(self.color) # list of Move objects
        move = self.minmaxSearch()
        self.board.make_move(move,self.color)
        return move


    # evaluate the state in my position
    def evaluate_score(self, myTurn: bool = True):
        point = 0
        for i in range(self.row):
            for j in range(self.col):
                checker = self.board.board[i][j]
                if checker.color == 'W':
                    point -= 1
                    if checker.is_king:
                        point -= 1
                elif checker.color == 'B':
                    point += 1
                    if checker.is_king:
                        point += 1


        if myTurn:
            return point
        else:
            return -point


    # create the search tree for minmax
    # def create_tree(self, root, depth=1):
    #     if depth == 0:
    #         return root
    #     else:
    #         move_available = self.board.get_all_possible_moves(self.opponent(self.color))
    #         for i in range(len(move_available)):
    #             for j in range(len(move_available[i])):
    #         return root




    ## the min-max search
    """def min_max(self, children: [Node], color):
        determineMinMax = lambda color, priorityMapColor: max if color == priorityMapColor else min
        priority_map = defaultdict(list)
    """
    '''
        def AlphaBetaSearch(self) -> Move:
        _, move = self.maxValue(1)
        return move

    def maxValue(self, depth: int = 0,a: int = float('-inf'),b: int = float('inf')) -> (int, Move):

        if self.board.is_win(self.color) != 0 or depth == 0:
                #print(self.evaluate_score())
            return (self.evaluate_score(), [])

        for checkMoves in self.board.get_all_possible_moves(self.color):
            for move in checkMoves:
                self.board.make_move(move, self.color)
                currScore, _ = self.minValue(depth - 1,a,b)
                self.board.undo()
                if currScore > b:
                    return float('inf')
                a = max(a,currScore)
        return a,


    def minValue(self, depth: int = 0,a: int = float('-inf'),b: int = float('inf')) -> (int, Move):
        if self.board.is_win(self.color) != 0  or depth == 0:
            #print(self.evaluate_score())
            return (self.evaluate_score(), [])

        for checkMoves in self.board.get_all_possible_moves(self.color):
            for move in checkMoves:
                self.board.make_move(move, self.color)
                currScore, _ = self.maxValue(depth - 1)
                self.board.undo()
                if currScore > bestScore:
                    bestScore, bestMove = currScore, move
        return (bestScore, bestMove)
    '''

    def minmaxSearch(self) -> Move:
        _, move = self.maxValue(7)

        # move = self.greedy(self.board.get_all_possible_moves(self.color), max)[1]

        return move


    def maxValue(self, depth: int = 0, myTurn: bool = True) -> (int, Move):
        color = self.color if myTurn else self.opponent[self.color]
        if self.board.is_win(color) != 0:
            return (self.evaluate_score(myTurn), self.board.get_all_possible_moves(color)[0][0] if len(self.board.get_all_possible_moves(color)) != 0 else None)
        if depth == 1:
            bestScore = -100000000
            bestMove = None
            for moves in self.board.get_all_possible_moves(color):
                for move in moves:
                    self.board.make_move(move, color)
                    currScore = self.evaluate_score(myTurn)
                    self.board.undo()
                    if currScore > bestScore:
                        bestScore, bestMove = currScore, move

                # if not hasattr(bestMove, "seq"):
                #     return (bestScore, Move([]))

            return (bestScore, bestMove)

        bestScore = -100000000
        bestMove = None

        if len(self.board.get_all_possible_moves(color)) != 0:
            bestMove = self.board.get_all_possible_moves(color)[-1][-1]

        for moves in self.board.get_all_possible_moves(color):
            for move in moves:
                self.board.make_move(move, color)
                currScore, remaining_moves = self.maxValue(depth - 1, not myTurn)
                self.board.undo()
                if currScore > bestScore:
                    bestScore, bestMove = currScore, move

        # if not hasattr(bestMove, "seq"):
        #     return (bestScore, Move([]))

        return (bestScore, bestMove)


    def minValue(self, depth: int = 0) -> (int, Move):
        if self.board.is_win(self.opponent) != 0:
            return (self.evaluate_score(), Move([]))
        if depth == 0:
            return (self.evaluate_score(), Move([]))

        bestScore = 100000000
        bestMove = Move([])

        for moves in self.board.get_all_possible_moves(self.opponent):
            for move in moves:
                self.board.make_move(move, self.opponent)
                currScore, remaining_moves = self.maxValue(depth - 1)
                self.board.undo()
                if currScore < bestScore:
                    bestScore, bestMove = currScore, move


        # if not hasattr(bestMove, "seq"):
        #     return (bestScore, Move([]))

        return (bestScore, bestMove)




    ## greedy algorithm
    def greedy(self, moves, func: "function min or max") -> (int, Move):
        """
        give the children node and the color of checker.
        :param moves: the all possible moves from the get_all_possible_moves()
        :return the optimal moves by greedy algorithm
        """
        point_list = defaultdict(list)
        for i in moves:
            for j in i:
                self.board.make_move(j,self.color)
                point_list[self.evaluate_score()].append(j)
                self.board.undo()

        return (func(point_list.keys()), point_list[func(point_list.keys())][0])





































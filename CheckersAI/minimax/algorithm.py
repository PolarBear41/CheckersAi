from copy import deepcopy
import pygame

RED = (255,0,0)
WHITE = (255, 255, 255)

#functia minimax care calculeaza un decision tree, bazandu-se pe cate piese are fata de oponent
def minimax(position, depth, max_player, game):
    if depth == 0 or position.winner() != None:
        return position.evaluate(), position
    
    if max_player:
        maxEval = float('-inf') #incepem valoarea playerului care trebuie sa minimizeze scorul in favoarea sa de la -infinit
        best_move = None
        for move in get_all_moves(position, WHITE, game):
            evaluation = minimax(move, depth-1, False, game)[0]
            maxEval = max(maxEval, evaluation)
            if maxEval == evaluation:  
                best_move = move  #daca maxEval devine evaluation atunci am gasit cea mai optima mutare pentru acest jucator
        
        return maxEval, best_move
    else:
        minEval = float('inf') #incepem valoarea playerului care trebuie sa minimizeze scorul in favoarea sa de la infinit 
        best_move = None 
        for move in get_all_moves(position, RED, game):
            evaluation = minimax(move, depth-1, True, game)[0]  #functia devine recursiva astfel incat nu calculeaza la infinit, depth-ul scazand cu 1 dupa fiecare ramura parcursa
            minEval = min(minEval, evaluation)
            if minEval == evaluation:
                best_move = move #daca minEval devine evaluation atunci am gasit cea mai optima mutare pentru acest jucator
        
        return minEval, best_move


#aceasta functie ne ajuta cu functia get_all_moves
def simulate_move(piece, move, board, game, skip):
    board.move(piece, move[0], move[1])
    if skip:  
        board.remove(skip)

    return board

# get_all_moves are ca rol sa mapeze toate mutarile posibile, astfel combinand aceasta functie in minimax() pentru obtinerea celei mai bune mutari
def get_all_moves(board, color, game):
    moves = []

    for piece in board.get_all_pieces(color):
        valid_moves = board.get_valid_moves(piece)
        for move, skip in valid_moves.items():
            draw_moves(game, board, piece)
            temp_board = deepcopy(board)
            temp_piece = temp_board.get_piece(piece.row, piece.col)
            new_board = simulate_move(temp_piece, move, temp_board, game, skip)
            moves.append(new_board)
    
    return moves

#functia care se ocupa cu demonstrarea mutarilor pe care algoritmul le calculeaza
def draw_moves(game, board, piece):
    valid_moves = board.get_valid_moves(piece)
    board.draw(game.win)
    pygame.draw.circle(game.win, (0,255,0), (piece.x, piece.y), 50, 5)
    game.draw_valid_moves(valid_moves.keys())
    pygame.display.update()
    #pygame.time.delay(100)
from reversi import Reversi, Coord
from reversiai import ReversiAI
from aihelper import AIHelper, FormatConverter
import time
from prettytable import PrettyTable

def attack():
    # 1 - Coin Parrity
    # 2 - Stability
    # 3 - Corner occupancy
    # 4 - CORNER CLOSENESS
    # 5 - Mobility
    # 6 - Static
    player_black = ReversiAI(1, 1)
    player_white = ReversiAI(-1, 2) #black player is i
    game = Reversi()

    current_player = 1
    count = 0
    game.print_board()
    start_game = time.time()
    while True:
        board = FormatConverter.game_to_ai_board(game.board)
        start = None
        elapse = None
        count += 1
        print("Board ", "%3d" % count)
        move = None
        if current_player == 1:
            print("BLACK turn", game.player.field)    
            start = time.time()
            move = player_black.get_next_move(board, 1)
            elapse = time.time() - start
            # if move_b is not None:
            #     game.play(move_b)
            #     print("The move is : ", move_b, end=" ")
            #     print(" (in %.2f ms)" % (elapse*1000))
            # else:
            #     game.change_current_player()

            # current_player = -1

        elif current_player == -1:
            print("WHITE turn", game.player.field)    
            start = time.time()
            move = player_white.get_next_move(board, -1)
            elapse = time.time() - start
            # if move_b is not None:
            #     game.play(move_b)
            #     print("The move is : ", move_b, end=" ")
            #     print(" (in %.2f ms)" % (elapse*1000))
            # else:
            #     game.change_current_player()

            # current_player = -1

        if move is not None:
            game.play(move)
            print("The move is : ", move, end=" ")
            print(" (in %.2f ms)" % (elapse*1000))
        else:
            game.change_current_player()

        current_player = -current_player

    
        if game.game_state!='In progress':
            game.print_board()
            print(game.black_player.result, ' - ', game.white_player.result)
            print(game.game_state)
            break
        game.print_board()
        print("------------------------------------")

    print("END GAME in %.2f s" % (time.time() - start_game))



if __name__ == '__main__':
    attack()
    # board = [[0  ,-1  ,-1  ,-1  ,-1   ,1   ,0   ,0],
    #         [0   ,0  ,-1  ,-1   ,1   ,1   ,1   ,0],
    #         [0   ,0   ,1  ,-1  ,-1  ,-1   ,1   ,0],
    #         [1   ,1   ,1   ,1  ,-1   ,1   ,1   ,1],
    #         [1   ,1  ,-1  ,-1   ,1   ,1   ,0   ,0],
    #         [1  ,-1   ,1   ,1  , 1  ,1   ,0   ,0],
    #         [-1   ,1   ,1   ,1   ,0   ,1  , 1   ,0],
    #         [-1   ,1   ,1   ,0   ,0   ,0   ,0   ,1]]
    board = [[0,0,-1,-1,-1,-1,0,0],
        [0,0,1,-1,-1,-1,1,0],
        [0,0,1,1,-1,-1,1,0],
        [1,1,1,-1,-1,1,1,1],
        [1,1,-1,-1,-1,1,0,0],
        [1,-1,1,1,1,1,1,0],
        [-1,1,1,1,0,1,1,0],
        [-1,1,1,0,0,0,0,1]] 
    # player_white = AIHelper()
    # for i in player_white.available_moves(board, -1):
    #     print(i, end="")
    # w = ReversiAI(1, 1)
    # print(w.get_next_move(board, 1))

    # print('\n',player_white.get_resulting_board(board, -1, player_white.available_moves(board, -1)[1]))







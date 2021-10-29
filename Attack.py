from reversi import Reversi, Coord
from reversiai import ReversiAI
from aihelper import AIHelper, FormatConverter
import time
from prettytable import PrettyTable

def attack():
    # 1 - Coin Parrity
    # 2 - Mobility
    # 3 - Corner occupancy
    # 4 - Stability
    # 5 - Total
    player_black = ReversiAI(1, 4)
    player_white = ReversiAI(-1, 4) #black player is i
    game = Reversi()

    current_player = 1
    count = 0
    game.print_board()
    start_game = time.time()
    while True:
        count += 1
        print("Board ", "%3d" % count)

        board = FormatConverter.game_to_ai_board(game.board)
        start = None
        elapse = None
        move = None
        
        if game.player.field == 1:
            print("BLACK turn")   
            start = time.time()
            move = player_black.get_next_move(board, 1)
            elapse = time.time() - start


        elif game.player.field == -1:
            print("WHITE turn")   
            start = time.time()
            move = player_white.get_next_move(board, -1)
            elapse = time.time() - start

        if move:
            game.play(move)
            print("The move is : ", move, end=" ")
            print(" (in %.2f ms)" % (elapse*1000))
        else:
            print("Not move")
            game.change_current_player()

        if game.game_state != 'In progress':
            game.print_board()
            print(game.black_player.result, ' - ', game.white_player.result)
            print(game.game_state)
            break
        game.print_board()
        print("------------------------------------")

    print("END GAME in %.2f s" % (time.time() - start_game))


def print_board(board):
    print("%7d" % 0, "%3d" % 1, "%3d" % 2, "%3d" % 3, "%3d" % 4, "%3d" % 5, "%3d" % 6, "%3d" %7)
    for i in range(8):
        print(i, ":", end=" ")
        for j in range(8):
            print("%3d" % board[i][j], end=" ")
        print()
    print("")

if __name__ == '__main__':
    attack()

    # board = [[0,0,1,1,1,1,1,-1],
    #         [1,1,1,1,1,1,1,-1],
    #         [1,1,1,-1,-1,1,-1,-1],
    #         [1,1,1,1,-1,1,1,-1],
    #         [1,1,-1,-1,-1,-1,1,-1],
    # [1,-1,-1,-1,-1,-1,-1,-1],
    # [-1,-1,-1,-1,-1,-1,-1,-1],
    # [-1,0,-1,-1,-1,-1,-1,-1]] 
    # print_board(board)
    # player = AIHelper()
    # x = Coord(0,1)
    # board = player.get_resulting_board(board, -1, x)
    # print_board(board)
    # x = Coord(0,0)
    # board = player.get_resulting_board(board, 1, x)
    # print_board(board)
    # print(player.available_moves(board,1))
    # print(player_white.available_moves(board, 1)[0])
    # for i in player_white.available_moves(board, -1):
    #     print(i, end="")
    # print_board(board)
    # w = ReversiAI(-1, 1)
    # print(type(w.get_next_move(board, -1)))

    # print('\n',player_white.get_resulting_board(board, -1, player_white.available_moves(board, -1)[1]))








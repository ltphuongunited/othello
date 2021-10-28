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
    for i in range(1,5):
        player_black = ReversiAI(1, i)
    
        player_white = ReversiAI(-1, 5)
        game = Reversi()

        current_player = 1
        count = 0
        # game.print_board()
        start_game = time.time()
        while True:
            count += 1
            # print("Board ", "%3d" % count)

            board = FormatConverter.game_to_ai_board(game.board)
            start = None
            elapse = None
            move = None
            
            if game.player.field == 1:
                # print("BLACK turn")   
                start = time.time()
                move = player_black.get_next_move(board, 1)
                elapse = time.time() - start


            elif game.player.field == -1:
                # print("WHITE turn")   
                start = time.time()
                move = player_white.get_next_move(board, -1)
                elapse = time.time() - start

            if move:
                game.play(move)
                # print("The move is : ", move, end=" ")
                # print(" (in %.2f ms)" % (elapse*1000))
            else:
                # print("Not move")
                game.change_current_player()

            if game.game_state != 'In progress':
                # game.print_board()
                print(game.black_player.result, ' - ', game.white_player.result)
                # print(game.game_state)
                break
            # game.print_board()
            # print("------------------------------------")

        # print("END GAME in %.2f s" % (time.time() - start_game))



if __name__ == '__main__':
    attack()







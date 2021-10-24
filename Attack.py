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
    heuristic = ("Pass", "Coin Parity", "Stability", "Corner occupancy", "Mobility", "Static", "Total")
    result_table = PrettyTable()
    result_table.field_names = [" ", heuristic[1], heuristic[2], heuristic[3], heuristic[4], heuristic[5], heuristic[6]]
    # Black player is 1
    # White player is -1
    for i in range(1, 7):
        player_black = ReversiAI(i)
        turn = []
        turn.append(heuristic[i])
        for j in range(1, 7):
            player_white = ReversiAI(j) #black player is i
            if i == j:
                turn.append('N/A')
                continue
            game = Reversi()
            current_player = 1
            count = 0
            # game.print_board()
            start_game = time.time()
            while True:
                board = FormatConverter.game_to_ai_board(game.board)
                start = None
                elapse = None
                if current_player == 1:
                    # print("BLACK turn")    
                    start = time.time()
                    move_b = player_black.get_next_move(board,1)
                    elapse = time.time() - start
                    if move_b is not None:
                        game.play(move_b)
                        # print("The move is : ", move_b, end=" ")
                        # print(" (in %.2f ms)" % (elapse*1000))
                    current_player = -1

                else:
                    # print("WHITE turn")    
                    start = time.time()
                    move_w = player_white.get_next_move(board,-1)
                    elapse = time.time() - start
                    if move_w is not None:
                        game.play(move_w)
                        # print("The move is : ", move_w, end=" ")
                        # print(" (in %.2f ms)" % (elapse*1000))
                    current_player = 1

                # count += 1
                # print("Board ", "%3d" % count)
                if game.game_state!='In progress':
                    turn.append(str(game.black_player.result) + ' - ' + str(game.white_player.result))
                    # print(heuristic[j],": ", game.black_player.result, ' - ', game.white_player.result)
                    # game.print_board()
                    # print(game.game_state)
                    break
                # game.print_board()
                # print("------------------------------------")

            # print("END GAME in %.2f s" % (time.time() - start_game))
        result_table.add_row(turn)
    print(result_table)



if __name__ == '__main__':
    attack()







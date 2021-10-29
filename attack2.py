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
    heuristic = ("Pass", "Coin Parity", "Mobility", "Corner occupancy", "Stability")
    result_table = PrettyTable()
    result_table.field_names = [" ", heuristic[1], heuristic[2], heuristic[3], heuristic[4]]
    # Black player is 1
    # White player is -1
    for i in range(1,5):
        player_black = ReversiAI(1, i)
        turn = []
        turn.append(heuristic[i])
        for j in range(1,5):
            player_white = ReversiAI(-1, j) #black player is i
            if i == j:
                turn.append('N/A')
                continue
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

                if game.game_state!='In progress':
                    turn.append(str(game.black_player.result) + ' - ' + str(game.white_player.result))
                    print(i*j)
                    break

        result_table.add_row(turn)
    print(result_table)


if __name__ == '__main__':
    attack()








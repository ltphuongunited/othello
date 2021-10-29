from reversi import Reversi, Coord
from reversiai import ReversiAI
from aihelper import AIHelper, FormatConverter
import time
from prettytable import PrettyTable
from prettytable import PrettyTable

def attack():
    # 1 - Coin Parrity
    # 2 - Mobility
    # 3 - Corner occupancy
    # 4 - Stability
    # 5 - Total
    start = time.time()
    heuristic = ("Pass", "Coin Parity", "Mobility", "Corner occupancy", "Stability")
    result_table = PrettyTable()
    result_table.field_names = [" ", heuristic[1], heuristic[2], heuristic[3], heuristic[4]]
    # result_table.field_names = [" ", "Medium"]
    player_white = ReversiAI(-1, 5)
    turn_1 = []
    turn_1.append("Total is white")
    for i in range(1,5):
        player_black = ReversiAI(1, i)
        game = Reversi()

        count = 0

        while True:
            count += 1

            board = FormatConverter.game_to_ai_board(game.board)
            move = None
            
            if game.player.field == 1:
                move = player_black.get_next_move(board, 1)


            elif game.player.field == -1:
                move = player_white.get_next_move(board, -1)

            if move:
                game.play(move)
            else:
                game.change_current_player()

            if game.game_state != 'In progress':
                turn_1.append(str(game.black_player.result) + ' - ' + str(game.white_player.result))
                print(i)
                break

    
    turn_2 = []
    turn_2.append("Total is black")    
    player_black = ReversiAI(1, 5)
    for i in range(1,5):
        player_white = ReversiAI(-1, i)
        game = Reversi()

        count = 0
        while True:
            count += 1

            board = FormatConverter.game_to_ai_board(game.board)
            move = None
            
            if game.player.field == 1:
                move = player_black.get_next_move(board, 1)


            elif game.player.field == -1:
                move = player_white.get_next_move(board, -1)

            if move:
                game.play(move)
            else:
                game.change_current_player()

            if game.game_state != 'In progress':
                turn_2.append(str(game.black_player.result) + ' - ' + str(game.white_player.result))
                print(i)
                break

    result_table.add_row(turn_1)
    result_table.add_row(turn_2)
    print(result_table)
    print("END in %.2f s" % (time.time() - start))

if __name__ == '__main__':
    attack()








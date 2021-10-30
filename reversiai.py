from aihelper import AIHelper


class ReversiAI():
    
    def __init__(self, player, heuristic):
        self.MAX_PLAYER = player
        self.heuristic = heuristic

    # runs the minimax with precision
    # @staticmethod
    def get_next_move(self, board, player):
        # the depth argument defines how many levels deep we go before using heuristic
        _, move = self.alpha_beta(board, 3, player)
        return move

    # @staticmethod
    def minimax(self, board, depth, player):
        helper = AIHelper()

        # if game is over then return something
        if helper.is_game_over(board) or depth == 0 or len(helper.available_moves(board, player)) == 0:
            # print(self.game_heuristic(board))
            return (self.game_heuristic(board), None)

        best_move = None
        # if it is a max node
        if player == self.MAX_PLAYER:
            best_value = -AIHelper.INFINITY
            available_moves = helper.available_moves(board, self.MAX_PLAYER)
            for move in available_moves:
                node = helper.get_resulting_board(board, self.MAX_PLAYER, move)
                value, _ = self.minimax(node, depth - 1, -self.MAX_PLAYER)
                if value > best_value:
                    best_value = value
                    best_move = move
            return (best_value, best_move)

        # if it is a min node
        else:
            best_value = AIHelper.INFINITY
            available_moves = helper.available_moves(board, -self.MAX_PLAYER)
            for move in available_moves:
                node = helper.get_resulting_board(board, -self.MAX_PLAYER, move)
                value, _ = self.minimax(node, depth - 1, self.MAX_PLAYER)
                if value < best_value:
                    best_value = value
                    best_move = move
            return (best_value, best_move)
    
    def alpha_beta(self, board, depth, player):
        return self.alpha_beta_pruning(board, depth, player, -AIHelper.INFINITY,AIHelper.INFINITY)

    def alpha_beta_pruning(self, board, depth, player, a, b):
        helper = AIHelper()
        # if game is over then return something
        if helper.is_game_over(board) or depth == 0 or len(helper.available_moves(board, player)) == 0:
            return (self.game_heuristic(board), None)

        best_move = None
        # if it is a max node
        if player == self.MAX_PLAYER:
            available_moves = helper.available_moves(board, self.MAX_PLAYER)
            for move in available_moves:
                node = helper.get_resulting_board(board, self.MAX_PLAYER, move)
                value, _ = self.alpha_beta_pruning(node, depth - 1, -self.MAX_PLAYER, a, b)
                if value > a:
                    a = value
                    best_move = move
                if a >= b:
                    break
            return (a, best_move)

        # if it is a min node
        else:
            available_moves = helper.available_moves(board, -self.MAX_PLAYER)
            for move in available_moves:
                node = helper.get_resulting_board(board, -self.MAX_PLAYER, move)
                value, _ = self.alpha_beta_pruning(node, depth - 1, self.MAX_PLAYER, a, b)
                if value < b:
                    b = value
                    best_move = move
                if a >= b:
                    break
            return (b, best_move)


    # @staticmethod
    def game_heuristic(self, board):
        # defining the ai and Opponent color
        my_color = self.MAX_PLAYER
        opp_color = -self.MAX_PLAYER

        my_tiles = 0
        opp_tiles = 0
        my_front_tiles = 0
        opp_front_tiles = 0

        coin = 0
        mobility = 0
        corner = 0
        stability = 0

        # these two are used for going in every 8 directions
        X1 = [-1, -1, 0, 1, 1, 1, 0, -1]
        Y1 = [0, 1, 1, 1, 0, -1, -1, -1]

        # =============================================================================================
        # 1 - Coin Parity
        # =============================================================================================
        for i in range(8):
            for j in range(8):
                if board[i][j] == my_color:
                    my_tiles += 1
                elif board[i][j] == opp_color:
                    opp_tiles += 1
        coin = 100 * (my_tiles - opp_tiles) / (my_tiles + opp_tiles)

        # 2 - Mobility
        # ===============================================================================================
        '''
        It attempts to capture the relative difference between 
        the number of possible moves for the max and the min players,
        with the intent of restricting the
        opponent’s mobility and increasing one’s own mobility
        '''
        # basically it calculates the difference between available moves
        my_tiles = len(AIHelper().available_moves(board, my_color))
        opp_tiles = len(AIHelper().available_moves(board, opp_color))

        if (my_tiles + opp_tiles != 0): 
            mobility = (100.0 * (my_tiles - opp_tiles)) / (my_tiles + opp_tiles)
        else:
            mobility = 0

        # ===============================================================================================
        # 3 - Corner occupancy
        '''
        Examine all 4 corners :
        if they were my color add a point to me 
        if they were enemies add a point to the enemy
        '''
        # ===============================================================================================
        my_tiles = opp_tiles = 0
        if board[0][0] == my_color:
            my_tiles += 1
        elif board[0][0] == opp_color:
            opp_tiles += 1
        if board[0][7] == my_color:
            my_tiles += 1
        elif board[0][7] == opp_color:
            opp_tiles += 1
        if board[7][0] == my_color:
            my_tiles += 1
        elif board[7][0] == opp_color:
            opp_tiles += 1
        if board[7][7] == my_color:
            my_tiles += 1
        elif board[7][7] == opp_color:
            opp_tiles += 1

        if (my_tiles + opp_tiles != 0):
            corner = 100 * (my_tiles - opp_tiles) / (my_tiles + opp_tiles)
        else:
            corner = 0


        # =============================================================================================
        # 4.1 - Stability - calculates the blank Spaces around my tiles
        # =============================================================================================
        for i in range(8):
            for j in range(8):
                if board[i][j] != 0:
                    for k in range(8):
                        x = i + X1[k]
                        y = j + Y1[k]
                        if (x >= 0 and x < 8 and y >= 0 and y < 8 and board[x][y] == 0):
                            if board[i][j] == my_color:
                                my_front_tiles += 1
                            else:
                                opp_front_tiles += 1
                            break

        if (my_front_tiles + opp_front_tiles != 0):
            stability_1 = -(50.0 * (my_front_tiles - opp_front_tiles)) / (my_front_tiles + opp_front_tiles)
        else:
            stability_1 = 0

        # 4.2 - CORNER CLOSENESS
        '''
        If the corner is empty then find out how many of the 
        adjacent block to the corner are AI's or the player's
        if AI's tiles were mote than players than it's a bad thing.
        '''
        # ===============================================================================================
        my_tiles = opp_tiles = 0
        if board[0][0] == 0:
            if board[0][1] == my_color:
                my_tiles += 1
            elif board[0][1] == opp_color:
                opp_tiles += 1
            if board[1][1] == my_color:
                my_tiles += 1
            elif board[1][1] == opp_color:
                opp_tiles += 1
            if board[1][0] == my_color:
                my_tiles += 1
            elif board[1][0] == opp_color:
                opp_tiles += 1

        if board[0][7] == 0:
            if board[0][6] == my_color:
                my_tiles += 1
            elif board[0][6] == opp_color:
                opp_tiles += 1
            if board[1][6] == my_color:
                my_tiles += 1
            elif board[1][6] == opp_color:
                opp_tiles += 1
            if board[1][7] == my_color:
                my_tiles += 1
            elif board[1][7] == opp_color:
                opp_tiles += 1

        if board[7][0] == 0:
            if board[7][1] == my_color:
                my_tiles += 1
            elif board[7][1] == opp_color:
                opp_tiles += 1
            if board[6][1] == my_color:
                my_tiles += 1
            elif board[6][1] == opp_color:
                opp_tiles += 1
            if board[6][0] == my_color:
                my_tiles += 1
            elif board[6][0] == opp_color:
                opp_tiles += 1

        if board[7][7] == 0:
            if board[6][7] == my_color:
                my_tiles += 1
            elif board[6][7] == opp_color:
                opp_tiles += 1
            if board[6][6] == my_color:
                my_tiles += 1
            elif board[6][6] == opp_color:
                opp_tiles += 1
            if board[7][6] == my_color:
                my_tiles += 1
            elif board[7][6] == opp_color:
                opp_tiles += 1

        if (my_tiles + opp_tiles != 0):
            stability_2 = -50 * (my_tiles - opp_tiles) / (my_tiles + opp_tiles)
        else:
            stability_2 = 0

        stability = stability_1 + stability_2

        # =============================================================================================
        # =============================================================================================
        # final weighted score
        # adding different weights to different evaluations

        if self.heuristic == 1:
            return coin
        elif self.heuristic == 2:
            return mobility
        elif self.heuristic == 3:
            return corner
        elif self.heuristic == 4:
            return stability
        else:
            return (5 * coin) + (35 * corner) + (25 * mobility) + 35 * stability

        #Easy: coin
        #Medium: stability + 0.5 * mobility
        #Hard: (7 * coin) + (33 * corner) + (34 * mobility) + 13 * stability
        
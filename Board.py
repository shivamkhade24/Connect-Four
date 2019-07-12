class Board:

    grid = []

    rows = 7
    columns = 6

    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.grid = [[0 for x in range(self.rows)] for y in range(self.columns)]



    def put_disk_on_column(self, col_number, player_number):
        for y in range(self.rows-1, -1, -1):
            if self.grid[col_number][y] == 0:
                self.grid[col_number][y] = player_number
                break

    def check_for_winner(self, player):
        if self.check_horizontally(player) != -1 or self.check_vertically(player) != -1 or \
                        self.check_first_diagonally(player) != -1 or self.check_second_diagonally(player) != -1:
            return player.get_player_number
        return -1

    def check_horizontally(self, player):
        for y in range(self.rows):
            for x in range(self.columns - 3):
                if self.grid[x][y] != 0:
                    last_disk_color = self.grid[x][y]
                    winner = True
                    for k in range(4):
                        if self.grid[x+k][y] != last_disk_color:
                            winner = False
                    if winner:
                        return player.get_player_number()
        return -1

    def check_vertically(self, player):
        for x in range(self.columns):
            for y in range(self.rows - 3):
                if self.grid[x][y] != 0:
                    last_disk_color = self.grid[x][y]
                    winner = True
                    for k in range(4):
                        if self.grid[x][y+k] != last_disk_color:
                            winner = False
                    if winner:
                        return player.get_player_number()
        return -1

    def check_first_diagonally(self, player):
        for i in range(3):
            for e in range(4):
                if self.grid[i][e] == player.get_player_number() and self.grid[i + 1][e + 1] == player.get_player_number() and self.grid[i + 2][e + 2] == player.get_player_number() and self.grid[i + 3][e + 3] == player.get_player_number():
                    return player.get_player_number()
        return -1

    def check_second_diagonally(self, player):
        for i in range(3):
            for e in range(self.columns-1, -1, -1):
                if self.grid[i][e] == player.get_player_number() and self.grid[i + 1][e - 1] == player.get_player_number() \
                        and self.grid[i + 2][e - 2] == player.get_player_number() and self.grid[i + 3][e - 3] == player.get_player_number():
                    return player.get_player_number()
        return -1

    def check_if_board_full(self):
        for y in range(self.rows):
            for x in range(self.columns):
                if self.grid[x][y] == 0:
                    return False

        return True

    def print_grid(self):
        for y in range(self.rows):
            for x in range(self.columns):
                print(self.grid[x][y], end=" ")
            print()

    def get_rows(self):
        return self.rows

    def get_columns(self):
        return self.columns

    def get_board_info_at_pos(self, pos_x, pos_y):
        # get the info number item at the given position
        return self.grid[pos_x][pos_y]

    def set_board(self, loaded_board):
        self.grid = loaded_board

    def get_board(self):
        return self.grid


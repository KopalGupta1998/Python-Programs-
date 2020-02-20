"""
Loyd's Fifteen puzzle - solver and visualizer
Note that solved configuration has the blank (zero) tile in upper left
Use the arrows key to swap this tile with its neighbors
"""

import poc_fifteen_gui

class Puzzle:
    """
    Class representation for the Fifteen puzzle
    """

    def __init__(self, puzzle_height, puzzle_width, initial_grid=None):
        """
        Initialize puzzle with default height and width
        Returns a Puzzle object
        """
        self._height = puzzle_height
        self._width = puzzle_width
        self._grid = [[col + puzzle_width * row
                       for col in range(self._width)]
                      for row in range(self._height)]

        if initial_grid != None:
            for row in range(puzzle_height):
                for col in range(puzzle_width):
                    self._grid[row][col] = initial_grid[row][col]

    def __str__(self):
        """
        Generate string representaion for puzzle
        Returns a string
        """
        ans = ""
        for row in range(self._height):
            ans += str(self._grid[row])
            ans += "\n"
        return ans

    #####################################
    # GUI methods

    def get_height(self):
        """
        Getter for puzzle height
        Returns an integer
        """
        return self._height

    def get_width(self):
        """
        Getter for puzzle width
        Returns an integer
        """
        return self._width

    def get_number(self, row, col):
        """
        Getter for the number at tile position pos
        Returns an integer
        """
        return self._grid[row][col]

    def set_number(self, row, col, value):
        """
        Setter for the number at tile position pos
        """
        self._grid[row][col] = value

    def clone(self):
        """
        Make a copy of the puzzle to update during solving
        Returns a Puzzle object
        """
        new_puzzle = Puzzle(self._height, self._width, self._grid)
        return new_puzzle

    ########################################################
    # Core puzzle methods

    def current_position(self, solved_row, solved_col):
        """
        Locate the current position of the tile that will be at
        position (solved_row, solved_col) when the puzzle is solved
        Returns a tuple of two integers        
        """
        solved_value = (solved_col + self._width * solved_row)

        for row in range(self._height):
            for col in range(self._width):
                if self._grid[row][col] == solved_value:
                    return (row, col)
        assert False, "Value " + str(solved_value) + " not found"

    def update_puzzle(self, move_string):
        """
        Updates the puzzle state based on the provided move string
        """
        zero_row, zero_col = self.current_position(0, 0)
        for direction in move_string:
            if direction == "l":
                assert zero_col > 0, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row][zero_col - 1]
                self._grid[zero_row][zero_col - 1] = 0
                zero_col -= 1
            elif direction == "r":
                assert zero_col < self._width - 1, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row][zero_col + 1]
                self._grid[zero_row][zero_col + 1] = 0
                zero_col += 1
            elif direction == "u":
                assert zero_row > 0, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row - 1][zero_col]
                self._grid[zero_row - 1][zero_col] = 0
                zero_row -= 1
            elif direction == "d":
                assert zero_row < self._height - 1, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row + 1][zero_col]
                self._grid[zero_row + 1][zero_col] = 0
                zero_row += 1
            else:
                assert False, "invalid direction: " + direction

    ##################################################################
    # Phase one methods

    
    def lower_row_invariant(self, target_row, target_col):
        """
        Check whether the puzzle satisfies the specified invariant
        at the given position in the bottom rows of the puzzle (target_row > 1)
        Returns a boolean
        """
        height = self.get_height()
        width = self.get_width()
        if self.get_number(target_row, target_col) != 0:
            return False
        for row in range(target_row+1, height):
            for col in range(width):
                if self.current_position(row, col) != (row, col):
                    return False
        for col in range(target_col+1, width):
            if self.current_position(target_row, col) != (target_row, col):
                return False
        return True

    def position_tile(self, target_row, target_col, current_row, current_col):
        """
        helper function based on Homework Q2 and Q8
        return: move string
        """
        move_str = ''
        druld = 'druld'
        row_diff = target_row - current_row
        col_diff = target_col - current_col

        move_str += row_diff * 'u'
        if col_diff == 0:
            move_str += 'ld' + (row_diff - 1) * druld
        elif col_diff > 0:
            move_str += col_diff * 'l'
            if current_row == 0:
                move_str += (abs(col_diff) - 1) * 'drrul'
            else:
                move_str += (abs(col_diff) - 1) * 'urrdl'
            move_str += row_diff * druld
        elif col_diff < 0:
            move_str += (abs(col_diff) - 1) * 'r'
            if current_row == 0:
                move_str += abs(col_diff) * 'rdllu'
            else:
                move_str += abs(col_diff) * 'rulld'
            move_str += row_diff * druld
        move_str = self.move_str_trimmer(move_str)
        return move_str

    def move_str_trimmer(self, move_str):
        """
        Trim redundant move
        """
        move_str2 = move_str
        move_str = move_str.replace('ud', '').replace('du', '').replace('lr', '').replace('rl', '')
        if move_str == move_str2:
            return move_str2
        else:
            return self.move_str_trimmer(move_str)

    def solve_interior_tile(self, target_row, target_col):
        """
        Place correct tile at target position
        Updates puzzle and returns a move string
        """
        assert self.lower_row_invariant(target_row, target_col)

        current_row, current_col = self.current_position(target_row, target_col)
        assert (current_row < target_row) or ((current_row == target_row) and (current_col < target_col))
        if (current_row, current_col) == (target_row, target_col):
            return ''
        move_str = self.position_tile(target_row, target_col, current_row, current_col)
        self.update_puzzle(move_str)
        assert self.lower_row_invariant(target_row, target_col - 1)
        return move_str

    def solve_col0_tile(self, target_row):
        """
        Solve tile in column zero on specified row (> 1)
        Updates puzzle and returns a move string
        """
        width = self.get_width()
        assert self.lower_row_invariant(target_row, 0)
        move_str = 'ur'
        self.update_puzzle(move_str)

        current_row, current_column = self.current_position(target_row, 0)
        if current_row == target_row and current_column == 0:
            move = (width - 2) * 'r'
            self.update_puzzle(move)
            move_str += move
        else:
            move = self.position_tile(target_row - 1, 1, current_row, current_column)
            move += 'ruldrdlurdluurddlu' + (width - 1) * 'r'
            move = self.move_str_trimmer(move)
            self.update_puzzle(move)
            move_str += move
        assert self.lower_row_invariant(target_row - 1, width - 1)
        return move_str


    #############################################################
    # Phase two methods

    def row0_invariant(self, target_col):
        """
        Check whether the puzzle satisfies the row zero invariant
        at the given column (col > 1)
        Returns a boolean
        """
        width=self.get_width()
        height=self.get_height()
        if self.get_number(0,target_col) !=0:
            return False
        for row in range(2,height):
            for col in range(width):
                if self.current_position(row,col)!=(row,col):
                    return False
        for col in range(target_col,width):
            if self.current_position(1,col)!=(1,col):
                return False
        for col in range(target_col+1,width):
            if self.current_position(0,col)!=(0,col):
                return False
        return True

    def row1_invariant(self, target_col):
        """
        Check whether the puzzle satisfies the row one invariant
        at the given column (col > 1)
        Returns a boolean
        """
        width=self.get_width()
        height=self.get_height()
        if self.get_number(1,target_col) !=0:
            return False
        for row in range(2,height):
            for col in range(width):
                if self.current_position(row,col)!=(row,col):
                    return False
        for col in range(target_col+1,width):
            if self.current_position(1,col)!=(1,col):
                return False
        for col in range(target_col+1,width):
            if self.current_position(0,col)!=(0,col):
                return False
        return True


    def solve_row0_tile(self, target_col):
        """
        Solve the tile in row zero at the specified column
        Updates puzzle and returns a move string
        """
        assert self.row0_invariant(target_col)
        move_str="ld"
        self.update_puzzle(move_str)
        current_row,current_col=self.current_position(0,target_col)
        if current_row==0 and current_col==target_col:
            return move_str
        else:
            move=self.position_tile(1,target_col-1,current_row,current_col)
            move += 'urdlurrdluldrruld'
            move = self.move_str_trimmer(move)
            self.update_puzzle(move)
            move_str += move
        assert self.row1_invariant(target_col-1)
        return move_str

    def solve_row1_tile(self, target_col):
        """
        Solve the tile in row one at the specified column
        Updates puzzle and returns a move string
        """
        assert self.row1_invariant(target_col)
        current_row,current_col=self.current_position(1,target_col)
        move_str=self.position_tile(1,target_col,current_row,current_col)
        move_str+="ur"
        move_str=self.move_str_trimmer(move_str)
        self.update_puzzle(move_str)
        return move_str

    ###########################################################
    # Phase 3 methods

    def solve_2x2(self):
        """
        Solve the upper left 2x2 part of the puzzle
        Updates the puzzle and returns a move string
        """
        assert self.row1_invariant(1)
        move_str="lu"
        move="rdlu"
        self.update_puzzle(move_str)
        while self.current_position(0,1)!=(0,1):
            self.update_puzzle(move)
            move_str+=move
        return move_str

    def solve_puzzle(self):
        """
        Generate a solution string for a puzzle
        Updates the puzzle and returns a move string
        """
        height=self.get_height()
        width=self.get_width()
        move_str=''
        current_row,current_col=self.current_position(0,0)
        row_diff = current_row - (height-1)
        col_diff = current_col - (width-1)
        move = abs(row_diff) * 'd' + abs(col_diff) * 'r'
        move = self.move_str_trimmer(move)
        self.update_puzzle(move)
        move_str += move
        
        for row in range(height-1,1,-1):
            for col in range(width-1,0,-1):
                move_str+=self.solve_interior_tile(row,col)
            move_str+=self.solve_col0_tile(row)
        for col in range(width-1,1,-1):
            move_str += self.solve_row1_tile(col)
            move_str += self.solve_row0_tile(col)
        move_str += self.solve_2x2()
        return move_str

poc_fifteen_gui.FifteenGUI(Puzzle(4, 4, [[15, 11, 8, 12], [14, 10, 9, 13], [2, 6, 1, 4], [3, 7, 5, 0]]))

My_Puzzle = Puzzle(4, 4, [[15, 11, 8, 12], [14, 10, 9, 13], [2, 6, 1, 4], [3, 7, 5, 0]])
print My_Puzzle.solve_puzzle()




"""
Clone of 2048 game.
"""

import poc_2048_gui
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    # Create a copy of the input list line
    list_copy=[]
    #adding the none zero elements of line to list_copy
    for dummy_i in range(len(line)):
        if line[dummy_i] != 0:
            list_copy.append(line[dummy_i])
    # adding the appropriate number of zeros to match the length of list_copy and line
    for dummy_j in range(len(list_copy),len(line)):
        list_copy.append(0)
    
    # merging the tiles that have the same value
    for dummy_k in range(len(list_copy)-1):
        # checking for equal values of the adjacent tiles 
        if list_copy[dummy_k]!=0 and list_copy[dummy_k]==list_copy[dummy_k+1]:
            # if equal double the value of the first tile and assign zero to second tile
            list_copy[dummy_k]=2*list_copy[dummy_k]
            list_copy[dummy_k+1]=0
            
            #shifting the rest of the values ot the tiles by one place
            for dummy_p in range(dummy_k+1,len(list_copy)-1):
                list_copy[dummy_p]=list_copy[dummy_p+1]
            if (len(line)>3):
                list_copy[-2]=list_copy[-1]
            list_copy[-1]=0
    # returning list_copy which is the answer
    return list_copy

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        # initializing the required variables
        self._width=grid_width
        self._height=grid_height
        self._grid=None
        self.reset()
        self._up_initial_cells=[]
        self._down_initial_cells=[]
        self._left_initial_cells=[]
        self._right_initial_cells=[]
        for dummy_i in range(self._width):
            self._up_initial_cells.append((0,dummy_i))
            self._down_initial_cells.append((self._height-1,dummy_i))
        for dummy_i in range(self._height):
            self._left_initial_cells.append((dummy_i,0))
            self._right_initial_cells.append((dummy_i,self._height-1))
        self._initial_cells={UP:self._up_initial_cells,
           DOWN: self._down_initial_cells,
           LEFT: self._left_initial_cells,
           RIGHT: self._right_initial_cells}
        
    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        # creating the grid with the values all initialized to zero
        
        self._grid = [[ 0 for dummy_col in range(self._width)]
                           for dummy_row in range(self._height)]
        # introducing the two initial tiles
        self.new_tile()
        self.new_tile()
        #for testing purposes
        #print self.grid
        #print self
    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        string_rep_of_grid=""
        row=""
        for dummy_j in range(self._height):
            for dummy_i in range(self._width):
                row=row+str(self._grid[dummy_j][dummy_i])+" " 
            string_rep_of_grid=string_rep_of_grid+"row number "+str(dummy_j)+": "+row
            row=""
        return string_rep_of_grid

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self._height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        # replace with your code
        return self._width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        # we are initializing the required variables
        num_steps=0
        if direction== UP or direction==DOWN:
            num_steps=self._height
        if direction==LEFT or direction==RIGHT:
            num_steps=self._width
        move_in=OFFSETS[direction]
        temp_list=[]
        moved=False 
        # merging the list in the particular direction
        for start_cell in self._initial_cells[direction]:
            for step in range(num_steps):
                row = start_cell[0] + step * move_in[0]
                col = start_cell[1] + step * move_in[1]
                # creating a list of all the columns and rows in that direction 
                temp_list.append(self._grid[row][col])
            # caling the merge function to calculate the resultant list
            merged_list=merge(temp_list)
            # putting back the resultant list
            for step in range(num_steps):
                row = start_cell[0] + step * move_in[0]
                col = start_cell[1] + step * move_in[1]
                self._grid[row][col]=merged_list[step]
            # cheking for any changes in the board
            if temp_list!=merged_list:
                moved=True
            temp_list=[]
        #adding anew tile
        if moved:
            self.new_tile()
    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        # creating a list value to ensure the 90 and 10 percent ratio
        value=[2,2,2,2,2,2,2,2,2,2]
        position_of_4=random.randrange(0,10)
        value[position_of_4]=4
        # selecting a random position on the grid
        dummy_row=random.randrange(0,self._height)
        dummy_column=random.randrange(0,self._width)
        # check to ensure that same tiles are not selected
        if self._grid[dummy_row][dummy_column]!=0:
            while self._grid[dummy_row][dummy_column]!=0:
                dummy_row=random.randrange(0,self._height)
                dummy_column=random.randrange(0,self._width)
        # assigning a value to the selected tile
        self._grid[dummy_row][dummy_column]=random.choice(value)
                
    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._grid[row][col]=value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self._grid[row][col]
    
#game=TwentyFortyEight(4, 4)
#print game
poc_2048_gui.run_gui(TwentyFortyEight(4, 4))

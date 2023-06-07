class Cell:
    def __init__(self, mine, around_mines=0):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = False

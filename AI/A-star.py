cols = 4
rows = 4
grid = []

class Spot:
    def __init__(self):
        self.f = 0
        self.g = 0
        self.h = 0
    def __repr__(self):
        string = '(%d,%d,%d)' % (self.f,self.g,self.h)
        return string
        
        

def set_grid():
    for i in range(cols):
        my_row = []
        for i in range(rows):
            my_row.append(i)
        grid.append(my_row)
    for i in range(cols):
        for j in range(rows):
            grid[i][j] = Spot()
        print('done')
           
    
set_grid()
print(grid[0][3])
print('Git Integration worked')

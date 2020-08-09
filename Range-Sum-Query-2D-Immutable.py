class NumMatrix:
    '''
    [2:00] Goal is to find the sum of all numbers given the area of a rectangle
    
    Queries have to be fast
    Matrix given
    
    Naive solution
    res = 0
    - for i in range (row1, row2):
          for j in range(col1, col2):
              res += matrix[i][j]
    
    Alternate solution:
    I think it would help if we precompute the solution
    and sum it up and shave off unecessary computations
    Use prefix sum
    
    1, 2, 0, 1, 5 = 9
    1, 3, 3, 4, 9
    
    ^ This solution works well when the area of rectangle is large
    Edge case:
    - Same row and col - What to do?
    [8:00]: Trying out naive solution
    - Check if out of bounds
    - Invalid matrix
    [18:00]: Coded naive solution
    [19:00]: Working solution
    [20:00]: Looked at solution - Caching approach
    Basically, cache the area of the square starting fom (0, 0)
    
    If matrix looks like this
    
    W             X

    r1,c1    r1,c2  
        A----B
        |    |
        |    | 
        C----D
    r2,c1     r2,c2
    
    Y             Z
    
    A = (row1, col1)
    D = (row2, col2)
    For each index (i, j), dp[i][j] is the area of the shape
    from (0, 0) to [i, j]
    To compute the area, ABCD
    Area(ABCD) = Area(W, D) - Area(WB) - Area(WC) + Area(W, A)
    = self.dp[row2][col2] - self.dp[row1][col2] - self.dp[row2][col1] + self.dp[row1][col1]
    
    
    [24:00]: Started coding __init__()
    Felt stuck getting formula
    [39:00]: ended coding __init__()
    
    [40:00]: Starting sum region
    [50:00]: Wrote buggy code
    '''

    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            self.matrix = None
            return None
        
        self.row = len(matrix)
        self.col = len(matrix[0])
        
        self.dp = [[0 for _ in range(self.row + 1)] for _ in range(self.col)]
        
        for r in range(self.row):
            for c in range(self.col):
                if r == 0:
                    if c == 0:
                        self.dp[r][c] = matrix[r][c]
                    else:
                        self.dp[r][c] = self.dp[r][c-1] + matrix[r][c]
                elif c == 0:
                    if r == 0:
                        self.dp[r][c] = matrix[r][c]
                    else:
                        self.dp[r][c] = self.dp[r-1][c] + matrix[r][c]
                else:
                    self.dp[r][c] = self.dp[r-1][c] + self.dp[r][c-1] + matrix[r][c] - self.dp[r-1][c-1]
        for r in self.dp:
            print(r)
                    
        '''       
        self.matrix = matrix
        self.row = len(matrix)
        self.col = len(matrix[0])
        
        dp = [[0 for _ in range(self.row + 1)] for _ in range(self.col)]
        for r in range(self.row):
            for c in range(self.col):
                dp[r][c + 1] = dp[r][c] + matrix[r][c]
               ''' 

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        #check out of bounds
        if row1 == row2 and col1 == col2:
            return self.dp[row1][col1]
        if not (0 <= row1 < self.row and 
               0 <= row2 < self.row and
               0 <= col1 < self.col and
               0 <= col2 < self.col):
                return None
            
        return self.dp[row2][col2] - self.dp[row1-1][col2] - self.dp[row2][col1-1] + self.dp[row1-1][col1-1]
        
        
        '''if row1 == row2 and col1 == col2:
            return self.matrix[row1][col1]
        
        #check if out of bounds
        if not (0 <= row1 < self.row and 
               0 <= row2 < self.row and
               0 <= col1 < self.col and
               0 <= col2 < self.col):
                return None
            
        res = 0        
        for i in range(row1, row2 + 1):
            for j in range(col1, col2 + 1):
                res += self.matrix[i][j]
                
        return res'''
                
            



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

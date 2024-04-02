import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(self.w):
        """
        Creates a self.w x self.w identity matrix.
        """
        I = zeroes(self.w, self.w)
        for i in range(self.w):
            I.g[i][i] = 1.0
        return I

class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    def rank(self):
        '''Reduce the matrix a to the row echelon form.'''
        i = 0
        j = 0
        numSwaps = 0
        while i < self.h and j < self.w:
            maxElem = abs(self.grid[i, j])
            maxIdx = i
            for k in range(i+1, self.h):
                if abs(self.grid[k, j]) >= maxElem:
                    maxElem = abs(self.grid[k, j])
                    maxIdx = k
            if maxElem <= 1e-8:
                j += 1
                continue
            assert abs(self.grid[maxIdx, j]) > 1e-8
            if maxIdx != i:
                self.grid[(i, maxIdx), :] = self.grid[(maxIdx, i), :]    
                numSwaps += 1
            assert abs(self.grid[i, j]) > 1e-8

            r = self.grid[i, j]
            for k in range(i+1, self.h):
                coeff = self.grid[k, j]/r
                self.grid[k] -= self.grid[i]*coeff
            i += 1
            j += 1

        rank = i
        return rank
    
    def det(self):
        '''Reduce the matrix a to the row echelon form.'''
        i = 0
        j = 0
        numSwaps = 0
        while i < self.h and j < self.w:
            maxElem = abs(self.grid[i, j])
            maxIdx = i
            for k in range(i+1, self.h):
                if abs(self.grid[k, j]) >= maxElem:
                    maxElem = abs(self.grid[k, j])
                    maxIdx = k
            if maxElem <= 1e-8:
                j += 1
                continue
            assert abs(self.grid[maxIdx, j]) > 1e-8
            if maxIdx != i:
                self.grid[(i, maxIdx), :] = self.grid[(maxIdx, i), :]    
                numSwaps += 1
            assert abs(self.grid[i, j]) > 1e-8

            r = self.grid[i, j]
            for k in range(i+1, self.h):
                coeff = self.grid[k, j]/r
                self.grid[k] -= self.grid[i]*coeff
            i += 1
            j += 1

        if self.h != self.w:
            raise Exception("Matrix is not square, determinant undefined")
        elif i < self.h:
            det = 0.
        else:
            det = self.grid[0, 0]
            for k in range(1, self.h):
                det *= self.grid[k, k]
            if numSwaps%2 != 0:
                det = -det
        return det
    
    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        inverse =[]
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")
        if self.h == 1:
            inverse.append([1/self.g[0][0]])
        elif self.h == 2:
            if self.determinant() == 0:
                raise ValueError("Cannot find the inverse if determinant is 0")
            else:
                a = self.g[0][0]
                b = self.g[0][1]
                c = self.g[1][0]
                d = self.g[1][1]

                factor = 1 /(a * d - b * c)


                inverse = [[d, -b],[-c, a]]

                for i in range(len(inverse)):
                    for j in range(len(inverse[0])):
                        inverse[i][j] = factor * inverse[i][j]
        return Matrix(inverse)
    
    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        matrix_transpose = []
    # Loop through columns on outside loop
        for c in range(self.w):
            new_row = []
        # Loop through columns on inner loop
            for r in range(self.h):
            # Column values will be filled by what were each row before
                new_row.append(self.g[r][c])
            matrix_transpose.append(new_row)
    
        return Matrix(matrix_transpose)

    def is_square(self):
        return self.h == self.w

    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\self.w"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError,"Matrices can only be added if the dimensions are the same") 
            # initialize matrix to hold the results
        matrixSum = []
    
    # matrix to hold a row for appending sums of each element
        row = []
    
    # For loop within a for loop to iterate over the matrices
        for r in range(self.h):
            row = [] # reset the list
            for c in range(self.w):
                row.append(self.g[r][c] + other.g[r][c]) # add the matrices
            matrixSum.append(row)
    
        return Matrix(matrixSum)

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        return Matrix([[-self.g[row][col] for row in range(self.h)] for col in range(self.w)])

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        matrixSub = []
    
    # matrix to hold a row for appending sums of each element
        row = []
    
    # For loop within a for loop to iterate over the matrices
        for r in range(self.h):
            row = [] # reset the list
            for c in range(self.w):
                row.append(self.g[r][c] - other.g[r][c]) # add the matrices
            matrixSub.append(row)
    
        return Matrix(matrixSub)
        
    def __mul__(self, other):
        
        def dot_product(v1, v2):
            return sum([x1*x2 for x1,x2 in zip(v1,v2)])

        result = zeroes(self.h, other.w)
        other_T = other.T()
        for i in range(self.h):
            for j in range(other_T.h):
                result[i][j] = dot_product(self.g[i], other_T[j])
        return result
        
    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            pass
        scalar_mul = []
        for i in range(self.h):
            row =[]
            for j in range(self.w):
                row.append(other*self.g[i][j])
            scalar_mul.append(row)
        return Matrix(scalar_mul)
# from array import array
#TODO: class is not generic. only works with int. Make class work with all numerical types
#TODO: add type annotations to every bit of this code
from numbers import Number
from random import randrange, randint, random


class Matrix(object):
    """
    A class representation of matrix data structure. 
    Common operations of a matrix object are demonstrated below.
    
    >>> mat = Matrix(3, 3)
    >>> print(mat)
    [0, 0, 0]
    [0, 0, 0]
    [0, 0, 0]   
    
    mat[2][2] = 34
    mat[0][0] = 20
    mat[0][1] = 10

    >>> print(mat)
    [20, 10, 0]
    [0, 0, 0]
    [0, 0, 34]

    >>> mat1 = Matrix.randomMat(3, 3, 100, 200)
    >>> print(mat1)
    [168, 169, 105]
    [152, 100, 162]
    [139, 116, 185]

    >>> mat2 = Matrix.identity(2)
    >>> print(mat2)
    [1, 0]
    [0, 1]
    

    >>> mat3 = Matrix.identity(7)
    >>> print(mat3)
    [1, 0, 0, 0, 0, 0, 0]
    [0, 1, 0, 0, 0, 0, 0]
    [0, 0, 1, 0, 0, 0, 0]
    [0, 0, 0, 1, 0, 0, 0]
    [0, 0, 0, 0, 1, 0, 0]
    [0, 0, 0, 0, 0, 1, 0]
    [0, 0, 0, 0, 0, 0, 1]
        
    """
    
    def __init__(self, rows: int, columns: int, fill_value: Number = 0):
        "n and m are of int type representing the row length and column length respectively."
        #error-check for size of matrix. Size must be integers
        if isinstance(rows, int) and isinstance(columns, int):
            self._rows = rows
            self._columns = columns
        else:
            raise TypeError("Matrix row and column length must be integers!")

        if isinstance(fill_value, Number):
            self._matrix = [[fill_value] * self._columns for _ in range(self._rows)]
        else:
            raise TypeError("Matrix elements must be of numeric type!")
       

    def __setitem__(self, idx: int, value: list):
        if isinstance(value, list) and isinstance(idx, int):
            self._matrix[idx] = value
        else:
            raise TypeError("A matrix object can only contain lists of numbers")
        return

    def __getitem__(self, idx: int):
        if isinstance(idx, int):
            return self._matrix[idx]
        else:
            raise TypeError("Matrix index must be an integer")


    def __repr__(self):
        '''Print the matrix row after row.'''
        prt = ""
        for row in self._matrix:
            prt += str(row)
            prt += "\n"
        return prt.rstrip()

    def __contains__(self, value: int):
        if isinstance(value, int):
            for row in self._matrix:
                for element in row:
                    if element == value:
                        return True
                    else:
                        pass
            return False
        else:
            raise TypeError("checking value must be numerical")

    def __add__(self, other: "Matrix") -> "Matrix":
        "Matrix addtion"
        raise NotImplementedError

    def __mul__(self, other: "Matrix") -> "Matrix":
        "Matrix multiplication"
        raise NotImplementedError

    def __sub__(self, other: "Matrix") -> "Matrix":
        "Matrix subtraction"
        raise NotImplementedError

    def __div__(self, other: "Matrix") -> "Matrix":
        "Matrix division"
        raise NotImplementedError

    def __eq__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError("A Matrix can only be compared with another Matrix")
        return self._matrix == other._matrix

    def __ne__(self, other):
        return not self == other

    def __neg__(self):
        return self * -1

    @classmethod
    def identity(cls, n: int):
        """ 
        Creates a n x n identity matrix.
        """
        newMatrix = Matrix(n, n)

        i = 0
        for row in newMatrix:
            row[i] = 1
            i += 1

        return newMatrix


    @classmethod
    def randomMat(cls,row_size: int, column_size: int, lower: Number = 0, upper: Number = 10):
        '''matrix with random elements of the same numerical type'''
        # if isinstance(row_size, int) and isinstance(column_size, int):
        newMatrix = Matrix(row_size, column_size)    
        for row in newMatrix:
            for i in range(newMatrix._columns):
                row[i] = randint(lower, upper)
        return newMatrix


if __name__ == "__main__":
        
    mat = Matrix(3, 3)
    print(mat)

    print()
    mat[2][2] = 34
    mat[0][0] = 20
    mat[0][1] = 10

    print(mat)
    print()

    mat1 = Matrix.randomMat(3, 3, 100, 200)
    print(mat1)
    print()

    mat2 = Matrix.identity(2)
    print(mat2)
    print()

    mat3 = Matrix.identity(7)
    print(mat3)
    print()
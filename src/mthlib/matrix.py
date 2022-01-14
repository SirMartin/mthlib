#from array import array




class Matrix(object):
    
    def __init__(self, rows: int, columns: int):
        self._rows = rows
        self._columns = columns
        self._matrix = []

        for i in range(rows):
            self._matrix.append([]) 

        for row in self._matrix:
            for i in range(columns):
                row.append(0) 

    def __setitem__(self, idx, value):
        if isinstance(value, list):
            self.matrix[idx] = value
        else:
            raise TypeError("A matrix object can only contain lists of numbers")
        return

    def __getitem__(self, idx: int):
        if isinstance(idx, int):
            return self._rows[idx]
        else:
            raise TypeError("Matrix index must be an integer")


    def __repr__(self):
        '''Print the matrix row after row.'''
        prt = ""
        for row in self._matrix:
            prt += str(row)
            prt += "\n"
        return prt.rstrip()



mat = Matrix(3, 3)
print(mat)

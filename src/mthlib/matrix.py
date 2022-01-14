#from array import array




class Matrix(object):
    
    def __init__(self, rows: int, columns: int, fill_value: int = 0):
        self._rows = rows
        self._columns = columns
        self._matrix = [[fill_value] * columns for _ in range(rows)]

        # for i in range(rows):
        #     self._matrix.append([]) 

        # for row in self._matrix:
        #     for i in range(columns):
        #         row.append(0) 

    def __setitem__(self, idx, value):
        if isinstance(value, list):
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

    def __contains__(self, value):
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

    # @classmethod
    # def makeId(cls, m):
    #     """ Make identity matrix of rank (mxm) """

    #     rows = [[0]*m for x in range(m)]
    #     idx = 0
        
    #     for row in rows:
    #         row[idx] = 1
    #         idx += 1

    #     return cls.fromList(rows)



mat = Matrix(3, 3, 0)
print(mat)
print(mat[2][2])
mat[2][2] = 34
# print(mat.makeId(3))
print(mat)
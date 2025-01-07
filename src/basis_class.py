import numpy as np
class Basis():

    def __init__(self, dimensions):
        if (dimensions % 2 != 0) or (dimensions <=0) or (type(dimensions) is not int):
            raise Exception("Only positive even integers allowed!")
        else:
            self._dimensions = dimensions

    @property
    def dimension(self):
        return self._dimensions

    
    def create_basis_vectors(self, index):
        
        if index < 0: 
            raise Exception("Index can't be less than zero!")
        else:
            vector = np.zeros(self._dimensions)
            vector[index] = 1
        
        
        return vector
    



    


import numpy as np
from scipy.sparse import lil_matrix

class Dissipation_Tensor():

    def __init__(self, size, kossakowski_type):
        self._size = size
        self._tensor = [ 
            [lil_matrix((size, size), dtype=complex) for _ in range(size)]
        for _ in range(size)
    ]
        if kossakowski_type.lower() == "general":
            self._kossakowski_type =  kossakowski_type.lower()
        elif kossakowski_type.lower() == "symmetric":
            self._kossakowski_type =  kossakowski_type.lower()
        else:
            raise Exception("Kossakowski matrix type must be \"general\" or \"symmetric\"")  
    
    @property
    def size(self):
        return self._size
    
    @property 
    def tensor(self):
        return self._tensor
    
    @property 
    def kossakowski_type(self):
        return self._kossakowski_type
    







        
import numpy as np
from scipy.sparse import lil_matrix

class Dissipation_Tensor():

    def __init__(self, size):
        self._size = size
        self._tensor = [ 
            [lil_matrix((size, size), dtype=complex) for _ in range(size)]
        for _ in range(size)
    ]
    
    @property
    def size(self):
        return self._size
    
    @property 
    def tensor(self):
        return self._tensor
    
    





        
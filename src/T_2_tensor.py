import numpy as np
import sys
sys.path.append('../src')
from scipy.sparse import lil_matrix
from dissipation_tensor import Dissipation_Tensor

class T_2_Tensor():


    def __init__(self, d_tensor):
        # print(Dissipation_Tensor, "this was printed")
        self._validation_dissipation_tensor(d_tensor)    
        self._type = d_tensor.kossakowski_type
        if self._type == "general":
            self._shape = (d_tensor._size**2, d_tensor._size**2)
        if self._type == "symmetric":
            symmetric_dof = d_tensor._size + (d_tensor._size**2 - d_tensor._size)/2
            self._shape = (d_tensor._size**2, symmetric_dof )
    
    @property
    def type(self):
        return self._type
    
    @property
    def shape(self):
        return self._shape
    

    def _validation_dissipation_tensor(self,d_tensor):
        #if not isinstance(d_tensor, Dissipation_Tensor)
        if not hasattr(d_tensor, "specific_atribute"):
            raise TypeError("d_tensor must be an instance of Dissipation_Tensor")









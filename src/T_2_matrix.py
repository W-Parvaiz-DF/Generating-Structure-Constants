import numpy as np
import sys
sys.path.append('../src')
from scipy.sparse import lil_matrix
from dissipation_tensor import Dissipation_Tensor

class T_2_Matrix():


    def __init__(self, d_tensor):
        # print(Dissipation_Tensor, "this was printed")
        self._validation_dissipation_tensor(d_tensor)    
        self.dissipation_tensor = d_tensor.tensor
        self._type = d_tensor.kossakowski_type
        if self._type == "general":
            self._shape = (d_tensor._size**2, d_tensor._size**2)
            self._matrix = self.build_general_matrix()
        if self._type == "symmetric":
            symmetric_dof = d_tensor._size + (d_tensor._size**2 - d_tensor._size)/2
            self._shape = (d_tensor._size**2, symmetric_dof)
    
    @property
    def type(self):
        return self._type
    
    @property
    def shape(self):
        return self._shape
    
    @property
    def matrix(self):
        return self._matrix
    
    

    def _validation_dissipation_tensor(self,d_tensor):
        #if not isinstance(d_tensor, Dissipation_Tensor)
        if not hasattr(d_tensor, "specific_atribute"):
            raise TypeError("d_tensor must be an instance of Dissipation_Tensor")
    
    def build_general_matrix(self):
        output = lil_matrix(self.shape, dtype=complex)

        for T_index_1 in range(self.shape[0]):
            D_index_1, D_index_2 = divmod(T_index_1, int(np.sqrt(self.shape[0])))
            for T_index_2 in range(self.shape[0]):
                D_index_3, D_index_4 = divmod(T_index_2, int(np.sqrt(self.shape[0])))
                output[T_index_1, T_index_2] = -self.dissipation_tensor[D_index_1][D_index_2][D_index_3, D_index_4]
        return output











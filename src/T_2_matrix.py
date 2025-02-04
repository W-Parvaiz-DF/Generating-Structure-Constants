import numpy as np
import sys
sys.path.append('../src')
from scipy.sparse import lil_matrix
from dissipation_tensor import Dissipation_Tensor
from utils import symmetric_index_mapping

class T_2_Matrix():



    def __init__(self, d_tensor):
        # print(Dissipation_Tensor, "this was printed")
        self._validation_dissipation_tensor(d_tensor)    
        self.dissipation_tensor = d_tensor.tensor
        self._type = d_tensor.kossakowski_type
        self._size = d_tensor._size
        self.symmetric_map = symmetric_index_mapping(self.size) 
        if self._type == "general":
            self._shape = (d_tensor._size**2, d_tensor._size**2)
            self._matrix = self.build_general_matrix()
        if self._type == "symmetric":
            symmetric_dof = int(d_tensor._size + (d_tensor._size**2 - d_tensor._size)/2)
            self._shape = (d_tensor._size**2, symmetric_dof)
            self._matrix = self.build_symmetric_matrix()
        
        self._rank = np.linalg.matrix_rank(self.matrix.toarray())
            
        
    
    
    @property
    def type(self):
        return self._type
    
    @property
    def shape(self):
        return self._shape
    
    @property
    def matrix(self):
        return self._matrix
    
    @property
    def rank(self):
        return self._rank
    
    @property
    def size(self):
        return self._size
    

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

    def build_symmetric_matrix(self):
        reduced_symmetric_matrix = lil_matrix(self.shape)


        for row in range(self.size):
            for column in range(self.size):
                original_index = row*self.size + column
                reduced_column_index = self.symmetric_map[(row, column)]
                D_index_1, D_index_2 = divmod(original_index, self.size)
                for reduced_row_index in range(self.size**2):
                    D_index_3, D_index_4 = divmod(reduced_row_index, self.size)
                    reduced_symmetric_matrix[reduced_row_index, reduced_column_index] -=self.dissipation_tensor[D_index_1][D_index_2][D_index_3, D_index_4]

        return reduced_symmetric_matrix


    def isfullrank(self):
        min_value = min(self.shape)
        return self.rank == min_value








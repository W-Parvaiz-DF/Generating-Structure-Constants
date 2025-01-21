import numpy as np
from scipy.sparse import lil_matrix

class Dissipation_Tensor():

    def __init__(self, kossakowski_type, complex_structure_constants):

        if kossakowski_type.lower() == "general":
            self._kossakowski_type =  kossakowski_type.lower()
        elif kossakowski_type.lower() == "symmetric":
            self._kossakowski_type =  kossakowski_type.lower()
        else:
            raise Exception("Kossakowski matrix type must be \"general\" or \"symmetric\"")  
        
        
        self.validate_complex_structure_constants(complex_structure_constants)
        self._complex_structure_constants = complex_structure_constants
        self._size = len(complex_structure_constants) 
        self._antisymmetric_structure_constants = np.real(complex_structure_constants)
        
        self._tensor =  self.build_general_tensor()

    @property 
    def tensor(self):
        return self._tensor
    
    @property 
    def kossakowski_type(self):
        return self._kossakowski_type
    
    def validate_complex_structure_constants(self, complex_structure_constants):

        if not isinstance(complex_structure_constants, list):
            raise TypeError("complex_structure_constants should be a list of n matrices with dimension n x n")
        
        size = len(complex_structure_constants)
        if size == 0:
            raise ValueError("complex_structure_constants cannot be an empty list")
        
        for matrix in complex_structure_constants:
            if not hasattr(matrix, "shape"):
                raise TypeError("complex_structure_constants must be a list of matrices")
            
            if matrix.shape != (size, size):
                raise ValueError(f"All matrices in complex_structure_constants must have dimensions ({size}, {size}). "
                                 f"Found a matrix with dimensions {matrix.shape}.")
        
    
    def build_general_tensor(self):
        tensor = [ 
                        [lil_matrix((self._size, self._size), dtype=complex) for _ in range(self._size)]
                        for _ in range(self._size)
                        ]
        
        for index_1 in range(self._size):
            for index_2 in range(self._size):
                for index_3 in range(self._size):
                    for index_4 in range(self._size):
                        value = 0
                        for summed_index in range(self._size):
                            value += (
                                (
                                self._complex_structure_constants[index_3][summed_index,index_2]*
                                self._antisymmetric_structure_constants[index_1][index_4, summed_index]
                                ) +
                                 (
                                  np.conjugate(self._complex_structure_constants[index_4][summed_index, index_2])*
                                  self._antisymmetric_structure_constants[index_1][index_3, summed_index]   
                                 ))
                        
                        tensor[index_1][index_2][index_3, index_4] = 0.25*value                               
        return  tensor

    







        
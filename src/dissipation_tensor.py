import numpy as np
from scipy.sparse import lil_matrix
import time

class Dissipation_Tensor():

    def __init__(self, kossakowski_type, complex_structure_constants, antisymmetric_structure_constants):

        self.validate_complex_structure_constants(complex_structure_constants)
        self._complex_structure_constants = complex_structure_constants
        self._size = len(complex_structure_constants) 
        self.validate_complex_structure_constants(antisymmetric_structure_constants)
        self._antisymmetric_structure_constants = antisymmetric_structure_constants

        if kossakowski_type.lower() == "general":
            self._kossakowski_type =  kossakowski_type.lower()
            self._tensor =  self.build_general_tensor()
        elif kossakowski_type.lower() == "symmetric":
            self._kossakowski_type =  kossakowski_type.lower()
            self._tensor = self.build_symmetric_tensor()
        else:
            raise Exception("Kossakowski matrix type must be \"general\" or \"symmetric\"")  
        
        self.specific_atribute = 0


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
        size = self._size
        complex_structure_constants = self._complex_structure_constants
        antisymmetric_structure_constants = self._antisymmetric_structure_constants
        tensor = [[lil_matrix((size, size), dtype=complex) for _ in range(size)] for _ in range(size)]
        
        for index_1 in range(size):
            for index_2 in range(size):
                for index_3 in range(size):
                    for index_4 in range(size):
                        value = 0
                        for summed_index in range(size):
                            value += (
                                (
                                complex_structure_constants[index_3][summed_index,index_2]*
                                antisymmetric_structure_constants[index_1][index_4, summed_index]
                                ) +
                                 (
                                  np.conjugate(complex_structure_constants[index_4][summed_index, index_2])*
                                  antisymmetric_structure_constants[index_1][index_3, summed_index]   
                                 ))
                        
                        tensor[index_1][index_2][index_3, index_4] = 0.25*value                             
        return  tensor
    
    def build_symmetric_tensor(self):
        size = self._size
        antisymmetric_structure_constants = self._antisymmetric_structure_constants

        tensor = [[lil_matrix((size, size)) for _ in range(size)] for _ in range(size)]
        
        for index_1 in range(size):
            # print(f"index_1 {index_1}")
            for index_2 in range(size):
                # print(f"index_2 = {index_2}")
                for index_3 in range(size):
                    # print(f"index_3 = {index_3}")
                    for index_4 in range(size):
                        # print(f"index_4 = {index_4}")
                        value = 0
                        for summed_index in range(size):
                            # print(f"summed_index = {summed_index}")
                            # print(antisymmetric_structure_constants[index_1][index_4, summed_index])
                            # print(antisymmetric_structure_constants[index_2][index_3,summed_index])
                            value += (antisymmetric_structure_constants[index_1][index_4, summed_index])*(antisymmetric_structure_constants[index_2][index_3,summed_index]) 
                        
                        #if value != 0:
                            #print(f"value = {value}, j = {index_1}, k = {index_2}, l = {index_3}, m={index_4}")
                        
                        tensor[index_1][index_2][index_3, index_4] = 0.5*value                             
        return  tensor


    
    

    







        
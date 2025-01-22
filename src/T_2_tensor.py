import numpy as np
from scipy.sparse import lil_matrix

class T_2_Tensor():

    def __init__(self, dissipation_tensor):
       self._validation_of_dissipation_tensor(dissipation_tensor)
       self._size = len(dissipation_tensor)**2
    
    @property
    def size(self):
        return self._size

    def _validation_of_dissipation_tensor(self, dissipation_tensor):

        if not isinstance(dissipation_tensor, list):
            raise TypeError("dissipation_tensor should be a list")

        outer_list_size = len(dissipation_tensor)
        if outer_list_size == 0:
            raise ValueError("dissipation_tensor cannot be empty")
        counter = -1
        for inner_list in dissipation_tensor:
            counter+=1
            if not isinstance(inner_list, list):
                raise TypeError(f"dissipation_tensor[{counter}] should be a list")
            
            if len(inner_list) != outer_list_size:
                raise ValueError(f"dissipation_tensor[{counter}] should have size {outer_list_size} not {len(inner_list)}")
            second_counter = -1
            for matrix in inner_list:
                second_counter += 1
                if not hasattr(matrix, "shape"):
                    raise  TypeError(f"dissipation_tensor[{counter}][{second_counter}] should have be a matrix")

                if matrix.shape != (outer_list_size, outer_list_size):
                    raise ValueError(f"dissipation_tensor[{counter}][{second_counter}] should have shape {(outer_list_size, outer_list_size)} not {matrix.shape}")










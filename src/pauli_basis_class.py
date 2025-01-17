import numpy as np
from .utils import commutator, anticommutator, find_matrix_mask

class Pauli_Basis():

    su_2_identity = np.eye(2)
    #change coeffs later
    su_2_pauli_x = np.array([[0,1],[1,0]])
    su_2_pauli_y = np.array([[0,-1j],[1j,0]])
    su_2_pauli_z = np.array([[1,0],[0,-1]])
    building_block_matrices = [
                                su_2_identity,
                                su_2_pauli_x,
                                su_2_pauli_y,
                                su_2_pauli_z
                                ]

    
    def __init__(self, dimension):
        
        if not (self.is_power_of_2(dimension)) :
            raise Exception("Must be a power of 2")
        
        self._dimension  = dimension
        self._basis = [
                    self.coefficient() * matrix for matrix in self.pauli_basis_matrices_without_coefficient()
                    ]

    @property
    def dimension(self):
        return self._dimension 
    
    @property
    def basis(self):
        return self._basis
    
    def is_power_of_2(self, x):
         return x > 0 and (x & (x - 1)) == 0
    
    def tensor_product_list(self, list_1, list_2):
        return[
            np.kron(list_1[index_1], list_2[index_2])
            for index_1 in range(len(list_1))
            for index_2 in range(len(list_2))                          
                                      ]
                
    def recursive_tensor_product_list(self, list_1, list_2, number_of_tensor_products):
        output = list_1
        for _ in range(number_of_tensor_products):
            output = self.tensor_product_list(output, list_2)
        return output
    
    def pauli_basis_matrices_without_coefficient(self):
        #This is without the coefficients
        if self.dimension == 2:
            output_list = self.building_block_matrices.copy()
            output_list.pop(0)
            return output_list
        else: 
            number_of_tensor_products = int(np.log2(self.dimension)) - 1
            output_list = self.recursive_tensor_product_list(list_1= self.building_block_matrices,
                                                        list_2= self.building_block_matrices,
                                                        number_of_tensor_products= number_of_tensor_products)
            output_list.pop(0)
            return output_list
            
    def coefficient(self):
        #just doing for one since should be consistent for all of them
        basis_matrix = self.pauli_basis_matrices_without_coefficient()[0]
        return np.sqrt(1/np.trace(np.dot(basis_matrix,basis_matrix)))

    def find_candidate_masks_from_basis(self, input_matrix_mask):
        
        if input_matrix_mask.dtype != bool:
            raise Exception("Input should be a matrix with boolean type elements!")

        candidate_indices = []

        for index in range(len(self.basis)):
            basis_mask = self.basis[index] !=0
            if np.array_equal(input_matrix_mask, basis_mask):
                candidate_indices.append(index)
        
        if len(candidate_indices) == 0:
            raise Exception("No candidate basis matrices found!")
        
        return candidate_indices

    def find_scale_factor_and_index(self, input_matrix, input_matrix_mask):

        #note here the scale factor is root(2)* what is given on wikipedia, because there they dont use normalisation       
 
        candidate_list = self.find_candidate_masks_from_basis(input_matrix_mask)
        scaling_factor = []
        index_list = []
        
        for index in candidate_list:
            all_scaling_factors = input_matrix[input_matrix_mask]/self.basis[index][input_matrix_mask]
            if np.allclose(all_scaling_factors, all_scaling_factors[0]):
                scaling_factor.append(all_scaling_factors[0])
                index_list.append(index)
        
        if len(scaling_factor) > 1:
            raise Exception("There should only be one candidate matrix here!")
        
        return scaling_factor[0], index_list[0]
        

            



            

    


  

    

            



    
    
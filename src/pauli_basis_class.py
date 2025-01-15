import numpy as np

class Pauli_Basis():

    su_2_identity = np.eye(2)
    su_2_pauli_x = 0.5*np.array([[0,1],[1,0]])
    su_2_pauli_y = 0.5*np.array([[0,-1j],[1j,0]])
    su_2_pauli_z = 0.5*np.array([[1,0],[0,-1]])
    building_block_matrices = [
                                su_2_identity,
                                su_2_pauli_x,
                                su_2_pauli_y,
                                su_2_pauli_z
                                ]

    
    def __init__(self, dimension):
        if not (self.is_power_of_2(dimension)) :
            raise Exception("Must be a power of 2")
        else:
            self._dimension  = dimension

    @property
    def dimension(self):
        return self._dimension 
    
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
    
    def pauli_basis_matrices(self):
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
            
        

    

            



    
    
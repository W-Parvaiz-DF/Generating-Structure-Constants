import numpy as np
class Basis():

    def __init__(self, dimensions):
        
        if  dimensions <= 0:
            raise Exception("Must be a positive integer")

        self._dimensions = dimensions
        
        self._basis_matrices = self.full_general_matrix_basis()

    @property
    def dimension(self):
        return self._dimensions
    
    @property
    def basis_matrices(self):
        return self._basis_matrices

    def create_basis_vectors(self, index):
        if index < 0: 
            raise Exception("Index can't be less than zero!")

        vector = np.zeros(self.dimension)
        vector[index] = 1
        return vector
    
    def create_single_symmetric_basis_matrix(self, first_index, second_index):
        
        if second_index >= first_index:
            raise Exception("first_index must be larger than second_index!")

        first_index_vector = self.create_basis_vectors(first_index)
        second_index_vector = self.create_basis_vectors(second_index)
        matrix = 0.5*(np.outer(second_index_vector, first_index_vector) + np.outer(first_index_vector, second_index_vector))
        return matrix
        
    def create_single_antisymmetric_basis_matrix(self, first_index, second_index):
        
        if second_index >= first_index:
            raise Exception("first_index must be larger than second_index!")
        
        first_index_vector = self.create_basis_vectors(first_index)
        second_index_vector = self.create_basis_vectors(second_index)
        matrix = -0.5j*(np.outer(second_index_vector, first_index_vector) - np.outer(first_index_vector, second_index_vector))
        return matrix

    def create_single_diagonal_basis_matrix(self, index):

        if index <= 0:
            raise Exception("Index must be greater than zero!")
        
        coeff = 1/np.sqrt(2*(index+1)*index)
        temp_matrix = np.zeros((self.dimension, self.dimension))

        for inner_index in range(index):
            inner_index_vector = self.create_basis_vectors(inner_index)
            temp_matrix += np.outer(inner_index_vector, inner_index_vector)
        
        index_vector = self.create_basis_vectors(index)
        matrix = temp_matrix - index*np.outer(index_vector, index_vector)
        return coeff*matrix 


    def create_all_symmetric_basis_matrices(self):
        
        return [
            self.create_single_symmetric_basis_matrix(first_index=first_index, second_index=second_index)
            for first_index in range(1, self.dimension)
            for second_index in range(first_index)
        ]

    def create_all_antisymmetric_basis_matrices(self):
        
        return [
            self.create_single_antisymmetric_basis_matrix(first_index=first_index, second_index=second_index)
            for first_index in range(1, self.dimension)
            for second_index in range(first_index)
        ]
    
    def create_all_diagonal_basis_matrices(self):

        return [
            self.create_single_diagonal_basis_matrix(index=index)
            for index in range(1,self.dimension)
        ]
       
    def full_general_matrix_basis(self):
        return self.create_all_symmetric_basis_matrices() + self.create_all_antisymmetric_basis_matrices() + self.create_all_diagonal_basis_matrices()

   


    
            


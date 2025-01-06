import numpy
class Basis():

    def __init__(self, dimensions):
        if (dimensions % 2 != 0) or (dimensions <=0) or (type(dimensions) is not int):
            raise Exception("Only positive even integers allowed!")
        else:
            self._dimensions = dimensions

    @property
    def dimension(self):
        return self._dimensions

    

#raise Exception("Sorry, no numbers below zero")
#if not type(x) is int:
  #raise TypeError("Only integers are allowed")

    


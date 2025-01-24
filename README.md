# README



# Notes for self

- Remember the indexing is from 0 to n-1 rather than in the paper which is 1 to n. 
- Currently when building the basis can only do this for 2**7 (7 qubits systems) so in the future try to make the basis sparse too instead of regular numpy arrays.
- For some reason, the code for building the D-tensor for n = 4 is taking 16 seconds to run however in the non-class version the nested for loops only took 4 seconds to run (not to do with the fact that I dont use a bijective map anymore). Find out where the issue is. 
  

- T_2 tensor validation didnt work when using isInstance(), was likely the way dissipation_tensor was being imported, may need to resolve using setup.py however, I did a cheap fix. 




  
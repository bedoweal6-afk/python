import numpy as np
A=np.array([[1,2,3],[4,5,6]])
B=np.array([[9,10,1],[3,4,5]])

print("A + B =", A + B)       
print("A - B =", A - B)         
print("A * B =", A * B)  
print("A / B =", A / B)
print("Mean of A:", np.mean(A))
print("Max of A:", np.max(A))
print("Min of A:", np.min(A))
print("Sum of A:",np.sum(A))
print("Reshaped A (6x1):\n", A.reshape(6, 1)) 

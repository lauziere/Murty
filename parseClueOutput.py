
import numpy as np
from scipy.optimize import linear_sum_assignment

def parseClueOutput(mat):
    
    rows, cols = linear_sum_assignment(mat)
    n = rows.shape[0]
    
    tmp = np.zeros((n,n),'int')
    tmp[rows,cols]=1
    cost = mat[rows,cols].sum()
    
    return [tmp, cost]

def parseClueOutputInf(mat):

    rows, cols = linear_sum_assignment(mat)
    n = rows.shape[0]
    
    tmp = np.zeros((n,n),'int')
    tmp[rows,cols]=1
    cost = mat[rows,cols].sum()
    
    return [tmp, cost]
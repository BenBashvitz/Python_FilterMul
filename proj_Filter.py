# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 16:29:58 2020

@author: bashv
"""

import numpy as np

def FilterMul(mat, fil):
    s = (mat.shape[0]-2,mat.shape[1]-2)
    c = np.zeros(s)
    for i in range(mat.shape[0]-2):
        for j in range(mat.shape[1]-2):
            c[i,j]= mat[i,j]*fil[0,0]+mat[i,j+1]*fil[0,1]+mat[i,j+2]*fil[0,2]
            c[i,j] += mat[i+1,j]*fil[1,0]+mat[i+1,j+1]*fil[1,1]+mat[i+1,j+2]*fil[1,2]
            c[i,j] += mat[i+2,j]*fil[2,0]+mat[i+2,j+1]*fil[2,1]+mat[i+2,j+2]*fil[2,2]
    return c
            



def main():
    mat = np.random.rand(8,8)
    for a in mat:
        a *= 5
        i=1
    while(mat.shape[0] > 3):
        print(i)
        fil = np.random.rand(3,3)
        mat = FilterMul(mat,fil)
    print(mat)
    
    
if __name__ == "__main__":
    main()
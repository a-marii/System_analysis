import numpy as np
import json

def task(str1):
    array = json.loads(str1)
    array=np.transpose(array)
    A = np.zeros((3,3))
    B= np.zeros((3,3))
    C = np.zeros((3,3))
    for i in range(len(array)):
        for j in range(len(array)):
            if array[i][0]<array[j][0]:
                A[i][j]=1
            elif array[i][0]==array[j][0]:
                A[i][j]=0.5
            else:
                A[i][j]=0
    for i in range(len(array)):
        for j in range(len(array)):
            if array[i][1]<array[j][1]:
                B[i][j]=1
            elif array[i][1]==array[j][1]:
                B[i][j]=0.5
            else:
                B[i][j]=0
    for i in range(len(array)):
        for j in range(len(array)):
            if array[i][2]<array[j][2]:
                C[i][j]=1
            elif array[i][2]==array[j][2]:
                C[i][j]=0.5
            else:
                C[i][j]=0
    result= np.zeros((3,3))
    for i in range(len(array)):
        for j in range(len(array)):
            result[i][j]=A[i][j]/3+B[i][j]/3+C[i][j]/3
    k_0=[1,1,1]
    k_1=[1/3,1/3,1/3]
    while max(abs(np.array(k_1)- np.array(k_0)))>0.001:
        k_0=k_1
        y_0=np.dot(result,k_0)
        lambda_0=np.dot([1,1,1],y_0)
        k_1=1/lambda_0*y_0
    k=[round(i,3) for i in k_1]
    return k


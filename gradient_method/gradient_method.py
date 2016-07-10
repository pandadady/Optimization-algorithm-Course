# -*- coding:  utf-8 -*
"""
This module is used to learn gradient method
Authors: shiduo(shiduo@baidu.com)
Date:2016-7-9
"""
def SGD(dataMatrix, classLabels, numIter=150):
    m,n = shape(dataMatrix)
    weights = ones(n)   #initialize to all ones
    for j in range(numIter):
        dataIndex = range(m)
        for i in range(m):
            alpha = 4/(1.0+j+i)+0.0001    #apha decreases with iteration, does not 
            randIndex = int(random.uniform(0,len(dataIndex)))
            h = sigmoid(sum(dataMatrix[randIndex]*weights))
            error = classLabels[randIndex] - h
            weights = weights + alpha * error * dataMatrix[randIndex]
            del(dataIndex[randIndex])
    return weights

def BGD(dataMatIn, classLabels):
    dataMatrix = mat(dataMatIn)            
    labelMat = mat(classLabels).transpose() 
    m,n = shape(dataMatrix)
    print m,n
    alpha = 0.001
    maxCycles = 500
    weights = ones((n,1))
    for k in range(maxCycles):             
        h = sigmoid(dataMatrix*weights)  
        error = (labelMat - h)             
        weights = weights + alpha * dataMatrix.transpose()* error 
    return array(weights.T)[0].tolist()

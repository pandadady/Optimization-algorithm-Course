# -*- coding:  utf-8 -*
"""
This module is used to learn newton algorithm
Authors: shiduo(shiduo@baidu.com)
Date:2016-7-10
"""
def newtonMethod(dataMat, labelMat, iterNum=5):
    
    dataMat=mat(dataMat)
    m,n=shape(dataMat)
    theta = zeros((1,n))
    while(iterNum):
        gradientSum = zeros((1,n))
        hessianMatSum = zeros((n,n))
        for i in range(m):
            hypothesis = sigmoid(sum(theta*dataMat[i,].T))
            error = labelMat[i] - hypothesis
            gradient = dataMat[i,]*error/m
            gradientSum = gradientSum+gradient
            hessian = (-dataMat[i,].T*dataMat[i,]*(1-hypothesis)*hypothesis)
            for j in range(n):
                hessianMatSum[j] = hessianMatSum[j]+hessian[j]
        try:
            hessianMatInv = mat(hessianMatSum).I
        except:
            continue
        theta=theta-gradientSum*hessianMatInv

        iterNum -= 1
    return array(theta)[0].tolist()

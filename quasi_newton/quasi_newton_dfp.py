# -*- coding:  utf-8 -*
"""
This module is used to learn quasi newton algorithm
Authors: shiduo(shiduo@baidu.com)
Date:2016-6-9
"""

from numpy import *
def calc_gradient(weight,dataMat,labelMat,m):
    hypothesis = sigmoid(sum(weight*dataMat.T))
    error = labelMat - hypothesis
    gradient = dataMat*error/m
    return gradient
def dfp(dataMat, labelMat, iterNum=5):
    dataMat=mat(dataMat)
    m,n=shape(dataMat)
    weight0 = zeros((1,n))
    H0=eye(n)
    while(iterNum):
        for i in range(m):
            gradient=calc_gradient(weight0,dataMat[i,],labelMat[i],m)
            weight1=weight0+gradient*H0
            S0=weight1-weight0
            y0=calc_gradient(weight1,dataMat[i,],labelMat[i],m)-calc_gradient(weight0,dataMat[i,],labelMat[i],m)
            try:
                M1=S0.T*S0*(S0.T*y0).I
    #             print H0*y0.T*y0*H0
    #             print y0.T*y0*H0
                M2=H0*y0.T*y0*H0*(H0*y0.T*y0).I
    #             print M2
            except:
                continue
            H1=H0+M1+M2
            weight0=weight1
            H0=H1
        iterNum-=1
    return array(weight1)[0].tolist()

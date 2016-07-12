# -*- coding:  utf-8 -*
"""
This module is used to learn quasi newton algorithm
Authors: shiduo(shiduo@baidu.com)
Date:2016-7-13
"""

from numpy import *
def calc_gradient(weight,dataMat,labelMat,m):
    gradient=dot(sigmoid(dot(weight,dataMat.T))-labelMat,dataMat)
    return gradient
def get_alphA(weight,dataMat,labelMat,dk): 
    c=float("inf")
    t=weight
    for k in range(1,10):
        a=1.0/k**2
        weight = t + a * dk
        f= sum(dot(sigmoid(dot(weight,dataMat.T))-labelMat,dataMat))
        if abs(f)>c:
            break
        c=abs(f)
        alpha=a
    return alpha
def dfp(dataMat, labelMat, iterNum=3):
    dataMat=mat(dataMat)
    labelMat=mat(labelMat)
    m,n=shape(dataMat)
    weight0 = ones((1,n))
    H0=eye(n)
    for j in range(iterNum):
        gradient=calc_gradient(weight0,dataMat,labelMat,m)
        dk=-1*dot(gradient,H0)
        alpha=get_alphA(weight0,dataMat,labelMat,dk)
        weight1=weight0+alpha*dk
        S0=weight1-weight0
        y0=calc_gradient(weight1,dataMat,labelMat,m)-calc_gradient(weight0,dataMat,labelMat,m)
        M1=S0.T.dot(S0)/(S0.dot(y0.T))
        M2=H0.dot(y0.T).dot(y0).dot(H0)/(y0.dot(H0).dot(y0.T))* (-1)
        H1=H0+M1+M2
        weight0=weight1
        H0=H1
    return array(weight1)[0].tolist()

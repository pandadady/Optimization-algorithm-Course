#Newton method
##1.Summary
    
    The algorithm is found by the famous Newton, and is often used in th ML and DL.
    
    The convergence speed is faster then GD algorithm.
    
    
##2.Process
    
    Suppose the current purpose is to optimize an objective function J(), that is, to calculate the 
    
    maximum value or minimum value of function J(). The problem can be transformed into a problem of 
    
    solving the derivatives of J(), J'()= 0. So that the newton method can be used to solve the problem.
    
    The original function J(x) need to do the two order form Taylor expansion.
    
<img src="http://chart.googleapis.com/chart?cht=tx&chl=J(x%2B%5CDelta%20x)%3DJ(x)%2BJ'(x)%5CDelta%20x%2B%5Cfrac%7B1%7D%7B2%7DJ''(x)%5CDelta%20x%5E%7B2%7D" style="border:none;" />
    
    The formula is equivalent to the following formula.

<img src="http://chart.googleapis.com/chart?cht=tx&chl=J'(x)%2B%5Cfrac%7B1%7D%7B2%7DJ''(x)%5CDelta%20x%3D0" style="border:none;" />

    Delta_X is infinitely closing to 0.
    
<img src="http://chart.googleapis.com/chart?cht=tx&chl=J'(x)%2BJ''(x)%5CDelta%20x%3D0%5C%5C%0A%5CDelta%20x%3D-%5Cfrac%7BJ'(x)%7D%7BJ''(x)%7D" style="border:none;" />

    If X is a Multi-dimensional vector.
    
<img src="http://chart.googleapis.com/chart?cht=tx&chl=J(X)%3DJ(X_%7B0%7D)%2B(X-X_%7B0%7D)%5E%7BT%7D%5Cnabla%20J(X_%7B0%7D)%2B%5Cfrac%7B1%7D%7B2%7D(X-X_%7B0%7D)%5E%7BT%7DHJ(X_%7B0%7D)(X-X_%7B0%7D)%2Bo(%7C%7C%7C%7CX-X_%7B0%7D)%5E%7B2%7D" style="border:none;" />

    Ignore the infinitesimal, the iteration formula is：
    
<img src="http://chart.googleapis.com/chart?cht=tx&chl=X_%7Bn%2B1%7D%3DX_%7Bn%7D-%5Cfrac%7B%5Cnabla%20J(X_%7Bn%7D)%7D%7BHJ(X_%7Bn%7D)%7D" style="border:none;" />

    HJ(X) is Hessian Matrix which is a two-order partial derivative of the multivariate function of the matrix.

    For example, logistic regression

<img src="http://chart.googleapis.com/chart?cht=tx&chl=%5Cfrac%7B%5Cpart%20lnL(W)%7D%7B%5Cpart%20W%7D%3D%5Csum_%7Bi%3D1%7D%5EM%20%5B(Y%5E%7Bi%7D-%5Cfrac%7B1%7D%7B1%2Be%5E%7BW%5E%7BT%7DX%5E%7Bi%7D%7D%7D)X%5E%7Bi%7D%5D" style="border:none;" />

<img src="http://chart.googleapis.com/chart?cht=tx&chl=set%20%5C%20%5C%20%5C%20%20%5Cpi%20(X%5E%7Bi%7D)%20%3D%20%5Cfrac%7B1%7D%7B1%2Be%5E%7B-W%5E%7BT%7DX%5E%7Bi%7D%20%7D%7D" style="border:none;" />

    It is easy to get
    
<img src="http://chart.googleapis.com/chart?cht=tx&chl=%5Cfrac%7B%5Cpart%20lnL(W)%7D%7B%5Cpart%20w_%7B0%7D%7D%3D%5Csum_%7Bi%3D1%7D%5EM%20%5B(Y%5E%7Bi%7D-%5Cfrac%7B1%7D%7B1%2Be%5E%7BW%5E%7BT%7DX%5E%7Bi%7D%7D%7D)x%5E%7Bi%7D_%7B0%7D%5D" style="border:none;" />

<img src="http://chart.googleapis.com/chart?cht=tx&chl=%5Cfrac%7B%5Cpart%20lnL(W)%7D%7B%5Cpart%20w_%7B1%7D%7D%3D%5Csum_%7Bi%3D1%7D%5EM%20%5B(Y%5E%7Bi%7D-%5Cfrac%7B1%7D%7B1%2Be%5E%7BW%5E%7BT%7DX%5E%7Bi%7D%7D%7D)x%5E%7Bi%7D_%7B1%7D%5D" style="border:none;" />

<img src="http://chart.googleapis.com/chart?cht=tx&chl=%5Cfrac%7B%5Cpart%20lnL(W)%7D%7B%5Cpart%20w_%7B2%7D%7D%3D%5Csum_%7Bi%3D1%7D%5EM%20%5B(Y%5E%7Bi%7D-%5Cfrac%7B1%7D%7B1%2Be%5E%7BW%5E%7BT%7DX%5E%7Bi%7D%7D%7D)x%5E%7Bi%7D_%7B2%7D%5D" style="border:none;" />

<img src="http://chart.googleapis.com/chart?cht=tx&chl=................................................%5C%5C%0A%5Cfrac%7B%5Cpart%20lnL(W)%7D%7B%5Cpart%20w_%7Bn%7D%7D%3D%5Csum_%7Bi%3D1%7D%5EM%20%5B(Y%5E%7Bi%7D-%5Cfrac%7B1%7D%7B1%2Be%5E%7BW%5E%7BT%7DX%5E%7Bi%7D%7D%7D)x%5E%7Bi%7D_%7Bn%7D%5D" style="border:none;" />
    
    The two-order partial derivative of the multivariate function is
    
<img src="http://chart.googleapis.com/chart?cht=tx&chl=%5Cfrac%7B%5Cpart%20lnL(W)%7D%7B%5Cpart%20w_%7Bk%7D%5Cpart%20w_%7Bj%7D%7D%3D%0A%0A%5Cfrac%7B%5Cpart%20%5Csum_%7Bi%3D1%7D%5EM%20%5B(Y%5E%7Bi%7D-%5Cfrac%7B1%7D%7B1%2Be%5E%7BW%5E%7BT%7DX%5E%7Bi%7D%7D%7D)x%5E%7Bi%7D_%7Bk%7D%5D%7D%0A%7B%5Cpart%20w_%7Bj%7D%7D%0A%0A" style="border:none;" />

<img src="http://chart.googleapis.com/chart?cht=tx&chl=%5Cfrac%7B%5Cpart%20lnL(W)%7D%7B%5Cpart%20w_%7Bk%7D%5Cpart%20w_%7Bj%7D%7D%3D%0A%0A%5Csum_%7Bi%3D1%7D%5EM%20x%5E%7Bi%7D_%7Bk%7D%20%5Ccdot%20%0A%0A%5Cfrac%7B1%7D%7B1%2Be%5E%7B%20W%5E%7BT%7DX%5E%7Bi%7D%20%7D%7D%20%5Ccdot%20%0A%0A(%5Cfrac%7B1%7D%7B1%2Be%5E%7B%20W%5E%7BT%7DX%5E%7Bi%7D%20%7D%7D%20-1)%20%20%5Ccdot%20%0A%0A%20x%5E%7Bi%7D_%7Bj%7D%20" style="border:none;" />

    
    




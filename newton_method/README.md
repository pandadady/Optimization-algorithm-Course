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




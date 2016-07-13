#Quasi Newton

##1.Summary
    
    This algorithm cluster is considered as the improvement of Newton algorithm. In order to solve problems 
    
    as below:
    
    (1) The calculation of inverse matrix of hessen is too large.
    
    (2) It's hard to make sure the desent direction is always right
    
    Many algorithm is developed such as DFP correction algorithm , BFGS correction algorithm and L-BFGS 
    
    correction algorithm.The core thinking is to find other way to simulate inverse matrix of hessen instead 
    
    of directly calculating.And, in addtion, invite alpha to correct the desent direction.
    
## DFP Algorithm

    The authors of DFP algorithm is Davidon,Fletcher adn Powell, they named the algorithm by the first 
    
    letter of their name.Here introduces the quasi Newton conditions which is the core of how to simulate 
    
    the inverse matrix of hessen.
    
<img src="http://chart.googleapis.com/chart?cht=tx&chl=H_%7Bk%7D%20%5C%20%5C%20%5C%20%5Capprox%20%20%5C%20%5C%20%5C%20G_%7Bk%7D%5E%7B-1%7D" style="border:none;" />

<img src="http://chart.googleapis.com/chart?cht=tx&chl=Set%20%5C%20%5C%20%5C%5C%20g(x)%3D%5Cnabla%20f(x)%20%5C%20%5C%20%5C%20%20g_%7Bk%7D%3D%5Cnabla%20f(x%5E%7Bk%7D)%20%5C%20%5C%20%5C%20G_%7Bk%7D%3D%5Cnabla%5E%7B2%7Df(x%5E%7Bk%7D)%20%5C%5C%0A%0A%0A" style="border:none;" />


    
    Assume this is the formula of updating inverse matrix of hessen

<img src="http://chart.googleapis.com/chart?cht=tx&chl=H_%7Bk%2B1%7D%3DH_%7Bk%7D%2B%5CDelta%20H" style="border:none;" />

    Assume delta H can be repesented by uk and vk.
    
<img src="http://chart.googleapis.com/chart?cht=tx&chl=%5Calpha_%7Bk%7D%2C%5Cbeta%20_%7Bk%7D%20%5C%20%5C%20%5C%20%20%5Cin%20%5C%20%5C%20%5C%20R%5C%5C%0Au_%7Bk%7D%2Cv_%7Bk%7D%20%5C%20%5C%20%5C%20%20%5Cin%20%5C%20%5C%20%5C%20%20R%5E%7Bn%7D%5C%5C%0A%0A%5CDelta%20H%20%3D%20%5Calpha_%7Bk%7D%20u_%7Bk%7Du_%7Bk%7D%5E%7BT%7D%2B%5Cbeta%20_%7Bk%7D%20v_%7Bk%7Dv_%7Bk%7D%5E%7BT%7D" style="border:none;" />

    
    
    
    
## BFGS Algorithm

## LBFGS Algorithm


    
    

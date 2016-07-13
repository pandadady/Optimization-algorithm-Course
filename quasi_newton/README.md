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
    
    letter of their name.
    
    Assume this is the formula of updating inverse matrix of hessen

<img src="http://chart.googleapis.com/chart?cht=tx&chl=H_%7Bk%2B1%7D%3DH_%7Bk%7D%2B%5CDelta%20H" style="border:none;" />

## BFGS Algorithm

## LBFGS Algorithm


    
    

#Quasi Newton

##1.Summary
    
    This algorithm cluster is considered as the improvement of Newton algorithm. In order to solve problems 
    
    as below:
    
    (1) The calculation of inverse matrix of hessen is too large.
    
    (2) It's hard to make sure the desent direction is always right
    
    Many algorithm is developed such as DFP correction algorithm , BFGS correction algorithm and L-BFGS 
    
    correction algorithm.The core thinking is to find other way to simulate inverse matrix of hessen instead 
    
    of directly calculating.And, in addtion, invite alpha to correct the desent direction.
    
##2.DFP Algorithm
    The authors of DFP algorithm is Davidon,Fletcher adn Powell, they named the algorithm by the first 
    
    letter of their name.Here introduces the quasi Newton conditions which is the core of how to simulate 
    
    the inverse matrix of hessen.
    
<img src="http://chart.googleapis.com/chart?cht=tx&chl=H_%7Bk%7D%20%5C%20%5C%20%5C%20%5Capprox%20%20%5C%20%5C%20%5C%20G_%7Bk%7D%5E%7B-1%7D" style="border:none;" />

<img src="http://chart.googleapis.com/chart?cht=tx&chl=Set%20%5C%20%5C%20%5C%5C%20g(x)%3D%5Cnabla%20f(x)%20%5C%20%5C%20%5C%20%20g_%7Bk%7D%3D%5Cnabla%20f(x%5E%7Bk%7D)%20%5C%20%5C%20%5C%20G_%7Bk%7D%3D%5Cnabla%5E%7B2%7Df(x%5E%7Bk%7D)%20%5C%5C%0A%0A%0A" style="border:none;" />

    2-oder Taylor formula
    
<img src="http://chart.googleapis.com/chart?cht=tx&chl=g(x)%5Capprox%20g(x%5E%7Bk%2B1%7D)%2B%5Cnabla%5E%7B2%7Df(x%5E%7Bk%2B1%7D)(x-x%5E%7Bk%2B1%7D)%5C%5C%0Ag_%7Bk%7D%5Capprox%20g(x%5E%7Bk%2B1%7D)%2B%5Cnabla%5E%7B2%7Df(x%5E%7Bk%2B1%7D)(x%5E%7Bk%7D-x%5E%7Bk%2B1%7D)%5C%5C%0A" style="border:none;" />

    It is easy to get.

<img src="http://chart.googleapis.com/chart?cht=tx&chl=g_%7Bk%2B1%7D-g_%7Bk%7D%3DG_%7Bk%2B1%7D(x%5E%7Bk%7D-x%5E%7Bk%2B1%7D)%5C%5C%0A%0AG_%7Bk%2B1%7D%5E%7B-1%7D(g_%7Bk%2B1%7D-g_%7Bk%7D)%3D(x%5E%7Bk%7D-x%5E%7Bk%2B1%7D)%5C%5C%0A" style="border:none;" />
    
    Add H.

<img src="http://chart.googleapis.com/chart?cht=tx&chl=H_%7Bk%2B1%7D(g_%7Bk%2B1%7D-g_%7Bk%7D)%3D(x%5E%7Bk%7D-x%5E%7Bk%2B1%7D)%5C%5C%0A" style="border:none;" />

<img src="http://chart.googleapis.com/chart?cht=tx&chl=Set%20%5C%20%5C%20%5C%20y_%7Bk%7D%3Dg_%7Bk%2B1%7D-g_%7Bk%7D%2C%5C%20%5C%20%5C%20s_%7Bk%7D%3D(x%5E%7Bk%7D-x%5E%7Bk%2B1%7D)%5C%5C%0A" style="border:none;" />

    And this is quasi-newton-condition.

<img src="http://chart.googleapis.com/chart?cht=tx&chl=H_%7Bk%2B1%7Dy_%7Bk%7D%3Ds_%7Bk%7D%0A" style="border:none;" />    

    Assume this is the formula of updating inverse matrix of hessen

<img src="http://chart.googleapis.com/chart?cht=tx&chl=H_%7Bk%2B1%7D%3DH_%7Bk%7D%2B%5CDelta%20H" style="border:none;" />

    Assume delta H can be repesented by uk and vk.
    
<img src="http://chart.googleapis.com/chart?cht=tx&chl=%5Calpha_%7Bk%7D%2C%5Cbeta%20_%7Bk%7D%20%5C%20%5C%20%5C%20%20%5Cin%20%5C%20%5C%20%5C%20R%5C%5C%0Au_%7Bk%7D%2Cv_%7Bk%7D%20%5C%20%5C%20%5C%20%20%5Cin%20%5C%20%5C%20%5C%20%20R%5E%7Bn%7D%5C%5C%0A%0A%5CDelta%20H%20%3D%20%5Calpha_%7Bk%7D%20u_%7Bk%7Du_%7Bk%7D%5E%7BT%7D%2B%5Cbeta%20_%7Bk%7D%20v_%7Bk%7Dv_%7Bk%7D%5E%7BT%7D" style="border:none;" />

    Add quasi-newton-condition into formula.
    
<img src="http://chart.googleapis.com/chart?cht=tx&chl=(H_%7Bk%7D%2B%5Calpha%20_%7Bk%7D%20u_%7Bk%7Du_%7Bk%7D%5E%7BT%7D%2B%5Cbeta%20_%7Bk%7Dv_%7Bk%7Dv_%7Bk%7D%5E%7BT%7D)y_%7Bk%7D%3Ds_%7Bk%7D%0A" style="border:none;" />

<img src="http://chart.googleapis.com/chart?cht=tx&chl=%5Calpha%20_%7Bk%7D%20u_%7Bk%7Du_%7Bk%7D%5E%7BT%7Dy_%7Bk%7D%2B%5Cbeta%20_%7Bk%7Dv_%7Bk%7Dv_%7Bk%7D%5E%7BT%7Dy_%7Bk%7D%3Ds_%7Bk%7D-H_%7Bk%7Dy_%7Bk%7D%0A" style="border:none;" />

    The above equation has many solutions, there is certain solution which needs our concern.
    
<img src="http://chart.googleapis.com/chart?cht=tx&chl=%5Calpha%20_%7Bk%7D%20u_%7Bk%7Du_%7Bk%7D%5E%7BT%7Dy_%7Bk%7D%3Ds_%7Bk%7D%5C%5C%0A%5Cbeta%20_%7Bk%7Dv_%7Bk%7Dv_%7Bk%7D%5E%7BT%7Dy_%7Bk%7D%3D-H_%7Bk%7Dy_%7Bk%7D%0A" style="border:none;" />

    Assume this 
    
<img src="http://chart.googleapis.com/chart?cht=tx&chl=%5Calpha%20_%7Bk%7Du_%7Bk%7D%5E%7BT%7Dy_%7Bk%7D%3D1%5C%5C%0Au_%7Bk%7D%3Ds_%7Bk%7D%5C%5C%0A%5Cbeta%20_%7Bk%7Dv_%7Bk%7D%5E%7BT%7Dy_%7Bk%7D%3D-1%5C%5C%0Av_%7Bk%7D%3DH_%7Bk%7Dy_%7Bk%7D%0A" style="border:none;" />
    
    So 
    
<img src="http://chart.googleapis.com/chart?cht=tx&chl=%5Calpha%20_%7Bk%7D%3D%5Cfrac%7B1%7D%7Bs_%7Bk%7D%5E%7BT%7Dy_%7Bk%7D%7D%5C%5C%0Au_%7Bk%7D%3Ds_%7Bk%7D%5C%5C%0A%5Cbeta%20_%7Bk%3D-%5Cfrac%7B1%7D%7B%7Dy_%7Bk%7D%5E%7BT%7DH_%7Bk%7Dy_%7Bk%7D%7D%5C%5C%0Av_%7Bk%7D%3DH_%7Bk%7Dy_%7Bk%7D%0A" style="border:none;" />

    Then the iteration formula is 
    
<img src="http://chart.googleapis.com/chart?cht=tx&chl=%0AH_%7Bk%2B1%7D%3DH_%7Bk%7D%2B%5Cfrac%7Bs_%7Bk%7Ds_%7Bk%7D%5E%7BT%7D%7D%7Bs_%7Bk%7D%5E%7BT%7Dy_%7Bk%7D%7D-%0A%0A%5Cfrac%7BH_%7Bk%7Dy_%7Bk%7Dy_%7Bk%7D%5E%7BT%7DH_%7Bk%7D%7D%7B%7Dy_%7Bk%7D%5E%7BT%7DH_%7Bk%7Dy_%7Bk%7D%7D" style="border:none;" />
    
    
##3.BFGS Algorithm

##4.LBFGS Algorithm


    
    

#Grandient method

##1.Summary

    It is the simplest and the most commonly optimization method. It is easy to achieve. Only when the objective 
    
    function is a convex function, the solution of the gradient descent method is a global solution. Usually, the 

    the solution of the gradient descent method isn't a global solution.
    
##2.Process
    
    For example, logistic regression, weight is updated following the below formalu.

<img src="http://chart.googleapis.com/chart?cht=tx&chl=W%5E%7Bt%2B1%7D%3DW%5E%7Bt%7D-%5Calpha%20%5Cfrac%7B%5Cpart%20lnL(w)%7D%7B%5Cpart%20W%7D" style="border:none;" />   

    BGD(Batch gradient descent method):
    
        During each iteration, all the input will be taken into calculation. The solution is goning 
        
        towards the global solution.
        
<img src="http://chart.googleapis.com/chart?cht=tx&chl=%5Cfrac%7B%5Cpart%20lnL(w)%7D%7B%5Cpart%20W%7D%20%3D%5Csum_%7Bi%3D1%7D%5EM%20%5B(Y%5E%7Bi%7DX%5E%7Bi%7D-%5Cfrac%7B1%7D%7B1%2Be%5E%7BW%5E%7BT%7DX%5E%7Bi%7D%7D%7D)X%5E%7Bi%7D%5D" style="border:none;" />
        

    SGD(Stochastic gradient descent method):
        
        During each iteration, one sample of data will be taken into calculation. It means to loss some accuracy but 
        
        speed up the process of convergence.

<img src="http://chart.googleapis.com/chart?cht=tx&chl=%5Cfrac%7B%5Cpart%20lnL(w)%7D%7B%5Cpart%20W%7D%20%3D%20%5B(Y%5E%7Bi%7DX%5E%7Bi%7D-%5Cfrac%7B1%7D%7B1%2Be%5E%7BW%5E%7BT%7DX%5E%7Bi%7D%7D%7D)X%5E%7Bi%7D%5D" style="border:none;" />
        
##3.Experiment

    The number of sample is 100, The dimension is 3.
<table>
<tr>
<td> Method name </td> <td> Iteration number</td> <td> Calculation time </td>
</tr>
<tr>
<td> BGD </td> <td> 500 </td> <td> 0.021650905029 s </td>
</tr>
<tr>
<td> SGD </td> <td> 150 </td> <td> 0.176577097458 s </td>
</tr>
</table>
    
    

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

    HJ(X) is Hessian Matrix which is a multivariate function of the two - order partial derivative of the matrix.

<math xmlns="http://www.w3.org/1998/Math/MathML" display="block">
  <semantics>
    <mrow>
      <mrow class="MJX-TeXAtom-ORD">
        <mi mathvariant="bold">H</mi>
      </mrow>
      <mo>=</mo>
      <mrow>
        <mo>[</mo>
        <mtable rowspacing="4pt" columnspacing="1em">
          <mtr>
            <mtd>
              <mfrac>
                <mrow>
                  <msup>
                    <mi mathvariant="normal">&#x2202;<!-- ∂ --></mi>
                    <mn>2</mn>
                  </msup>
                  <mi>f</mi>
                </mrow>
                <mrow>
                  <mi mathvariant="normal">&#x2202;<!-- ∂ --></mi>
                  <msubsup>
                    <mi>x</mi>
                    <mn>1</mn>
                    <mn>2</mn>
                  </msubsup>
                </mrow>
              </mfrac>
            </mtd>
            <mtd>
              <mfrac>
                <mrow>
                  <msup>
                    <mi mathvariant="normal">&#x2202;<!-- ∂ --></mi>
                    <mn>2</mn>
                  </msup>
                  <mi>f</mi>
                </mrow>
                <mrow>
                  <mi mathvariant="normal">&#x2202;<!-- ∂ --></mi>
                  <msub>
                    <mi>x</mi>
                    <mn>1</mn>
                  </msub>
                  <mi mathvariant="normal">&#x2202;<!-- ∂ --></mi>
                  <msub>
                    <mi>x</mi>
                    <mn>2</mn>
                  </msub>
                </mrow>
              </mfrac>
            </mtd>
            <mtd>
              <mo>&#x22EF;<!-- ⋯ --></mo>
            </mtd>
            <mtd>
              <mfrac>
                <mrow>
                  <msup>
                    <mi mathvariant="normal">&#x2202;<!-- ∂ --></mi>
                    <mn>2</mn>
                  </msup>
                  <mi>f</mi>
                </mrow>
                <mrow>
                  <mi mathvariant="normal">&#x2202;<!-- ∂ --></mi>
                  <msub>
                    <mi>x</mi>
                    <mn>1</mn>
                  </msub>
                  <mi mathvariant="normal">&#x2202;<!-- ∂ --></mi>
                  <msub>
                    <mi>x</mi>
                    <mi>n</mi>
                  </msub>
                </mrow>
              </mfrac>
            </mtd>
          </mtr>
          <mtr>
            <mtd>
              <mfrac>
                <mrow>
                  <msup>
                    <mi mathvariant="normal">&#x2202;<!-- ∂ --></mi>
                    <mn>2</mn>
                  </msup>
                  <mi>f</mi>
                </mrow>
                <mrow>
                  <mi mathvariant="normal">&#x2202;<!-- ∂ --></mi>
                  <msub>
                    <mi>x</mi>
                    <mn>2</mn>
                  </msub>
                  <mi mathvariant="normal">&#x2202;<!-- ∂ --></mi>
                  <msub>
                    <mi>x</mi>
                    <mn>1</mn>
                  </msub>
                </mrow>
              </mfrac>
            </mtd>
            <mtd>
              <mfrac>
                <mrow>
                  <msup>
                    <mi mathvariant="normal">&#x2202;<!-- ∂ --></mi>
                    <mn>2</mn>
                  </msup>
                  <mi>f</mi>
                </mrow>
                <mrow>
                  <mi mathvariant="normal">&#x2202;<!-- ∂ --></mi>
                  <msubsup>
                    <mi>x</mi>
                    <mn>2</mn>
                    <mn>2</mn>
                  </msubsup>
                </mrow>
              </mfrac>
            </mtd>
            <mtd>
              <mo>&#x22EF;<!-- ⋯ --></mo>
            </mtd>
            <mtd>
              <mfrac>
                <mrow>
                  <msup>
                    <mi mathvariant="normal">&#x2202;<!-- ∂ --></mi>
                    <mn>2</mn>
                  </msup>
                  <mi>f</mi>
                </mrow>
                <mrow>
                  <mi mathvariant="normal">&#x2202;<!-- ∂ --></mi>
                  <msub>
                    <mi>x</mi>
                    <mn>2</mn>
                  </msub>
                  <mi mathvariant="normal">&#x2202;<!-- ∂ --></mi>
                  <msub>
                    <mi>x</mi>
                    <mi>n</mi>
                  </msub>
                </mrow>
              </mfrac>
            </mtd>
          </mtr>
          <mtr>
            <mtd>
              <mo>&#x22EE;<!-- ⋮ --></mo>
            </mtd>
            <mtd>
              <mo>&#x22EE;<!-- ⋮ --></mo>
            </mtd>
            <mtd>
              <mo>&#x22F1;<!-- ⋱ --></mo>
            </mtd>
            <mtd>
              <mo>&#x22EE;<!-- ⋮ --></mo>
            </mtd>
          </mtr>
          <mtr>
            <mtd>
              <mfrac>
                <mrow>
                  <msup>
                    <mi mathvariant="normal">&#x2202;<!-- ∂ --></mi>
                    <mn>2</mn>
                  </msup>
                  <mi>f</mi>
                </mrow>
                <mrow>
                  <mi mathvariant="normal">&#x2202;<!-- ∂ --></mi>
                  <msub>
                    <mi>x</mi>
                    <mi>n</mi>
                  </msub>
                  <mi mathvariant="normal">&#x2202;<!-- ∂ --></mi>
                  <msub>
                    <mi>x</mi>
                    <mn>1</mn>
                  </msub>
                </mrow>
              </mfrac>
            </mtd>
            <mtd>
              <mfrac>
                <mrow>
                  <msup>
                    <mi mathvariant="normal">&#x2202;<!-- ∂ --></mi>
                    <mn>2</mn>
                  </msup>
                  <mi>f</mi>
                </mrow>
                <mrow>
                  <mi mathvariant="normal">&#x2202;<!-- ∂ --></mi>
                  <msub>
                    <mi>x</mi>
                    <mi>n</mi>
                  </msub>
                  <mi mathvariant="normal">&#x2202;<!-- ∂ --></mi>
                  <msub>
                    <mi>x</mi>
                    <mn>2</mn>
                  </msub>
                </mrow>
              </mfrac>
            </mtd>
            <mtd>
              <mo>&#x22EF;<!-- ⋯ --></mo>
            </mtd>
            <mtd>
              <mfrac>
                <mrow>
                  <msup>
                    <mi mathvariant="normal">&#x2202;<!-- ∂ --></mi>
                    <mn>2</mn>
                  </msup>
                  <mi>f</mi>
                </mrow>
                <mrow>
                  <mi mathvariant="normal">&#x2202;<!-- ∂ --></mi>
                  <msubsup>
                    <mi>x</mi>
                    <mi>n</mi>
                    <mn>2</mn>
                  </msubsup>
                </mrow>
              </mfrac>
            </mtd>
          </mtr>
        </mtable>
        <mo>]</mo>
      </mrow>
    </mrow>
    <annotation encoding="application/x-tex">\mathbf{H}=\begin{bmatrix} 
\frac{\partial^2f}{\partial x_1^2} & \frac{\partial^2f}{\partial x_1\partial x_2} & \cdots &\frac{\partial^2f}{\partial x_1\partial x_n} \\
 \frac{\partial^2f}{\partial x_2\partial x_1} & \frac{\partial^2f}{\partial x_2^2} &  \cdots &\frac{\partial^2f}{\partial x_2\partial x_n} \\ \vdots & \vdots & \ddots & \vdots \\
\frac{\partial^2f}{\partial x_n\partial x_1}&\frac{\partial^2f}{\partial x_n\partial x_2}&\cdots &\frac{\partial^2f}{\partial x_n^2} \end{bmatrix}</annotation>
  </semantics>
</math>




---
title: "Polynomial Generator Functions"
date: 2024-12-28T12:33:01+01:00
draft: false
toc: false
images:
math: true
tags: 
  - signal-processing
  - polynomials
  - digital-circuits
  - python
---

Previously I went over some interesting techniques for 
[synthesizing sinusoids]({{< relref "../2022/synthesizing-sinusoids" >}}). 
There were some interesting points to take away from that discussion. First
the CIC topology essentially calculated the Nᵗʰ moments or derivatives in a 
signal and essentially reconstructed a corresponding response using a polynomial
with those moments or piece-wise derivatives.

This leads to a interesting question when synthesizing a time-limited
waveform: What are the properties for using polynomial generator functions
for waveform synthesis if we follow a simple cascade of integrators? The 
general structure for a cascade of integrators is shown below.


``` goat
   
       .-.              .-.              .-.            
c₃ -->| Σ +-----*----->| Σ +-----*----->| Σ +-----*---->  N sequence Waveform
       '-'      |       '-'      |       '-'      |     
        ^       v        ^       v        ^       v     
        |    .-----.     |    .-----.     |    .-----.  
        |    | z⁻¹ |<--  |    | z⁻¹ |<--  |    | z⁻¹ |<-- Initial Conditions
        |    '--+--'     |    '--+--'     |    '--+--'    3ʳᵈ Order Polynomial
        |       |        |       |        |       |       c₂, c₁, c₀
         '-----'          '-----'          '-----'     

```

The concept here is that the registers are initialized with coefficients
derived from the desired polynomial response and sequenced for a fixed set of
cycles before we trigger a reset. This is some what a simplified scenario but
one could imagine the sequence can be used to modulate a RF carrier in order
to transmit amplitude modulated symbols. As we will see the approach of using
generator functions will allow us to synthesize high-precision waveforms with
exact frequency characteristics with just a few predetermined coefficients.

At first glance, we can reason that many of the desirable properties that one would 
like to see here are similar to that of window functions (e.g. Hanning or
Kaiser Windows)[^1]. This is because we are interested in both the time and 
frequency properties of the generated sequence simultaneously. The key 
difference here however is that we are constrained to polynomial dynamics.
As a result the text-book approach for approximating a sum of weighted cosines
may not be the best approach. Although taking a padé-approximant, using a 
rational polynomial basis, may be a good choice in some cases. More generally
nesting or convolving our polynomial basis will result in higher oder 
polynomal. In order to realize a transcendental response we would need to
revisit the feedback coefficient for each integrator.

## Determining Initial Conditions

There are a few ways to go about defining a polynomial \\(P(x)\\). Either in terms of
the roots or in terms of the characteristic equation. Both are useful, 
especially when we consider the derivative components at the extents of our
synthesized waveform.

$$ P(x) = (x-p_1) (x-p_2) (x-p_3) ... (x-p_n) $$

$$ P(x) = a_n x^n + ... + a_2 x^2 + a_1 x + a_0 $$

We can back calculate the corresponding initial conditions for our cascade
of integrators by considering the super-position of each component $a_n$ 
seperately. Lets denote our initial conditions as \\( c_n + ... + c_2 + c_1 + c_0 \\)
for our Nᵗʰ order polynomial. As shown in the diagram above the coefficient 
\\(c_n\\) is directly accumulated on the left most integrator. It should be obvious
that the first two coefficients: \\(a_1\\) & \\(a_0\\) from our characteristic equation 
directly related correspond to \\(c_1\\) & \\(c_0\\) respectively. Now we can infer the 
mapping by recursion and equating the derivative components. For example \\(P(x) = a_2 x^2\\): the
contribution from \\(a_2\\) on the 2nd order derivative is calculated as taking 
the 2nd derivative of \\(P(x)\\) and evaluating its value with x=0 which gives 
us \\(c_2 = 2 * a_2\\). Now equating the 1st derivative from \\(a_2\\) 
similarly gives \\(c_1 = a_2\\) and finally \\(c_0 = 0\\). If there were lower 
order terms, the contribution from a_1 for example would be calculated 
independently and added together.

This was a simpler example but one can reason that if the mapping for a particular \\( a_n \\) is
\\( m_n, ... , m_1, m_0 \\) such that for all \\( n \\) the initial conditions are
\\(c_n = m_n a_n\\). Then for some given mapping of a Nᵗʰ order polynomial
we can add one more integration stage to the far right integrating the output 
to realize a N+1ᵗʰ order polynomial. This is equivalent to multiplying the 
response with \\( x + 1 \\). Now it should be clear that when we equate the 
derivative terms the N+1ᵗʰ order terms can be derived from the Nᵗʰ order terms 
simply by adding the appropriate contributions after the aforementioned 
multiplication. That is \\( k_n = m_n + m_{n-1} \\) where \\( k_n \\) are the 
mapping terms for the N+1ᵗʰ order polynomial.
Interestingly the mapping here generates a set of basis coefficients related to
the sterling-numbers of the second kind. More specifically the 
[A019538](https://oeis.org/A019538) sequence. Using python and numpy as np 
we can write the following recursive function:

``` python
def mapping_coefficients(order: int) -> np.array:
    """Determine nth coefficient scaling factor for initial condition."""
    assert order >= 0
    # Start with coefficient from n-1
    if order == 0:
        return np.array([1])
    elif order == 1:
        return np.array([1, 0])
    else:
        base = mapping_coefficients(order - 1)
    coef = np.zeros((order + 1,))
    for elem in range(order - 1):
        # for each element calculate new coefficient
        # Based on expanding d/dx * P(x) * (x+1)
        coef[elem + 1] = (order - elem - 1) * (base[elem] + base[elem + 1])
    # m_n will always be n!
    coef[0] = base[0] * order
    return coef

```

This function will derive the \\( m_n \\) mapping values based on our recursive 
derivation above. In order to then determine the initial conditions we similarly
iterate over the characteristic coefficients \\( a_n \\) and accumulate all 
contributions to resolve the initial conditions \\( c_n \\).

``` python
def initial_condition(self, poly_coef: np.array) -> np.array:
    """Set register values based on polynomial coefficients."""
    init_coef = np.zeros((poly_coef.size,))
    for index, elem in enumerate(poly_coef):
        init_coef[index:] += elem * mapping_coefficients(poly_coef.size - index - 1)
    return init_coef

```

It is worthwhile to point out that not all polynomial functions can be realized
with this method. While not all zeros in \\( P(x) \\) have to be real, we do 
require the characteristic coefficients \\( a_n \\) and thereby \\( c_n \\) to
to be real numbers. 

## Frequency Response

Here we will consider a simplified scenario to exemplify the frequency \
characteristics for generated polynomials.
Specifically polynomials of even orders with real roots such
that we can decompose the polynomial \\(P(x)\\) as a product of several 
elements in the form of \\( (x+p_1)(x+p_2) \\). We can show that the 
fourier-transform of of this element is in the form of \\( sinc(d ω)^4 \\)
where \\( d = (p_1 - p_2)/2 \\) such that we can resolve the transform for 
\\( P(x) = (x+d)(x-d) \\)

First consider a simple box function of 
width \\( d/4 \\) and its corresponding fourier transform:

$$
S(x) = \begin{cases}
   1 &\text{if |x| <= d/4 } \\\\
   0 &\text{otherwise } 
\end{cases}  \quad \xrightarrow{\mathfrak{F}} \quad \frac{d}{2}  sinc( \frac{d\omega}{4} ) 
$$

We can auto-convolve \\(S(x)\\) twice in order to realize a parabola with roots at
+/- d. First formulate the associated triangle function \\(T(x)\\):

$$
T(x) = S(x) \ast S(x) = \int_{-d/2}^{d/2} S(\tau) S(x-\tau) d\tau \quad = \begin{cases}
   0  &\text{if x <  -d/2 } \\\\
   (x+d/2)  &\text{if x <  0 } \\\\
   (d/2-x)  &\text{if x <  d/2 } \\\\
   0  &\text{otherwise}
\end{cases}
$$

The second auto-convolution of \\(T(x)\\) gives back the parabola \\(P(x)\\):

$$
P(x) = T(x) \ast T(x) = \int_{-d}^{d} T(\tau) T(x-\tau) d\tau = \begin{cases}
   d^2/4 - x^2/4  &\text{if |x| <= d } \\\\
   0 &\text{otherwise }
\end{cases}
$$



$$
P(x) \quad \xrightarrow{\mathfrak{F}} \quad \frac{d^4}{16}  sinc(\frac{d\omega}{4} )^4
$$


## References:

[^1]: A. Nuttall, ''Some windows with very good sidelobe behavior,'' IEEE 
Trans. Acoust., Speech, Signal Process. , vol. 29, no. 1, pp. 84-91, February 
1981 [Online]:  http://dx.doi.org/10.1109/TASSP.1981.1163506.

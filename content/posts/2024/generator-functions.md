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
of integrators by considering the super-position of each component \\(a_n\\) 
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
order terms, the contribution from \\(a_1\\) for example would be calculated 
independently and added together.

This was a simpler example but one can reason that if the mapping for a particular \\( a_n \\) is
\\( m(n,i), ... , m(n,1), m(n,0) \\) such that for all \\( i \\) the initial conditions are
\\(c_n = \sum^n_{i=0} m(n,i) * a_i\\). The final value for the initial condition \\(c_n\\) is then
sum of all mapping terms from each \\(a_n\\). Then for some given mapping of a Nᵗʰ order polynomial
we can add one more integration stage to the far right integrating the output 
to realize a N+1ᵗʰ order polynomial. This is equivalent to multiplying the 
response with \\( x + 1 \\). Now it should be clear that when we equate the 
derivative terms the N+1ᵗʰ order terms can be derived from the Nᵗʰ order terms 
simply by adding the appropriate contributions after the aforementioned 
multiplication. That is \\( m(n+1,i) = m(n,i) + m(n,i-1) \\) where \\( m(n+1,i) \\) 
are the mapping terms for the N+1ᵗʰ order polynomial.
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

This function will derive the \\( m(n,i) \\) mapping values based on our recursive 
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
fourier-transform of of this element is in the form of \\( sinc(d ω)^2 \\)
where \\( d = (p_1 - p_2)/2 \\) such that we can derive relations for the 
polynomial \\( P(x) = d^2-x^2 \\) and scale them accordingly.

$$
\hat{P}(x) = \int^{d/2}_{d/2} (d^2-x^2) cos(k x) dx 
\quad = \quad 
\frac{8 \sin{ (d k) }}{k^3} -  \frac{8 d \cos{ (d k ) }}{k^2}
$$

Here we have an example where \\(d=1\\) and we observe the expected
characteristic functions in both time and frequency space.

{{< figure src="/images/posts/generator/P2.svg" >}}
{{< figure src="/images/posts/generator/F2.svg" >}}

We can numerically solve for some of the filter properties of interest and 
compare to other simple windows. There is little suprise in the table below
as the roll-off and rejection is closely related to the 3dB bandwidth.
Here we see that the frequency response of P(x) is somewhere inbetween a 
rectangular window and that of the raise-cosine or Hann window.

| Property      | 2nd Order Poly len(2d) | Rectangle len(2d)     | Hann len(2d)          |
|---------------|------------------------|-----------------------|-----------------------|
| DC Value      | \\(\frac{2d^3}{3}\\)   | \\(2d^2\\)            | \\(2d^2\\)            |
| 3dB Bandwidth | \\(\sim 2.498/d\\)     | \\(\sim 1.895/d\\)    | \\(\sim 3.168/d\\)    |
| 1st Null      | \\(\sim 4.5/d\\)       | \\(\frac{\pi}{d}\\)   | \\(\frac{2\pi}{d}\\)  |
| Roll Off      | 40 dB / decade         | 20 dB / decade        | 60 dB / decade        |
| First Sidelobe| -21 dB                 | -13 dB                | -31 dB                |

For completeness we also include the analytical expression for the Hann window
frourier transform.

$$
\hat{H}(x) = \int^{d/2}_{d/2} (1+cos(\frac{2\pi x}{d})) cos(k x) dx 
\quad = \quad 
\frac{2 \pi^2 sin(d k)}{k(d^2 k^2-\pi^2)}
$$

Because we have a clean analytical representation of the frequency response
it is simple to manipulate our coefficients to get a more desirable response.
The second order function is limited to a three term composition: 
\\(sinc + sinc/k^2 + cos/k^2\\). Adding assymetry or using odd-order polynomials 
can resolve band-pass characteristics which are also interesting. 

In the example below we have chosen to place poles at \\(\pm d\\) and 
\\(\pm 1.2 d\\) in order to minimize the first sidelobe level using a 
8ᵗʰ order polynomial.

{{< figure src="/images/posts/generator/P4.svg" title="" width="500" >}}
{{< figure src="/images/posts/generator/F4.svg" title="" width="500" >}}

## References:

[^1]: A. Nuttall, ''Some windows with very good sidelobe behavior,'' IEEE 
Trans. Acoust., Speech, Signal Process. , vol. 29, no. 1, pp. 84-91, February 
1981 [Online]:  http://dx.doi.org/10.1109/TASSP.1981.1163506.

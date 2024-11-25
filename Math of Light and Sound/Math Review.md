# Part 1
* Wave Equation
* Wave Equation development
* Damped simple harmonic oscillation
* Wave motion simulation using appropriate numerical

equ**ili**brium 平衡 
$c$ speed $m s^{-1}$ 
$\lambda$ wave length $m$
$T = \lambda/c$ wave period $s$
$v = 1/T = c/\lambda$ wave frequency $Hz$
$\omega = 2\pi/T$ angular frequency $rad\space s^{-1}$ 
$k=2\pi/\lambda$ wave number $rad\space m^{-1}$ 

## Wave equation

![[Math Review-20241124213433763.webp]]

### Math Description

**$r$ is the distance, $t$ is time**

>[!definition] Sum of two sinusoids travelling in opposite directions over time.
>* The term $cos(kr - \omega t)$ represents a wave travelling in the positive r-direction
>* The term $cos(kr + \omega t)$ represents a wave travelling in the negative r-direction
>  ![[Math Review-20241119220602262.webp]]
>
>### Superposition Principle: 
>The total wave $A(r,t)$ is the result of adding these two waves together, demonstrating the principle of superposition, where waves combine to form a resultant wave.
>
>### Physical Interpretation: 
>Two waves have the same amplitude, wavenumber $k=2\pi/\lambda$, and angular frequency $\omega = 2\pi/T$, but they travel in opposite directions.
>
>### Simplification to a Standing Wave: 
>Using the trigonometric identity $\cos(x) + \cos(y) = 2\cos\left(\frac{x+y}{2}\right)$ you can rewrite A(r,t) as $$A(r, t) = 2 \cos(kr) \cos(\omega t)$$
>
>* $\cos(kr)$: Describes the spatial variation of the standing wave, where A(r,t)=0.
>* $\cos(\omega t)$: Describes the temporal variation, showing oscillations in time.
>  ### Conceptual meaning
>  - The equation models a standing wave, where the wave's shape remains stationary in space, with certain points (nodes) not moving, while others (antinodes) oscillate with maximum amplitude.
>  - This arises from the interference of two waves traveling in opposite directions with the same frequency and wavelength.


The equation at first is in angular, then as we solve, it turns into meters.
$$
\begin{align}
A(r,t) & = cos(kr - \omega t) + cos(kr + \omega t) \\
&=cos(\frac {2\pi} {\lambda} r - \frac {2\pi} {T}) + cos(\frac {2\pi} {\lambda} r + \frac {2\pi} {T}) \\
&=cos(\frac {2\pi} {\lambda} (r - ct)) + cos(\frac {2\pi} {\lambda} (r + ct))
\end{align}
$$
A constrain equation derived from Newton's and Hooke's physical law:
$$
\frac {\partial A(r, t)} {\partial r^2} = \frac {1} {c^2} \frac {\partial A(r, t)} {\partial t^2}
$$



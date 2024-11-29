## Simulation of String Wave Propagation Using Finite Difference Approximation

#### Purpose

This program simulates wave propagation on a string using the **finite difference approximation** to solve the 1D wave equation:
$$\frac{\partial^2 A}{\partial t^2} = c^2 \frac{\partial^2 A}{\partial x^2}$$
where A(x, t) is the displacement, and c is the wave speed. It models the evolution of the string's displacement over time and visualizes the results.

---

### Numerical Methodology

1. **Discretization**:
    
    - The string of length L and simulation time T are divided into $N_x$ spatial and $N_t$ temporal points, with step sizes: $\Delta x = \frac{L}{N_x}, \quad \Delta t = \frac{T}{N_t}$
2. **Finite Difference Scheme**:
    
    - The second-order spatial and temporal derivatives are approximated as: $\frac{\partial^2 A}{\partial t^2} \approx \frac{A_{i+1, j} - 2A_{i, j} + A_{i-1, j}}{\Delta t^2}, \quad \frac{\partial^2 A}{\partial x^2} \approx \frac{A_{i, j+1} - 2A_{i, j} + A_{i, j-1}}{\Delta x^2}$
    - Substituting into the wave equation: 
      $A_{i+1, j} = 2A_{i, j} - A_{i-1, j} + C^2 \left(A_{i, j+1} - 2A_{i, j} + A_{i, j-1}\right)$ where $C = \frac{c \Delta t}{\Delta x}$ is the **Courant number**.
3. **Stability Condition**:
    
    - The scheme is stable only if $C \leq 1$. If $C > 1$, the program halts.

---

### Implementation

1. **Initial Conditions**:
    
    - The string starts with a triangular displacement profile and no initial velocity: $a_{j}^{0} = L(x), \quad a_{j}^{i+1} = a_{j}^{i - 1}, for \space i = 0$
2. **Wave Propagation**:
    
    - The displacement at **each grid point is iteratively computed** for **each time step** using the **finite difference scheme**.
3. **Visualization**:
    
    - An animation visualizes the wave's evolution over time using `Matplotlib`.

---

### Key Features

- **Accuracy**: The program uses second-order central differences for space and time.
- **Stability**: Enforces C≤1C \leq 1 to prevent divergence.
- **Animation**: Displays wave propagation, demonstrating standing or traveling wave behavior depending on initial conditions.

---

### Applications

This program models wave dynamics in systems like vibrating strings, seismic waves, or sound waves. It can be extended with damping, realistic boundary conditions, or higher-order methods.

---

This concise explanation balances technical detail and clarity within the word limit. Let me know if you need further adjustments!


Here’s a concise explanation under 500 words:

---

## Simulation of Wave Propagation for acoustic Wave

#### Purpose

The program simulates the propagation of waves in **a medium using discrete points**, showcasing longitudinal and transverse displacements caused by the superposition of traveling waves. It visualizes wave behavior dynamically with customizable parameters.

---

### Wave Solution

The wave is modeled using the equation:

$A(x, t) = R \cos(kx - \omega t) + (1 - R) \cos(kx + \omega t)$

Where:

- R: Controls the wave direction and amplitude balance.
- $k = \frac{2\pi}{\lambda}$: Wavenumber.
- $\omega = \frac{2\pi}{f}$: Angular frequency.
- $A(x, t)$: Combined displacement at position x and time t.

This equation **represents the superposition of leftward and rightward traveling waves, with R tuning their relative contributions**.

---

### Key Features

#### 1. Point Initialization

The medium is represented by discrete points randomly distributed in 2D space. The function `create_points_pos` generates these points, allowing control over the number and range of points along the x- and y-axes:

```python
points_pos = create_points_pos(x_num, y_num, x_axis, y_axis)
```

#### 2. Wave Propagation

The wave equation **determines the displacement of each point over time**. The longitudinal and transverse displacements are updated in each animation frame:
$$\text{gap} = R \cos(kx - \omega t) + (1 - R) \cos(kx + \omega t)$$
These displacements are applied to the x- and y-coordinates of each point:

```python
arr[i][0] += gap  # Longitudinal motion
arr[i][1] += gap  # Transverse motion
```

#### 3. Visualization

An animated scatter plot visualizes the wave propagation. The function `animate` updates the points’ positions and dynamically renders the wave:

```python
ani = animation.FuncAnimation(fig=fig, func=animate, frames=100, interval=30)
```

For static views, the wave can also be plotted at specific times using:

```python
plot_wave_at_time(t, points_pos)
```

#### 4. Adjustable Parameters

Key wave parameters include:

- **Wave frequency** (`wave_frequency`): Governs oscillation speed.
- **Wavelength** (`wave_len`): Sets spatial periodicity.
- **Directional parameter** (`R`): Determines the relative strength of opposing wave directions.

---

### Physical Interpretation

The program demonstrates:

- **Longitudinal Waves**: Oscillation along the direction of wave propagation.
- **Transverse Waves**: Oscillation perpendicular to the propagation direction.
- **Superposition**: Interaction of leftward and rightward traveling waves.

---

### Applications

This simulation can model acoustic waves, surface waves, or elastic waves in various media. The program’s versatility enables exploration of wave phenomena like standing waves or resonance.

---

This explanation balances technical precision and clarity, staying under 500 words. Let me know if further details are needed!



---

## Simulation of Wave Superposition

#### Purpose

The program simulates and visualizes the propagation and superposition of two traveling waves in one dimension. It demonstrates wave interference by summing the displacements of two sinusoidal waves.

---

### Wave Solution

The waves are described by:
$$y_1(x, t) = A_1 \cos\left(\frac{2\pi}{\lambda_1} (x - v_1 t) + \phi_1 \pi\right)$$$$y_2(x, t) = A_2 \cos\left(\frac{2\pi}{\lambda_2} (x + v_2 t) + \phi_2 \pi\right)$$
Where:

- A1,A2: Amplitudes of the waves.
- λ1,λ2: Wavelengths.
- v1,v2: Wave speeds.
- ϕ1,ϕ2: Phase shifts.
- x, t: Position and time.

The total displacement at any point is the sum of the two waves:
$y_{\text{sum}}(x, t) = y_1(x, t) + y_2(x, t)$

---

### Program Workflow

1. **Wave Parameters**: The parameters $A_1, A_2, \lambda_1, \lambda_2, v_1, v_2, \phi_1, \phi_2$ are defined to control the properties of the two waves:
    
    ```python
    plot_animated_waves(4.0, 1.0, 3.0, 2.0, 0.5, 0.0, 1.5, 2.5)
    ```
    
2. **Wave Propagation**: At each time step t, the program calculates the displacement for both waves and their superposition:
    
    ```python
    y1 = amplitude1 * np.cos(2 * np.pi / lambda1 * (x - speed1 * t) + phi1 * np.pi)
    y2 = amplitude2 * np.cos(2 * np.pi / lambda2 * (x + speed2 * t) + phi2 * np.pi)
    summed_wave = y1 + y2
    ```
    
3. **Visualization**:
    
    - Three curves are plotted:
        - Wave 1 (blue, dashed).
        - Wave 2 (green, dashed).
        - Superposition (red, solid).
    - The animation updates these curves dynamically over time:
        
        ```python
        ani = animation.FuncAnimation(fig, animate, init_func=init, frames=200, interval=60, blit=True)
        ```
        

---

### Physical Interpretation

- **Wave Interference**: The superposition demonstrates **constructive and destructive interference:**
    
    - **Constructive**: When peaks of both waves align, **amplifying** the displacement.
    - **Destructive**: When a peak of one wave aligns with a trough of the other, **reducing** displacement.
- **Traveling Waves**: **Each wave propagates independently**, one to the left and the other to the right, creating complex patterns in the superposition.
    

---

### Applications

This simulation **illustrates principles of wave interference**, traveling waves, and beats. It has applications in acoustics, optics, and quantum mechanics, providing insights into phenomena like standing waves and wave packets.

---

This explanation captures the essence of the program within 500 words. Let me know if more details are needed!


## Summary

### **1. NumericSimulation.py**

#### **Key Idea**:

- Simulates a **1D string wave** using the **finite difference method (FDM)**.

#### **How the Program Works**:

- **Wave Equation**: Solves $\frac{\partial^2 A}{\partial t^2} = c^2 \frac{\partial^2 A}{\partial x^2}$ numerically.
- **Finite Difference Approximation**: $A_{i+1, j} = 2A_{i, j} - A_{i-1, j} + C^2 (A_{i, j+1} - 2A_{i, j} + A_{i, j-1})$
- **Stability**: Enforces $C = \frac{c \Delta t}{\Delta x} \leq 1$.
- **Visualization**: Animates the displacement of the string over time.

#### **When to Use**:

- Problems requiring **numerical wave solutions**.
- Demonstrating **finite difference approximation** or Courant stability.

---

### **2. AcousticsWave.py**

#### **Key Idea**:

- Models **2D wave fields** with **longitudinal and transverse components**.

#### **How the Program Works**:

- **Wave Equation**: $\text{gap} = R \cos(kx - \omega t) + (1 - R) \cos(kx + \omega t)$
    - Updates each point’s x and y positions dynamically.
    - Combines longitudinal (along x) and transverse (along y) motion.
- **Random Points**: The wave propagates through points distributed randomly in 2D space.
- **Visualization**: Animates how the points move dynamically to form a wave.

#### **When to Use**:

- Problems involving **complex wave propagation**, sound waves, or 2D motion.

---

### **3. WaveSuperposition.py**

#### **Key Idea**:

- Demonstrates **superposition of two sinusoidal waves**.

#### **How the Program Works**:

- **Wave Equations**: 
  $y_1(x, t) = A_1 \cos\left(\frac{2\pi}{\lambda_1}(x - v_1 t) + \phi_1\pi\right)$  $y_2(x, t) = A_2 \cos\left(\frac{2\pi}{\lambda_2}(x + v_2 t) + \phi_2\pi\right)$
    - Calculates the **sum** of the two waves: $y_{\text{sum}}(x, t) = y_1(x, t) + y_2(x, t)$
    - Animates individual waves and their sum over time.
- **Customization**: Parameters like amplitude, wavelength, phase, and speed are adjustable.

#### **When to Use**:

- Problems focusing on **wave interference**, beats, or **constructive/destructive superposition**.

---

### Memory Aid

1. **Numeric Simulation**:
    
    - **What it Simulates**: String wave.
    - **Key Method**: Finite difference method (FDM), Courant stability.
    - **Output**: Animated string displacement.
2. **Acoustics Wave**:
    
    - **What it Simulates**: 2D wave field.
    - **Key Method**: Longitudinal + transverse motion, random points in 2D.
    - **Output**: Points move dynamically to form waves.
3. **Wave Superposition**:
    
    - **What it Simulates**: Interference of two waves.
    - **Key Method**: Sum of sinusoidal waves.
    - **Output**: Clean plots of waves + superposition.

---

These concise explanations include both how the programs work and their focus, making them easier to memorize while providing enough detail for the exam. Let me know if you need further clarifications!
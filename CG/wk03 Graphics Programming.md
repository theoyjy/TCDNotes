#### Debugging
Make sure shader works fine with just assign pure color

>[!info] OpenGL
>able to access and control the graphics subsystem of the device upon which it runs
>* cross platform
>* Only does 3D graphics
>* *client-server model*:
> 	 client is your app, server is OpenGL implementation on your GPU/network Graphics card
> * **state machine**
> * 
> ![[wk03 Graphics Programming-20240924123044336.webp|300]]

#### OpenGL Global State Machine
Most parameters are **persistent**
- Values *remain unchanged until we explicitly change* them through functions that alter the state
	- for example, color, lighting, blending

#### Primitives
Objects are created form Basic Primitives
- Line Based Primitives
	![[wk03 Graphics Programming-20240924123336773.webp|400]]
* Polygon Primitives
  ![[wk03 Graphics Programming-20240924123430057.webp|400]]

#### Conventions
- all func names begin with `gl` or `glut`
- constants begin with `GL_` `GLU_` `GLUT_`
- ==Function names can encode parameter types, e.g. `glVertex`:==
	- `glVertex2i(1, 3)`
	- `glVertex3f(1.0, 3.0, 2.5)`

#### Drawing Process
##### 1. Clear the screen:
`glClearColor(0.0, 0.0, 0.0, 0.0)`
`glClear(GL_COLOR_BUFFER_BIT)`
- and clear color and depth buffers
  - `glClearColor(0.0, 0.0, 0.0, 0.0);` 
  - `glClearDepth(0.0);` 
  - `glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);`
- You can also clear the accumulation and stencil buffers. 
  - `GL_ACCUM_BUFFER_BIT `and `GL_STENCIL_BUFFER_BIT`
##### 2. Draw the Screen
specify the color, buffers

##### 3. Complete Drawing
`glFinish()` or `glFlush()` to tell OpenGL you have finished drawing your scene

##### 4. Swap Buffers


#### `GLUT`
##### Event loop
![[wk03 Graphics Programming-20240924124452576.webp|500]]

```
#include <glm.hpp>
#include <gtc/type_ptr.hpp>
#include <gtc/matrix_transform.hpp>
```

#### Shaders
A shader is a program with main as its entry point 
- Has source code (text file)
- Cg, HLSL and GLSL  GLSL is a C-like language
- Is compiled into a program 
- We get back IDs, which are just ints!

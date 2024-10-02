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
- Cg, HLSL and GLSL is a C-like language
- Is compiled into a program 
- We get back IDs, which are just `int`!

##### Qualifiers
`in type variableName;`
`out type variableName;`
`uniform float time;`: shader-**constant** **global** variable from applications, so it stays constant for all vertices or fragments during a single draw call.

##### Vertex Shader
- change position of a vertex
- determine color of a vertex
**must always output vertex locations**
- `gl_Position` is no need to declare `out` since opengl knows about it 

##### Fragment Shader
The input is the output of vertex shader
- determine color of a pixel/fragment
- uses lighting, material, normal

1. Once creating two shaders `GLuint glCreateShader(..)`, we get an ID for each shader
   `GLuint ID = glCreateShader(GL_VERTEX_SHADER)`
   `glShaderSource(id, countm src codem lengths)` bind the code of the shader
2. Then we need to compile the shader together `glCompileShader()`
3. `programID = glCreateProgram`
4. `glAttchShader(programId, shaderId)` do it both for vertex and fragment shaders
5. `glLInkProgram(programId)` actually makes the shader program
6. `glUseProgam(programId)` use this shader when drawing

#### Vertex Buffer Object
Pass objs to GPU
1. opengl generate a memory buffer
   `GLuint buffer;`
   `glGenBuffers(1, &buffer);`
2. `glBindBuffer(GL_ARRAY_BUFFER buffer);` set the buffer active.\
3. `glBufferData(GL_ARRAY_BUFFER, sizeof(data), data, GL_STATIC_DRAW)` loading buffer with data
   - GL_STATIC_DRAW means the data won't change, draw means it's for drawing
   - we can call `glBufferSubData(GL_ARRAY_BUFFER, startPos, sizeof(anotherdateSet), anotherdateSet);`
4. pass data to shader:
   ```c++
   vpos = glGetAttribLocation (programID, “vPosition”); 
   glEnableVertexAttribArray(vpos); 
   glVertexAttribPointer(vpos, 3, GL_FLOAT, GL_FALSE, 0, 0);
   
	cpos = glGetAttribLocation (programID, “vColor”);
	glEnableVertexAttribArray(cpos);
	glVertexAttribPointer(cpos, 4, GL_FLOAT, GL_FALSE, 0, (BUFFER_OFFSET(numVertices * 3 * sizeof(Glfloat)));
/// shader
	in vec4 vPosition;
	in vec4 vColor;
	out vec4 color;
	void main()
	{
		gl_Position = vPosition;
		color = vColor;
	}
	```

#### Index Buffer
get rid of redundant vertexes, instead record the the index of vertices associated with a triangle

#### VAO

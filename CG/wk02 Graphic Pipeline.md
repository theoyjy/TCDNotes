- A Triangle has 3 vertices and a normal
- *Vertex Buffer* contains all the vertices related to the obj
- Modelling Programs: create 3D models
- Scanning Tech:
	- Photogrammetry: 
	  take photos of an obj from all angles, different heights under multiple lighting conditions. Basically it's trying to subtract the lighting effect on the objects, so we can apply light on the model later on.
	- Structured light scanning
	- Laser Scanning:
	  Using the time for light to travel from cam to surface, to figure out the depth of points.
	- Gaussian Splatting:
	  Sparce Point Cloud, each sparce has its own shape and color.

>[!info] Rendering
>The process by which a cp creates images from models of objects
>And It's all Graphics Pipeline's job.

- Fixed Function Pipeline -- OpenGL 1
  Lack of programmability
### Graphics Programmable Pipeline

Introduce the Fragment Shader for much more *lightings*, *textures*.
#### Coarse Division:
1. Application Stage:
   - Developer has full control
     Setting up on the vertex and programs. Basically ends up with Vertex buffer
2. Geometry Stage
   ![[wk02-20240924120601697.webp|500]]
	1. Vertex Shader(Programmable)
	   1. Model & View Transformation
	      - Scale objs to the suitable scale.
	      - Place objs in the desired locations
	      - Place camera in the right place.
	   2. Vertex Shading
	      - focus on the contribution of light, which means the effect of a light on a material
	      - don't care about the polygons at this stage, only on the vertices, vertices has material, color info
	      - It's not the good enough for lighting, fancy effect should be done later on
	   3. Projection
	      - Determine how 3D objs being view in 2D
	      - Perspective or orthographic viewing
	2. Clipping
	   Eliminate the objs outside of the frustrum
	3. Screening Mapping
	   Convert 2D Normalized Coordinates(range from -1 to 1) to 2D Screen/pixel(0,0) to (x resolution, y resolution)
3. The Rasterized Stage
    *compute and set colors for the pixels covered by the object*
   ![[wk02-20240924120631550.webp|500]]
   1. Triangle Traversal
	- Which pixels are inside a triangle
	- Each pixel that has its center covered by the triangle is checked
	- A *fragment* is generated for *the part of the pixel that overlaps* the triangle(**can be hidden or visible**) -- potential pixels
	- Triangle vertices interpolation'
2. Pixel Shading
	* Per-pixel shading computations performed
	* End result is *one or more colors to be passed to the next stage*
3. Merging
	* Information for each pixel is stored in the color buffer
	* *Combine* the fragment color produced by the shading stage with the color currently stored in the buffer
	* This stage is also responsible for resolving visibility
		* Using the z-buffer
		* Z-Buffer stores the depth of each pixel, darker means closer

#### Double Buffering
 To avoid perception of primitives being rasterized, double buffering is used
 Once complete, contents are swapped with the front buffer
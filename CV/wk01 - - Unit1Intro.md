# Syllabus
- Intro to CV
	- Intro
	- Applications
	- Linear Filters
	- Edge Detection
	- Image Pyramids
- Feature Detection and Matching
	- matching: telling/interpreting/understanding the meaning of features
		- next step: decision making
- Multiple Views and Motion
	- **depth** gets from multiple views, from occluding
- ML for CV
- DL for CV applications

# Introduction

>[!question] Definition
>CV enables machines to interpret and understand visual information from the world, similar to how humans perceive and process images.
>
>Understand the scene in order to take actions: perception, planning, reasoning.
>
>Understand the location, materials of objects

## Image Acquisition

>[!info] Energy - illumination
>photon can be measured
>	by Energy $E$
>	frequency $f$
>	wavelength $\lambda$
>$\lambda = \frac {c} {f} \quad  E =h \times f  \quad E = \frac {h \times c} {\lambda}$

Visible light is just small part of light. If $\lambda < visible light$, $f$ increases, $E$ increases


>[!info] The lens
>$\frac {1} {g} + \frac {1} {b} = \frac {1} {f}$
>g is distance between obj and lens
>b is the dis between lens and sensor
>f is focal length
>g is fairly long, could be omitted, so $b \approx f$
>- Depth of Field: change g without need to change b, the photo is still good

#### Image Capture - Sensor
##### Brightness 
* Sensor is nothing but illumination energy capacitor 
* 1 pixel - one sensor
* More *closer* sensors are, higher resolution will be
* distance of the sensors is **dot pitch**
* all pixel values is 8 bits(0~255)
* *Shutter* to prevent over amount of light or information.
* longer exposure time  -> more light captured -> image becomes lighter
  - correctly, over, under, motion blur
##### Color
- Capture RGB(24 bits, 3 channels), Shade of Gray.
- when light is very low, **Rods** capture the **Shade of Gray**
- White light is proper light, that make you can see all colors(all wavelengths)
- (0,0,0) not capturing any light is black, (255,255,255) is white
- Normalized RGB
- **Hue and Saturation**
  - Hue is actually angles.
  - Saturation is the purity of the color
  - ![[wk01 - - Unit1Intro-20240918093908763.webp|300]]

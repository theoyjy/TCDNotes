# Summary

The dissertation addresses the common problem of turning pages in sheet music by developing an iOS application called `EyeGaze`. This application uses eye gaze tracking to trigger page-turning animations, aiming to create a seamless and hands-free experience for musicians. Two eye gaze tracking methods, `iTracker` and `SeeSo`, are evaluated, along with three page-turning animation styles: scrolling, single animation, and double animation.

While the accuracy of the eye gaze detection methods is acknowledged to be imperfect, the dissertation finds that the mechanisms for triggering page turns have a more significant impact on user experience. The experimental results demonstrate that the scrolling animation performs best overall. This superior performance is attributed to the scrolling animation’s lower reliance on precise gaze predictions. Unlike the other animation styles, the scrolling animation does not require pinpointing a precise gaze location to trigger a page turn. Instead, it relies on identifying the user's general gaze location within broadly defined regions of the screen, allowing for smooth and less disruptive page transitions even with fluctuating gaze data.

# Business Idea
1. Free hand reading for instructions, such as model building, crafts, DIY projects, cooking, and even musical instruments
   we can add features like when users are staring at a point for a long time, the system can zoom in that part
   
2. Eye gaze detection for accessibility
4. TV control free hand by eye gaze detection and voice input
5. Movie, music theater analyze audiences' preferences on contents by applying eye gaze detection (Ethic problems)

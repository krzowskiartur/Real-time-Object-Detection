# SawTracker – Real‑time Moving Saw Detection

A computer vision project that detects and tracks a moving saw in a video file using **OpenCV** and **HSV color masking**. The program finds the largest contour (the ball), marks its center with a crosshair, and displays the processed video in real time.

##  Features
- HSV color filtering to isolate the saw  
- Morphological operations (dilation + erosion) to reduce noise  
- Contour detection to find the largest object  
- Center point calculation and visualization  
- Resizable output window

- ## How It Works
1. The video is read frame by frame.  
2. Each frame is converted from BGR to **HSV** color space.  
3. A color range mask isolates the ball (customizable).  
4. Morphological operations clean up the mask.  
5. Contours are detected – the largest contour is assumed to be the ball.  
6. The center of that contour is calculated and drawn as a blue cross.  
7. The annotated frame is displayed. Press `q` to quit.

## Requirements
- Python 3.7+  
- OpenCV (`opencv-python`)  
- NumPy  

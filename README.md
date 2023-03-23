# Real Time Pose Estimation  
  
## Description  
This code uses the Mediapipe library to extract pose landmarks from a live video stream captured using the webcam. The landmarks are the 33 specific points on the human body, such as the nose, eyes, shoulders, elbows, wrists, hips, knees, and ankles. It then calculates the speed of movement and the direction of movement of the body in real-time using the landmarks data. The majority vote algorithm is utilized to determine the overall direction of movement.  
The output can help in analyzing the body posture and movement patterns, and it can be used for various applications such as sports training, health monitoring, and gaming.  
  
 ![image](https://user-images.githubusercontent.com/100927079/227047436-729eedfc-7c5d-4b12-9e6e-43b6762f564f.png)  
  
### Displaying on the video window:  
- The mean speed in meters per second along each axis (x, y, z).  
- The direction of movement (**forward**, **backward** or **not moving**).  
   
 ## Calculations  
- Each one of the 33 landmarks can be represented by a set of three coordinates in three-dimensional space, denoted as $(x, y, z)$. The corresponding covariance matrix of the landmark, denoted as $\Sigma$, is defined as:  
```math  
\Sigma = 
\begin{bmatrix}
    \operatorname{var}(x) & \operatorname{cov}(x, y) & \operatorname{cov}(x, z)\\
    \operatorname{cov}(x, y) & \operatorname{var}(y) & \operatorname{cov}(y, z)\\
    \operatorname{cov}(x, z) & \operatorname{cov}(y, z) & \operatorname{var}(z)
\end{bmatrix}
```  
denote by $\lambda$ the largest eigenvalue of $\Sigma$, and by $\vec{v}$ its corresponding eigenvector, then $\vec{v}$ represents the direction of the maximum variance which is also the direction of the most significant movement of the landmark.  

 - To calculate the speed of movement of a landmark in each direction (x, y, and z) in the video stream, we can use the `Timestamp` class to obtain the time stamps of the current and previous frames. Let $\Delta t$ denote the time difference between these two time stamps. We can also obtain the location of the landmark in both the current and previous frames as $(x_t, y_t, z_t)$ and $(x_{t-1}, y_{t-1}, z_{t-1})$, respectively.  
The distance traveled by the landmark in each direction can be calculated as follows:  
$$\Delta x = |x_t - x_{t-1}|, \Delta y = |y_t - y_{t-1}|, \Delta z = |z_t - z_{t-1}|$$  
where $| \cdot |$ denotes the absolute value.  
The speed of the landmark's movement in each direction can then be calculated using the Speed Distance Time formula, where:  
 $$s_x = \frac{\Delta x}{\Delta t}, s_y = \frac{\Delta y}{\Delta t}, s_z = \frac{\Delta z}{\Delta t}$$  
 
   
 ## TODO
 - Try different methods to calculate the overall direction of movement from the landmarks' directions, other than the majority vote (perhaps methods that assign different weights to different landmarks)  
 - Recognize some gestures such as hand gestures (waving, pointing, etc.) and facial expressions (smiling, raising eyebrows, etc.)  
   
   
 # Run and Install  

 

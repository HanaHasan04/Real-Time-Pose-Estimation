# Real Time Pose Estimation  
  
This code uses the Mediapipe library to extract pose landmarks from a live video stream captured using the webcam. The landmarks are the 33 specific points on the human body, such as the nose, eyes, shoulders, elbows, wrists, hips, knees, and ankles. It then calculates the speed of movement and the direction of movement of the body in real-time using the landmarks data. The majority vote algorithm is utilized to determine the overall direction of movement.  
The output can help in analyzing the body posture and movement patterns, and it can be used for various applications such as sports training, health monitoring, and gaming.
  
### Displaying on the video window:  
- The mean speed in meters per second along each axis (x, y, z).  
- The direction of movement (forward, backward, not moving).  
   
   
 ![image](https://user-images.githubusercontent.com/100927079/227047436-729eedfc-7c5d-4b12-9e6e-43b6762f564f.png)  
   
 ## Install
 ## TODO:
 - Try different methods to calculate the overall direction of movement from the landmark's directions.  
 

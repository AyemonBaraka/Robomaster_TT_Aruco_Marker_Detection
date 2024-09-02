# Robomaster Tello Talent – ArUco Marker Detection and Video Recording

The project involves the Tello Talent performing a series of actions, including taking off, displaying messages on its matrix, rotating 360 degrees, detecting ArUco markers, recording a video, and finally landing.


## Components:

The components used in this project are:
1.	Robomaster Tello Talent
2.	ArUco Markers
   
![image](https://github.com/user-attachments/assets/947a33d6-29b2-4561-8df8-778627a8acfa)
![image](https://github.com/user-attachments/assets/8fbdcfaa-f156-484a-9fd8-6563189c9a07)


## Sub tasks:
1.	Takeoff and Display "Hello":
   The Tello Talent initiates by taking off from a stable surface. Once it is in air, the drone's display matrix showcases the message "Hello." This action serves as an indication of successful takeoff.
2.	ArUco Marker Detection:
   After displaying the greeting message, the Tello Talent proceeds to rotate 360 degrees horizontally. While rotating, the Tello Talent utilizes its built-in camera and computer vision techniques implemented using OpenCV in Python to search for ArUco markers within its field of view. 
3.	Marker Detection Outcome
   When the Tello Talent fails to detect an ArUco marker, it updates its display matrix with a frown face. Conversely, upon successfully detecting an ArUco marker, it updates its display matrix with a happy smiley face.
5.	Video Recording
   Following the detection, the Tello Talent continues its 360-degree rotation while simultaneously initiating the video recording process. Once the video recording is complete, the Tello Talent lands safely.

   
# Demo Video: https://youtu.be/HPvbXHlDvX0

## Video Recorded by Robomaster Tello Talent in AISL Summer camp 2023 (Vegas Stem Lab 2023) during Demo: 
https://youtu.be/DsnT45xsGOg

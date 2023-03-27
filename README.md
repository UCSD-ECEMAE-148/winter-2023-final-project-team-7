## UCSD ECE/MAE-148 2023 Winter Team 7

# Team Members
**Francisco Downey (BENG), Jonathan Xiong (ECE), Nicholas Preston (MAE), Karthik Srinivasan (MAE)**

# Final Project Overview
![GPS points](https://user-images.githubusercontent.com/103704890/227807683-064f8b95-401a-4239-9933-644017986b55.png)

For our final project, we made our car drive from point A to B, given starting and ending GPS points. 

# Assembled Car Design
![final assembled car](https://user-images.githubusercontent.com/103704890/227806766-31cf95f4-d0e6-4ada-861e-9daa5a33eac2.jpg)
LIDAR was set in the front of the car. This was an easy decision for the team since we cared for varying obstacles crossing the points the comprise the path from Point A to Point B. Essentially, it was only important to care for obstacles that come into the front of the moving car. GNSS was secure near the center of the car with the antenna placed high and toward the rear.

# DonkeyCar - 3 Autonomous Laps
https://user-images.githubusercontent.com/103704890/227807530-35ed2ea5-2bc0-4b8b-983d-ca6bed659390.mp4

# ROS2 Line Following - 3 Autonomous Laps
https://user-images.githubusercontent.com/103704890/227801950-dfd60ddd-300e-4af8-9878-c62338184269.mp4

# ROS2 Left Lane - 3 Autonomous Laps
https://user-images.githubusercontent.com/103704890/227804039-c1aafb7a-8bf6-4f86-89cf-1fa21c7ea5d2.mp4

# GPS - 3 Autonomous Laps
https://user-images.githubusercontent.com/103704890/227804055-d9c3ccce-ef8d-427d-a6b6-e1db12eba440.mp4
Important to note for the final project, many of the configurations that were found to work in the GPS 3 autonomous laps were used for the final project. The GPS points making up the path were 0.55 meters apart. The nature of the csv points used in the final project matched the one used for this assignment. This allowed the project to move faster as the configurations did work out. See section Algorithmic Design of Directing Car from GPS point A to B.

# Final Project
**Plan: Go from point A to B with object detection.**
<img width="854" alt="PointAtoB" src="https://user-images.githubusercontent.com/103704890/227807817-2b348d11-a5f9-4646-9f11-02e7379b1f43.png">

**Overview**
Originally, we were going to have LIDAR detect objects in front of the car so the car can see what it needs to go around. However, we did not have enough time to see how to use LIDAR, since there was no assignment with it and not enough time at end of quarter given rain. We, however, got quite experienced with the GPS functionality of the car. Using the GPS modules, we were able to direct the car using a path of car-readble GPS coordinates.

**Algorithmic Design of Directing Car from GPS point A to B**
By the end of the quarter, we wrote a program, AtoB.py, which requires two sets of GPS coordinates as inputs. This program generates a .csv file containing a path of GPS coordinates about .55 meters apart from point A to B. These generated points latitude longitude formatted and relative to the base station antenna. The inputted absolute (planet's) GPS coordinates, thus, needed to be translated to these relative coordinates and converted to rectangular from polar positions. It took some testing to increase the precision of the translation as we did not know the exact conversion constants.

**Demonstration**

https://user-images.githubusercontent.com/103704890/227807009-ec59e649-c068-4543-9dba-9ddb16ea8ee5.mp4




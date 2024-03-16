README file for ROBT414 Programming Assignment 2 by Zarema Balgabekova

INTRODUCTION
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
The purpose of the program is to implement a "Follow me" application on a Pepper robot using Python NaoQi and then test it on a virtual robot with the help of Choregraphe.

PROGRAM DESCRIPTION
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
*Robot waves hello with its right arm
*Robot says "Hi, human! I want to come with you" (for a virtual robot, the phrase is displayed on a screen as a text)
*Robot raises its hand for 5 seconds for a user to hold it
*Robot can move forward with different speeds (It is controlled by LShoulderPitch joint) and stop: It moves faster if robot's arm is close to 'up' position
												   It moves slower if it is at about 90-degree angle
												   It stops if robot's arm is almost dropped
												   In other cases it moves with normal speed
*Robot can turn left and right: It turns left if LWristYaw is about 90 degrees 
        			It turns right if LWristYaw is about -90 degrees 

REQUIREMENTS
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
*Python 2.7
*Choregraphe
*Python libraries: naoqi, time, math

INSTALLATION
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
To install Python Naoqi and Choregraphe, visit https://developer.softbankrobotics.com/

TROUBLESHOOTING
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
It may be needed to change IP and port if they do not coincide with '127.0.0.1' and 9559. To see your port and IP, open Choregraphe and then click on Connect->Connect to.


#Importing used libraries
from naoqi import ALProxy
import time
import math

#Function for waving hello
#Animation was created in Choregraphe, and then animation values were exported
def waving_hello():
        names = list()
        times = list()
        keys = list()

        names.append("HeadPitch")
        times.append([1.92])
        keys.append([[-0.384578, [3, -0.653333, 0], [3, 0, 0]]])

        names.append("HeadYaw")
        times.append([1.92])
        keys.append([[0.0183391, [3, -0.653333, 0], [3, 0, 0]]])

        names.append("HipPitch")
        times.append([1.92])
        keys.append([[-0.123518, [3, -0.653333, 0], [3, 0, 0]]])

        names.append("HipRoll")
        times.append([1.92])
        keys.append([[0.00661768, [3, -0.653333, 0], [3, 0, 0]]])

        names.append("KneePitch")
        times.append([1.92])
        keys.append([[0.00165148, [3, -0.653333, 0], [3, 0, 0]]])

        names.append("LElbowRoll")
        times.append([1.92])
        keys.append([[-0.201082, [3, -0.653333, 0], [3, 0, 0]]])

        names.append("LElbowYaw")
        times.append([1.92])
        keys.append([[-1.43489, [3, -0.653333, 0], [3, 0, 0]]])

        names.append("LHand")
        times.append([1.92])
        keys.append([[0.500915, [3, -0.653333, 0], [3, 0, 0]]])

        names.append("LShoulderPitch")
        times.append([1.92])
        keys.append([[1.60187, [3, -0.653333, 0], [3, 0, 0]]])

        names.append("LShoulderRoll")
        times.append([1.92])
        keys.append([[0.092563, [3, -0.653333, 0], [3, 0, 0]]])

        names.append("LWristYaw")
        times.append([1.92])
        keys.append([[-0.386955, [3, -0.653333, 0], [3, 0, 0]]])

        names.append("RElbowRoll")
        times.append([1.92])
        keys.append([[0.211185, [3, -0.653333, 0], [3, 0, 0]]])

        names.append("RElbowYaw")
        times.append([1.92])
        keys.append([[1.46913, [3, -0.653333, 0], [3, 0, 0]]])

        names.append("RHand")
        times.append([0.96, 1.48, 1.92])
        keys.append([[0.87, [3, -0.333333, 0], [3, 0.173333, 0]], [0.97, [3, -0.173333, 0], [3, 0.146667, 0]], [0.566928, [3, -0.146667, 0], [3, 0, 0]]])

        names.append("RShoulderPitch")
        times.append([0.96, 1.48, 1.92])
        keys.append([[-1.68424, [3, -0.333333, 0], [3, 0.173333, 0]], [-1.37706, [3, -0.173333, 0], [3, 0.146667, 0]], [-1.37706, [3, -0.146667, 0], [3, 0, 0]]])

        names.append("RShoulderRoll")
        times.append([0.96, 1.16, 1.48, 1.92])
        keys.append([[-0.0506145, [3, -0.333333, 0], [3, 0.0666667, 0]], [-0.111701, [3, -0.0666667, 0.0592964], [3, 0.106667, -0.0948743]], [-0.513127, [3, -0.106667, 0], [3, 0.146667, 0]], [-0.107952, [3, -0.146667, 0], [3, 0, 0]]])

        names.append("RWristYaw")
        times.append([0.96, 1.48, 1.92])
        keys.append([[-1.82387, [3, -0.333333, 0], [3, 0.173333, 0]], [-1.22173, [3, -0.173333, -0.359747], [3, 0.146667, 0.304401]], [0.168577, [3, -0.146667, 0], [3, 0, 0]]])

        try:
        # uncomment the following line and modify the IP if you use this script outside Choregraphe.
        #Necessary IP is 127.0.0.1
                motion = ALProxy("ALMotion", "127.0.0.1", 9559)
                #motion = ALProxy("ALMotion")   we comment this line because the script is used outside Choregraphe
                motion.angleInterpolationBezier(names, times, keys)
        except BaseException, err:
                print err

#Defining variables for the use of ALMotion and ALTextToSpeech modules
#We need ALMotion module to move the robot
#We need AlTextToSpeech for the use of tts
textSpeakProxy = ALProxy("ALTextToSpeech", "127.0.0.1", 9559)
motionProxy = ALProxy("ALMotion", "127.0.0.1", 9559)

#Robot waves hello
waving_hello()

#TTS
#Speaking rate was changed to 50% so that we can observe a text for the virtual robot clearly
#If it was 100%, it will disappear too rapidly
textSpeakProxy.say("\\rspd=50\\Hi, human! I want to come with you.")

#LShoulderPitch joint is used for speed change
#LWristYaw joint is used for turning right and left
l_shoulder = "LShoulderPitch"
l_wrist = "LWristYaw"

#Robot raises its left arm for 5 seconds for the user to hold it
fractionMaxSpeed = 0.3
t_end = time.time() + 5
while time.time() < t_end:
        motionProxy.setAngles(l_shoulder, -0.9, fractionMaxSpeed)
        
#if useSensors is true, sensor angles will be returned
useSen = 0
while(1):
        shoulder_rad = motionProxy.getAngles(l_shoulder, useSen)
        wrist_rad = motionProxy.getAngles(l_wrist, useSen)

        #As getAngles() returns joint angles in radians, we convert them to degrees for convenience
        shoulder_deg = shoulder_rad[0]*180/math.pi
        wrist_deg = wrist_rad[0]*180/math.pi

        #Move faster if robot's arm is close to 'up' position
        #Move slower if it is at about 90-degree angle
        #Stop motion if it is almost dropped
        #In other cases move with normal speed
        
        if -119.5 < shoulder_deg < -55:
                motionProxy.move(2.0, 0.0, 0.0)
                print('Faster motion')
                #add 1 second delay to observe motion's change clearly
                time.sleep(1.00)
        elif -5 < shoulder_deg < 5:
                motionProxy.move(0.5, 0.0, 0.0)
                print('Slower motion')
                time.sleep(1.0)
        elif 85 < shoulder_deg < 119.5:
                motionProxy.move(0.0, 0.0, 0.0)
                print('Stop motion')
                time.sleep(1.0)
        else:
                motionProxy.move(1.0, 0.0, 0.0)
                print('Normal motion')
                time.sleep(1.0)

        #Turn left if LWristYaw is about 90 degrees 
        #Turn right if LWristYaw is about -90 degrees 
        if (85 < wrist_deg < 95):
                motionProxy.moveTo(0.0, 0.0, 1.57)
                print('Turn left')
                time.sleep(1.00)   
        elif  -95 < wrist_deg < -85:
                motionProxy.moveTo(0.0, 0.0, -1.57)
                print('Turn right')
                time.sleep(1.00)
              


        

        


        
        


  

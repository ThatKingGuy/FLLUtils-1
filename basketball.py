from pybricks.hubs import EV3Brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# Create objects here.
ev3 = brick()

# _____________________________________________
#/                                             \
#|1 - left color sensor   left medium motor - D |
#|                                              |
#|2 - gyro                 left large motor - C |
#|                                              |
#|3 - color chip          right large motor - B |
#|                                              |
#|4 - right color sensor right medium motor - A |
#\_____________________________________________/

# Initialize the motors.
R_att_motor = Motor(Port.A)
R_motor = Motor(Port.B,Direction.COUNTERCLOCKWISE)
L_motor = Motor(Port.C,Direction.COUNTERCLOCKWISE)
L_att_motor = Motor(Port.D)

#Initialize the sensors.
L_color_sensor = ColorSensor(Port.S1)
gyro = GyroSensor(Port.S2)
chip_color_sensor = ColorSensor(Port.S3)
R_color_sensor = ColorSensor(Port.S4)

# Initialize the drive base.
wheel_diameter=62.4
axle_track=104
robot = DriveBase(L_motor, R_motor, wheel_diameter, axle_track)

# Reset the motor angles.
L_motor.reset_angle(0)
R_motor.reset_angle(0)
L_att_motor.reset_angle(0)
R_att_motor.reset_angle(0)

# Reset the gyro sensor.
gyro.reset_angle(0)


#########################################################
# Write your program below.
#########################################################

#Function for gyro straight to bench-
def gyroStraight(targetAngle, rotations, gain = 3, speed = -260):
    while int(L_motor.angle()) > rotations * -360:
        # ^While the robot hasn't gone forward 2.5 rotations...
        angle = gyro.angle()
        robot.drive(speed, (targetAngle - angle)*gain)
    # ^Go forward using gyro
    robot.stop()
    L_motor.brake()
    R_motor.brake()
    L_motor.reset_angle(0)
    R_motor.reset_angle(0)
    # ^Reset angles and brake

#########################################################
def followLine(rotations, threshold = 23, speed = 100, gain = 1):
    sensor = ColorSensor
    robot.stop()
    L_motor.reset_angle(0)
    R_motor.reset_angle(0)
    while int(L_motor.angle()) < rotations * 360:
        light = R_color_sensor.reflection()
        robot.drive(speed, (threshold - light )*gain)
    robot.stop()
    L_motor.brake()
    R_motor.brake()
    L_motor.reset_angle(0)
    R_motor.reset_angle(0)
####################################################3###
def followLineStoponLine(Lthreshold = 80, threshold = 10, speed = 100, gain = 1):
    sensor = ColorSensor
    while L_color_sensor.reflection() < Lthreshold:
        light = R_color_sensor.reflection()
        robot.drive(speed, (threshold - light )*gain)
    robot.stop()
    L_motor.brake()
    R_motor.brake()
    L_motor.reset_angle(0)
    R_motor.reset_angle(0)
####################################################3###
def lineSquare(threshold=15,speed=50):
    
    while ((L_color_sensor.reflection() > threshold) and (R_color_sensor.reflection() > threshold)):
        robot.drive(speed, 0)
        wait(10)
    robot.stop()
    L_motor.brake()
    R_motor.brake() 
    wait(100)

    if (L_color_sensor.reflection() <= threshold):
        while (R_color_sensor.reflection() > threshold):
            R_motor.run(100)
            wait(10)
        L_motor.brake()
        R_motor.brake()
        
    elif (R_color_sensor.reflection() <= threshold):    
        while (L_color_sensor.reflection() > threshold):
            L_motor.run(100)
            wait(10)
        L_motor.brake()
        R_motor.brake()
        
def RUNlineSquare():
    robot.settings(1000)
    i=0
    while (i<3):
        lineSquare()
        robot.straight(-20)
        i+=1

def PR():
    while (True):
        print ("L=",L_color_sensor.reflection(),"   R=", R_color_sensor.reflection())
        wait(500)

######################################################################

def gyroTurn(turnAmount, speed = 150, correction_speed = 30, correction_amount = 2):
    if(correction_amount < 0):
        raise Exception("Correction amount cant be below zero")

    if(gyro.angle() < turnAmount):
        while gyro.angle() < turnAmount:
            angle = gyro.angle()
            L_motor.run(speed)
            R_motor.run(-speed)
        L_motor.brake()
        R_motor.brake()
    else:
        while gyro.angle() > turnAmount:
            angle = gyro.angle()
            L_motor.run(-speed)
            R_motor.run(speed)
        L_motor.brake()
        R_motor.brake()
    
    L_motor.brake()
    R_motor.brake()

    #Correct for overshoot
    times_corrected = 0
    while (times_corrected < correction_amount):
        if(gyro.angle() < turnAmount):
            while gyro.angle() < turnAmount:
                angle = gyro.angle()
                L_motor.run(correction_speed)
                R_motor.run(-correction_speed)
            L_motor.brake()
            R_motor.brake()
        else:
            while gyro.angle() > turnAmount:
                angle = gyro.angle()
                L_motor.run(-correction_speed)
                R_motor.run(correction_speed)
            L_motor.brake()
            R_motor.brake()
        times_corrected += 1
    print(angle)
    L_motor.reset_angle(0)
    R_motor.reset_angle(0)

######################################################################

def benchbasketslide():
    gyro.reset_angle(0)
    L_motor.reset_angle(0)
    R_motor.reset_angle(0)
    gyroStraight(0, 2.3, 3, -260)                             #<This calls the above function to go straight using gyro^
    robot.turn(-60)                                         #turn to get backrest
    robot.turn(60)
    robot.straight(60)                                      #go back
    #robot.turn(-123)                                        #turn to line
    robot.stop()
    gyroTurn(-95)
    robot.straight(320)                                     #straight to line
    lineSquare(15,50)                                       #line square
    robot.straight(-5)                                     #back a little
    robot.turn(-75)
    followLine(1, 15, 100, 1)                              #call function for follow line
    ev3.speaker.beep()
    followLineStoponLine(90, 10, 100, 1)                    #stop when left color sensor senses white line
    ev3.speaker.beep() 
    robot.settings(50, 581, 80, 640)
    robot.straight(-45)                                     #back up a little on line
    robot.turn(-70)                                         #turn towards basketball
    robot.straight(75)                                      #go forwards so that cube gets dropped
    robot.straight(-65)                                      # align for linear actuator
    robot.turn(18)                                          #Turn back for linear actuator
    robot.straight(45)
    R_att_motor.run_until_stalled(-3000, duty_limit=73)     #Lift up basketball, run until stalled
    R_att_motor.run_angle(3000,3300)
    robot.stop()
    robot.settings(300, 581, 80, 640)
    robot.straight(-240)
    robot.turn(100)                                         #slide mission
    robot.straight(-850)                                    #get to launch area
    robot.turn(50)                                         #turn to base
    robot.straight(-50)
    
    

####################################################
####################################################

def run():
    gyro.reset_angle(0)
    benchbasketslide()                                       # Run the whole run
    robot.stop()
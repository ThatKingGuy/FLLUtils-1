import FLLUtils.movement.gyro_steering as gy
import FLLUtils.movement.line_movement as li

from pybricks.hubs import EV3Brick
from pybricks.parameters import Port, Color, Direction
from pybricks.ev3devices import Motor, GyroSensor, ColorSensor
from pybricks.ev3devices import Motor
from pybricks.robotics import DriveBase
import time




#The function that gets called when this mission is selected
def run():
    
    # Initialize the EV3 Brick.
    left_motor = Motor(Port.B)  
    right_motor = Motor(Port.C)
    robot = DriveBase(left_motor,right_motor,56,114)
    ev3 = EV3Brick()
    ev3.speaker.beep()
    left_motor = Motor(Port.B, Direction.CLOCKWISE)  
    right_motor = Motor(Port.C, Direction.CLOCKWISE)
    gyro = GyroSensor(Port.S2)
    robot = DriveBase(left_motor, right_motor, 56, 114)
    gy.resetMotors()
    gy.calibrateGyro()

    arm = Motor(Port.D)
    bucket = Motor(Port.A)

    

    li.followLine(Port.S4, 0.5)

    ########## Mission Start ##########

    #Go straight 4 rotations to the RePlay logo
    gy.gyroStraight(0, 4, 5)
    #Rotatate the motor for 900ms
    arm.run_time(-400, 600)
    arm.stop()
    #Reset motors
    gy.resetMotors()

    # Go foward a tiny bit 
    gy.gyroStraight(0, 0.8)
    #Turn the attachment backwards so it fits under the pull-up bar
    arm.run_time(400, 900)
    #Turn in the direction of the line
    gy.gyroTurn(-60)
    #Turn untill it hits the line
    gy.gyroTurnUntillLine(Port.S4, 11, -50)
    #Reset motors just in case
    gy.resetMotors();
    #Follow line to get close to boccia
    li.followLine(Port.S4, 0.5)
    #Finish following the line
    li.followLineUnitllSquare(Port.S4, Port.S1)
    #Run into boccia
    gy.gyroStraight(-90, 0.8)
    #Align the robot for dropping the cubes
    gy.gyroTurn(-95)

    #Define attachments and drop boccia
    
    arm.run_time(1000, 500)
    arm.stop()

    bucket.run_time(-50, 4000)
    bucket.stop()



    #Go backwards
    gy.gyroStraightBack(-90,0.15)
    # Turn to dance floor
    gy.gyroTurn(-145)
    #Go onto the floor
    gy.gyroStraight(-145, 1.5)
    
    #Dance infinitely
    while(True):
        robot.turn(30)
        robot.turn(-30)
        

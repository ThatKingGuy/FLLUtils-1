import FLLUtils.movement.gyro_steering as gy
import FLLUtils.movement.line_movement as li

from pybricks.hubs import EV3Brick
from pybricks.parameters import Port, Color
from pybricks.ev3devices import Motor, GyroSensor, ColorSensor
from pybricks.ev3devices import Motor
from pybricks.robotics import DriveBase
import time


def run():
    # Initialize the EV3 Brick.
    left_motor = Motor(Port.B)  
    right_motor = Motor(Port.C)
    robot = DriveBase(left_motor,right_motor,56,114)
    ev3 = EV3Brick()
    ev3.speaker.beep()
    left_motor = Motor(Port.B)  
    right_motor = Motor(Port.C)
    gyro = GyroSensor(Port.S2)
    robot = DriveBase(left_motor, right_motor, 56, 114)
    gy.resetMotors()
    gy.calibrateGyro()

    arm = Motor(Port.D)
    bucket = Motor(Port.A)

    ########## Mission Start ##########


    gy.calibrateGyro()
    gy.gyroStraight(3,4)
    gy.gyroStraightForSeconds(3, 2);

    gy.gyroStraightBack(0,1)
    gy.gyroTurn(-45)
    gy.gyroStraight(-45,0.25)
    gy.gyroStraightUntilLine(Port.S4,15,-45)
    ev3.speaker.beep()

    gy.gyroTurn(-90)
    gy.gyroStraightBackForSeconds(-90,1);
    gy.calibrateGyro()
    gy.gyroStraight(0,0.9)
    gy.gyroTurn(-90, 50)

    gy.gyroStraightBackForSeconds(-90,4.75,3,200)
    gy.gyroTurn(-100, 100)

    ev3.speaker.beep()

    motor = Motor(Port.D)
    motor.run_target(1000,-13000)
    motor.stop()

    gy.gyroTurn(-90, 100)  
    gy.gyroStraight(-90,10) 
    robot.stop()

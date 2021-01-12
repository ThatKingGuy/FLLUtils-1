from pybricks import ev3brick as brick
from pybricks.ev3devices import Motor, GyroSensor, ColorSensor
from pybricks.parameters import Port, Stop
from pybricks.tools import print, wait
from pybricks.robotics import DriveBase
import time


left_motor = Motor(Port.B)  
right_motor = Motor(Port.C)
gyro = GyroSensor(Port.S2)
gyro.reset_angle(0)
robot = DriveBase(left_motor, right_motor, 56, 114)

def calibrateGyro():
    gyro.reset_angle(0)

def resetMotors():
    left_motor.reset_angle(0)
    right_motor.reset_angle(0)

def gyroStraight(targetAngle, rotations, gain = 3, speed = -300):
    while int(left_motor.angle()) > -rotations * 360:
        angle = gyro.angle()
        robot.drive(speed, (targetAngle - angle)*gain)
    robot.stop()
    left_motor.brake()
    right_motor.brake()
    resetMotors()

def gyroStraightForSeconds(targetAngle, seconds, gain = 3, speed = -300):
    target = time.time()+seconds
    while time.time() < target:
        angle = gyro.angle()
        robot.drive(speed, (targetAngle - angle)*gain)
    robot.stop()
    left_motor.brake()
    right_motor.brake()
    resetMotors()


def gyroStraightBack(targetAngle, rotations, gain = 3, speed = 300):
    while int(left_motor.angle()) < rotations * 360:
        angle = gyro.angle()
        robot.drive(speed, (targetAngle - angle)*gain)
    robot.stop()
    left_motor.brake()
    right_motor.brake()
    resetMotors()

def gyroStraightBackForSeconds(targetAngle, seconds, gain = 3, speed = 300):
    target = time.time()+seconds
    while time.time() < target:
        angle = gyro.angle()
        robot.drive(speed, (targetAngle - angle)*gain)
    robot.stop()
    left_motor.brake()
    right_motor.brake()
    resetMotors()

def gyroStraightUntilLine(port, light_threshold, targetAngle, gain = 3, speed = -300):
    sensor = ColorSensor(port)
    while sensor.reflection() > light_threshold:
        print(sensor.reflection())
        angle = gyro.angle()
        robot.drive(speed, (targetAngle - angle)*gain)
    robot.stop()
    left_motor.brake()
    right_motor.brake()
    resetMotors()
    
def gyroTurn(turnAmount, speed = 150, correction_speed = 30, correction_amount = 2):
    if(correction_amount < 0):
        raise Exception("Correction amount cant be below zero")

    if(gyro.angle() < turnAmount):
        while gyro.angle() < turnAmount:
            angle = gyro.angle()
            left_motor.run(speed)
            right_motor.run(-speed)
        left_motor.brake()
        right_motor.brake()
    else:
        while gyro.angle() > turnAmount:
            angle = gyro.angle()
            left_motor.run(-speed)
            right_motor.run(speed)
        left_motor.brake()
        right_motor.brake()
    
    left_motor.brake()
    right_motor.brake()

    #Correct for overshoot
    times_corrected = 0
    while (times_corrected < correction_amount):
        if(gyro.angle() < turnAmount):
            while gyro.angle() < turnAmount:
                angle = gyro.angle()
                left_motor.run(correction_speed)
                right_motor.run(-correction_speed)
            left_motor.brake()
            right_motor.brake()
        else:
            while gyro.angle() > turnAmount:
                angle = gyro.angle()
                left_motor.run(-correction_speed)
                right_motor.run(correction_speed)
            left_motor.brake()
            right_motor.brake()
        times_corrected += 1
    print(angle)
    resetMotors()


def gyroTurnUntillLine(port, light_threshold, speed):
    sensor = ColorSensor(port)
    print(sensor.reflection())
    while sensor.reflection() > light_threshold:
        angle = gyro.angle()
        print(angle)
        left_motor.run(speed)
        right_motor.run(-speed)
    left_motor.brake()
    right_motor.brake()

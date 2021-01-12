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

def followLine(port, rotations, threshold = 20, speed = -130, gain = 1):
    sensor = ColorSensor(port)
    while int(left_motor.angle()) > -rotations * 360:
        light = sensor.reflection()
        robot.drive(speed, (threshold - light )*gain)
    robot.stop()
    left_motor.brake()
    right_motor.brake()
    left_motor.reset_angle(0)
    right_motor.reset_angle(0)


def followLineUnitllSquare(port, port2, threshold = 20,threshold2 = 12, speed = -130, gain = 1):
    sensor = ColorSensor(port)
    sensor2 = ColorSensor(port2)
    while int(sensor2.reflection()) > threshold2:
        light = sensor.reflection()
        robot.drive(speed, (threshold - light )*gain)
    print(sensor2.reflection())
    robot.stop()
    left_motor.brake()
    right_motor.brake()
    left_motor.reset_angle(0)
    right_motor.reset_angle(0)


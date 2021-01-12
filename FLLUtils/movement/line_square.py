from pybricks import ev3brick as brick
from pybricks.ev3devices import Motor, GyroSensor, ColorSensor
from pybricks.parameters import Port, Direction, Stop
from pybricks.tools import print, wait
from pybricks.robotics import DriveBase

right_motor = Motor(Port.B)
left_motor = Motor(Port.C)
gyro = GyroSensor(Port.S2)
gyro.reset_angle(0)
robot = DriveBase(left_motor, right_motor, 56, 114)
left_color_sensor = ColorSensor(Port.S1)
right_color_sensor = ColorSensor(Port.S4)

#Line Square

def lineSquare(threshold=15,speed=50):
    
    while ((left_color_sensor.reflection() > threshold) and (right_color_sensor.reflection() > threshold)):
        robot.drive(speed, 0)
        wait(10)
    robot.stop()
    left_motor.brake()
    right_motor.brake() 
    wait(100)

    if (left_color_sensor.reflection() <= threshold):
        while (right_color_sensor.reflection() > threshold):
            right_motor.run(100)
            wait(10)
        left_motor.brake()
        right_motor.brake()
        
    elif (right_color_sensor.reflection() <= threshold):    
        while (left_color_sensor.reflection() > threshold):
            left_motor.run(100)
            wait(10)
        left_motor.brake()
        right_motor.brake()
        
    
    
def RUNlineSquare():
    robot.settings(1000)
    i=0
    while (i<3):
        lineSquare()
        robot.straight(-20)
        i+=1
    

def PR():
    while (True):
        print ("L=",left_color_sensor.reflection(),"   R=", right_color_sensor.reflection())
        wait(500)


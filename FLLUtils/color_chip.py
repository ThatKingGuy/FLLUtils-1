from pybricks.hubs import EV3Brick
from pybricks.parameters import Port, Color
from pybricks.ev3devices import ColorSensor
from pybricks.ev3devices import Motor

# Initialize the EV3 Brick.
ev3 = EV3Brick()


chipSensor = ColorSensor(Port.S3)
 
def waitForAttachmentReady(color):
    i = 0
    print("waiting for attachment...")
    while(chipSensor.color() != color):
        i+=1
        attach.run_time(100, 200)
        attach1.run_time(100, 200)
        attach.run_time(-100, 200)
        attach1.run_time(-100, 200)
        attach.run_time(100, 200)
        attach1.run_time(100, 200)
        attach.run_time(-100, 200)
        attach1.run_time(-100, 200)
        attach.run_time(100, 200)
        attach1.run_time(100, 200)
        attach.run_time(-100, 200)
        attach1.run_time(-100, 200)

    print("attachment found after "+str(i)+" loops")
    ev3.speaker.beep()
    print("waiting for button press...")
    i=0
    while(len(ev3.buttons.pressed()) == 0):
        i+=1
    print("detected button press after "+str(i)+" loops")
#!/usr/bin/env pybricks-micropython

import stepcounter as sc
import boccia as bc
import basketball as bb
from pybricks.hubs import EV3Brick
from pybricks.parameters import Port, Button
from pybricks.ev3devices import Motor
import time


# Initialize the EV3 Brick.
ev3 = EV3Brick()
ev3.speaker.beep()

#These are so we can prevent the menu from cyclying very quickly when held down 
upbounce = False
dbounce = False

#The item we are currently on
currentItem = 1
#The amount of missions there are
maxItem = 3

def say(msg):
    try:
        #Not sure why, but this has been throwing a RuntimeError
        ev3.speaker.say(msg)
    except RuntimeError:
        print("Runtime Error: ")

#A basic function to display the mission on the screen and (try) to say it
def saySelection():
    if(currentItem == 1):
        say("Mission One")
        ev3.screen.clear()
        ev3.screen.draw_text(0, 0, "Mission One")
    if(currentItem == 2):
        say("Mission Two")
        ev3.screen.clear()
        ev3.screen.draw_text(0, 0, "Mission Two")
    if(currentItem == 3):
        say("Mission Three")
        ev3.screen.clear()
        ev3.screen.draw_text(0, 0, "Mision Three")

#In charge of running the correct mission when the button is pressed
def runSelected():
    if(currentItem == 1):
        bb.run()
    if(currentItem == 2):
        sc.run()
    if(currentItem == 3):
        bc.run()
#Say the selection which defaults to 'Mission 1'
saySelection()
attach = Motor(Port.D)
attach1 = Motor(Port.A)

while True:


    #Check if right button is pressed
    if Button.RIGHT in ev3.buttons.pressed():
        if(upbounce == False):
            #Check if the item is the max and loops back to the 1 if it is
            if(currentItem == maxItem):
                currentItem = 1
            else:
                #Else, it just adds one
                currentItem += 1
            saySelection()

            upbounce = True
    else:
        upbounce = False  
    #Check if left button is pressed
    if Button.LEFT in ev3.buttons.pressed():
        if(dbounce == False):
            #Check if the item is 1 and loops back to the max if it is
            if(currentItem == 1):
                currentItem = maxItem
            else:
                #Else, it just removes one
                currentItem -= 1
            saySelection()

            dbounce = True
    else:
        dbounce = False  
    #Check if center button is pressed
    if Button.CENTER in ev3.buttons.pressed():
        #If it is, run the selected mission 
        runSelected()
        #After running, advance menu item

        #Check if the item is the max and loops back to the 1 if it is
        if(currentItem == maxItem):
            currentItem = 1
        else:
            #Else, it just adds one
            currentItem += 1
        saySelection()
        


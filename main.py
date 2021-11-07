import time
#import RPi.GPIO
import datetime

xPins = [6, 13, 19, 26]
yPins = [1, 7, 8, 25]

global xStep
xStep = 0
global yStep
yStep = 0

def step(axis, step):
    for pin in axis:
        GPIO.output(pin, 0)
    GPIO.output(axis[step % len(axis)], 1)

def driveAxis(xTrg, yTrg):
    while(xStep != xTrg and yStep != yTrg):
        #X axis
        if(xStep == xTrg):
            return
        elif(xStep < xTrg):
            step(xPins, xStep-1)
        elif(xStep > xTrg):
            step(xPins, xStep+1)

        #Y axis
        if(xStep == yTrg):
            return
        elif(xStep < yTrg):
            step(yPins, yStep-1)
        elif(xStep > yTrg):
            step(yPins, yStep+1)
        
        #Sleep so the motors can actually do the moving and grooving
        time.sleep(0.01)

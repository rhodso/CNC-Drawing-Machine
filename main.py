import time
import RPi.GPIO as GPIO

xPins = [6,13,19,26]
yPins = [1,7,8,25]

global xStep
xStep = 0
global yStep
yStep = 0

def step(pinAxis, step):
    for pin in pinAxis:
        GPIO.output(pin, 0)
    GPIO.output(pinAxis[step % len(pinAxis)], 1)

def driveAxis(trgX, trgY):
    global xStep
    global yStep
    
    
    while(xStep != trgX and yStep != trgY):
        if(xStep < trgX):
            step(xPins, xStep-1)
            xStep -= 1 
        elif(xStep > trgX):
            step(xPins, xStep+1)
            xStep += 1
        
        if(yStep < trgY):
            step(yPins, yStep-1)
            yStep -= 1
        elif(yStep > trgY):
            step(yPins, yStep+1)
            yStep += 1
    
        time.sleep(0.01)
    
    for pin in xPins:
        GPIO.output(pin, 0)
    
    for pin in yPins:
        GPIO.output(pin, 0)

try:
    print("Setting up GPIO")
    
    GPIO.setmode(GPIO.BCM)

    for pin in xPins:
        GPIO.setup(pin, GPIO.OUT)
    for pin in yPins:
        GPIO.setup(pin, GPIO.OUT)
    
    driveAxis(0,0)
    driveAxis(2,2)

#     driveAxis(2,2)
#     driveAxis(0,2)
#     driveAxis(0,0)
#     driveAxis(2,2)
#     driveAxis(0,0)


except:
    print("Error")

finally:
    for pin in xPins:
        GPIO.output(pin, 0)
    
    for pin in yPins:
        GPIO.output(pin, 0)
    
    GPIO.cleanup()
    print("Done")

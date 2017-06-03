#Aeroponic mister logic
#Controls the turning on and turning off of a pump
#Lights are wired into Relay #3 (Pin 31)
#!/usr/bin/python
import RPi.GPIO as GPIO
import time
from bookshelf import takeOffShelf, putOnShelf
from logData import logData

def runMister():
    "Set pin HIGH for a specified time"
    pumpPin = 31
    pumpTimeKey = "pumpTime"

    pumpTime = takeOffShelf(pumpTimeKey)
    
#configure pins
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    
#set pin HIGH
    GPIO.setup(pumpPin, GPIO.OUT)
    GPIO.output(pumpPin, GPIO.HIGH)
    startTime = time.time()
    logData("Pump", "On", 'Seconds to run: ' + str(pumpTime))
    time.sleep(pumpTime)
    GPIO.output(pumpPin, GPIO.LOW)
    logData("Pump", "Off", 'Seconds ran: ' + str(time.time() - startTime) )           

runMister()
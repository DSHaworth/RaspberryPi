import RPi.GPIO as GPIO
import time

# https://raspberrypi.stackexchange.com/questions/12966/what-is-the-difference-between-board-and-bcm-for-gpio-pin-numbering
# ledPin = 18 #BCM
ledPin = 12 #BOARD

def setup():
    GPIO.setwarnings(False)
    
    #GPIO.setmode(GPIO.BCM)
    GPIO.setmode(GPIO.BOARD)
    
    GPIO.setup(ledPin, GPIO.OUT)
    GPIO.output(ledPin, GPIO.LOW)
    print ("using pin %d" %ledPin)
   
def loop():
    while True:
        GPIO.output(ledPin, GPIO.HIGH)
        print ("LED turned on >>>")
        time.sleep(1)
        GPIO.output(ledPin, GPIO.LOW)
        print ("LED turned off <<<")
        time.sleep(1)
   
def destroy():
    GPIO.cleanup()
   
if __name__ == "__main__":
    print("Program is staring...\n")
    setup()
    
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
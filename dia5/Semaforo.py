import RPi.GPIO as GPIO
import time

redauto=17
yellowauto=27
greenauto=22

redpeat=19
yellowpeat=13
greenpeat=6

GPIO.setmode(GPIO.BCM)
GPIO.setup(redauto, GPIO.OUT)
GPIO.setup(yellowauto, GPIO.OUT)
GPIO.setup(greenauto, GPIO.OUT)

GPIO.setup(redpeat, GPIO.OUT)
GPIO.setup(yellowpeat, GPIO.OUT)
GPIO.setup(greenpeat, GPIO.OUT)

try:
    while True:

        GPIO.output(redauto, True)
        time.sleep(2)

        GPIO.output(greenpeat, True)
        time.sleep(5)

        GPIO.output(yellowpeat, True)              
        time.sleep(2)

        GPIO.output(greenpeat, False) 
        time.sleep(2)

        GPIO.output(redpeat, True) 
        time.sleep(2)
        
        GPIO.output(yellowpeat, False) 
        time.sleep(2)

        GPIO.output(yellowauto, True) 
        time.sleep(2)

        GPIO.output(redauto, False) 
        time.sleep(2)

        GPIO.output(greenauto, True) 
        time.sleep(2)

        GPIO.output(yellowauto, False) 
        time.sleep(5)
        GPIO.output(yellowauto, True)
        time.sleep(2)
        GPIO.output(greenauto, False)
        time.sleep(2)

        GPIO.output(redauto,True)
        GPIO.output(yellowauto, False)
        time.sleep(2)


except KeyboardInterrupt:
    print("Saliendo")
finally:
    GPIO.cleanup() 

import RPi.GPIO as GPIO
bt = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(bt, GPIO.IN)
try:
    while True:
        print(GPIO.input(bt))
except KeyboardInterrupt:
    print("Chau")
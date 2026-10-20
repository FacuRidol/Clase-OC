import time
import board
import neopixel
import random
import RPi.GPIO as GPIO


pixel_pin = board.D18
num_pixels = 16 
ORDER = neopixel.GRB 

bt = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(bt, GPIO.IN)

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
)
def ganar(num):
    pixels.fill=(0,0,0)
    pixels.fill=(255,0,0)
    pixels.show()
    pixels.fill=(0,0,0)
    pixels.show()
    global a
    a=num

def perder(num1):
    pixels.fill=(0,0,0)
    pixels.fill=(0,255,0)
    pixels.show()
    pixels.fill=(0,0,0)
    pixels.show()
    global a
    a=num1
vel=1
try:
    while True:
        pixels.show()
        ob=random.randint(0,num_pixels)
        a=0
        while a==0:
            for j in range(num_pixels):
                pixels[j]=(225,0,0)
                pixels[ob]=(0, 255, 0)
                pixels.show()  
                time.sleep(vel)
                pixels[j]=(0,0,0)

                if GPIO.input(bt)==False:
                    time.sleep(0.05)
                    if GPIO.input(bt)==False:
                        if j==ob:
                            vel= vel -0.25
                            ganar(1)
                         
                        elif j != ob:
                            vel=1
                            perder(1)

except KeyboardInterrupt:
    pixels.fill(0, 0, 0)
    pixels.show()

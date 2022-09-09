import RPi.GPIO as GPIO
import time, datetime

Moisture_pin = 40
relay = 38

GPIO.setmode(GPIO.BOARD)
GPIO.setup(Moisture_pin, GPIO.IN)
GPIO.setup(relay, GPIO.OUT)

def sense(Moisture_pin):
        timedate = datetime.datetime.now().strftime("%H:%M %Y-%m-%d ")
        if GPIO.input(Moisture_pin):
                print ("Dry - turn water on", timedate)
                GPIO.output(relay, GPIO.LOW)
                print ("relay on")
        else:
                print ("Wet - turn water off", timedate)
                GPIO.output(relay, GPIO.HIGH)
                print ("relay off")
        return()

while True:
        sense(Moisture_pin)
        time.sleep(1)
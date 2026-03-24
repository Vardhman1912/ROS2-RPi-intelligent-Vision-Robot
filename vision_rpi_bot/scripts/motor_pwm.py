import RPi.GPIO as GPIO
import time

# Based on your setup(27,22,24,23,17,21)
# Let's assume 27 & 22 are Direction, and 17 is the Enable (PWM) pin
ENA = 21 
IN1 = 23
IN2 = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(ENA, GPIO.OUT)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)

# 1. Turn Enable HIGH (This acts like the jumper you removed)
GPIO.output(ENA, GPIO.HIGH)

print("Testing Motor Forward...")
GPIO.output(IN1, GPIO.HIGH)
GPIO.output(IN2, GPIO.LOW)
time.sleep(2)

print("Stopping...")
GPIO.output(IN1, GPIO.LOW)
GPIO.output(IN2, GPIO.LOW)
GPIO.output(ENA, GPIO.LOW) # Turn off the bridge entirely

GPIO.cleanup()
# ラズパイでLEDを点滅させる

import RPi.GPIO as GPIO
import time

Led_pin = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(Led_pin, GPIO.OUT)

for i in range(0, 5, 1):
  GPIO.output(Led_pin, GPIO.HIGH)
  time.sleep(0.5)
  GPIO.output(Led_pin, GPIO,LOW)
  time.sleep(0.5)
  
GPIO.cleanup()

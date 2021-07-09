from time import sleep
from gpiozero import MotionSensor

def detectIntruders():
  pir.wait_for_ motion()
  print('Alert!')
  sleep(5)
  
pir = MoionSensor(18)

while True:
  DetectIntruders()

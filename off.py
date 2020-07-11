from gpiozero import LEDBoard, LED

from time import sleep
from signal import pause

leds = LEDBoard(6, 13, pwm=True)

leds.off()

pause()
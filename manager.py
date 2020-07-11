from gpiozero import LEDBoard, LED
import RPi.GPIO as GPIO
from signal import pause
from time import sleep


class Manager:

    chan_list = []
    lightPin = 23
    btnPin = 6

    def __init__(self):
        print("init class")
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.lightPin, GPIO.OUT)
        #GPIO.setup(13, GPIO.OUT)
        GPIO.setup(self.btnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(self.btnPin, GPIO.RISING,
                              callback=self.button_pressed, bouncetime=200)

        #self.chan_list = (6, 13)

    def on(self):
        # GPIO.output(self.chan_list, GPIO.HIGH)  # all LOW
        GPIO.output(self.lightPin, GPIO.HIGH)

    def off(self):
        # GPIO.output(self.chan_list, GPIO.LOW)  # all LOW
        GPIO.output(self.lightPin, GPIO.LOW)

    def button_pressed(self, channel):
        # print(GPIO.RISING)
        # print(GPIO.FALLING)
        if(GPIO.input(self.lightPin)):
            GPIO.output(self.lightPin, GPIO.LOW)
        else:
            GPIO.output(self.lightPin, GPIO.HIGH)

    def blink(self):
        p = GPIO.PWM(self.lightPin, 50)  # channel=12 frequency=50Hz
        p.start(0)
        try:
            for x in range(3):
                for dc in range(0, 101, 5):
                    p.ChangeDutyCycle(dc)
                    sleep(0.1)
                for dc in range(100, -1, -5):
                    p.ChangeDutyCycle(dc)
                    sleep(0.1)
        except KeyboardInterrupt:
            pass
        p.stop()
        # GPIO.cleanup()


# @app.route('/off')
# def off():
#     leds = LEDBoard(6, 13, pwm=True)

#     leds.off()
#     return 'On'

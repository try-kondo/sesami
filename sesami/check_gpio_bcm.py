import RPi.GPIO as GPIO


def gpio_input_bcm(i_bcm):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(i_bcm,GPIO.IN)
    result = GPIO.input(i_bcm)

    return result

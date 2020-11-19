import time
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

GPIO.setwarnings(False)

button1 = 0
button2 = 5
button3 = 6
button4 = 13
button5 = 19
button6 = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(button1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button6, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

'''
GPIO.add_event_detect(0,GPIO.RISING,callback=button1, bouncetime=500)
GPIO.add_event_detect(5,GPIO.RISING,callback=button2, bouncetime=500)
GPIO.add_event_detect(6,GPIO.RISING,callback=button3, bouncetime=500)
GPIO.add_event_detect(13,GPIO.RISING,callback=button4, bouncetime=500)
GPIO.add_event_detect(19,GPIO.RISING,callback=button5, bouncetime=500)
GPIO.add_event_detect(26,GPIO.RISING,callback=button6, bouncetime=500)
'''
while True:
    buttonState1 = GPIO.input(button1)
    buttonState2 = GPIO.input(button2)
    buttonState3 = GPIO.input(button3)
    buttonState4 = GPIO.input(button4)
    buttonState5 = GPIO.input(button5)
    buttonState6 = GPIO.input(button6)

    if (not buttonState1):

        print("1\n")
        time.sleep(0.5)

    elif (buttonState2):

        print("2\n")
        time.sleep(0.5)

    elif (buttonState3):

        print("3\n")
        time.sleep(0.5)

    elif (buttonState4):

        print("4\n")
        time.sleep(0.5)

    elif (buttonState5):
        print("5\n")
        time.sleep(0.5)

    elif (buttonState6):
        print("6\n")
        time.sleep(0.5)

    else:
        continue

input()

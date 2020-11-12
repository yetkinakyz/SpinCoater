import time
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

def button_callback(channel):
    print("Button was pushed!")

    time.sleep(0.1)

GPIO.setwarnings(False) # Ignore warning for now

GPIO.setmode(GPIO.BCM) # Use physical pin numbering
GPIO.setup(0, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.add_event_detect(0,GPIO.RISING,callback=button_callback)
GPIO.add_event_detect(5,GPIO.RISING,callback=button_callback)
GPIO.add_event_detect(6,GPIO.RISING,callback=button_callback)
GPIO.add_event_detect(13,GPIO.RISING,callback=button_callback)
GPIO.add_event_detect(19,GPIO.RISING,callback=button_callback)
GPIO.add_event_detect(26,GPIO.RISING,callback=button_callback)

message = input("Press enter to quit\n\n") # Run until someone presses enter
GPIO.cleanup() # Clean up
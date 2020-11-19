'''
SPIN COATER PROJECT MAIN SOFTWARE
                        by Yetkin AKYUZ

    Website: https://yetkinakyuz.com
    Email:   contact@yetkinakyuz.com
'''

##### LIBRARIES #####
import RPi.GPIO as GPIO #RASPBERRY PI GPIO LIBRARY WIKI: https://sourceforge.net/p/raspberry-gpio-python/wiki/Home/
import lcddriver #LCD I2C LIBRARY
import RpmControl as Spinner

import time

##### SETUP ##### 

## DISPLAY
display = lcddriver.lcd()

## GPIO
GPIO.setwarnings(False) #DISABLE WARNINGS
GPIO.setmode(GPIO.BCM) #GPIO PIN NUMBERS (GPIO.BOARD for physical pin numbers.)

## BUTTONS
button1 = 0
button2 = 5
button3 = 6
button4 = 13
button5 = 19
button6 = 26

GPIO.setup(button1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button6, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

buttons = [ not GPIO.input(button1), 
            GPIO.input(button2), 
            GPIO.input(button3), 
            GPIO.input(button4), 
            GPIO.input(button5), 
            GPIO.input(button6)]

## MAIN MENU
mainMenu = ["SET PROGRAM     ",
            "TEST            ",
            "INFO            "]

menuAscii = [   "             " + " " + chr(124) + chr(62),
                "             " + chr(60) + chr(124) + chr(62),
                "             " + chr(60) + chr(124) + " "]

menuPosition = 0 

display.lcd_clear()
display.lcd_display_string("SPIN COATER     ", 1) #PRINT LINE 1
display.lcd_display_string("        PROJECT ", 2) #PRINT LINE 2

time.sleep(2)

display.lcd_display_string("BY YETKIN AKYUZ ", 1) #PRINT LINE 1
display.lcd_display_string("yetkinakyuz.com ", 2) #PRINT LINE 2

time.sleep(2)
display.lcd_clear()

display.lcd_display_string("    STARTING    ", 1) #PRINT LINE 1

for i in range(17):
    loading = '*'*i
    display.lcd_display_string(loading, 2) #PRINT LINE 2
    time.sleep(0.125)

time.sleep(1)

display.lcd_display_string("    WELCOME!    ", 1) #PRINT LINE 1

time.sleep(2)
display.lcd_clear()

while True:

    display.lcd_display_string(mainMenu[menuPosition], 1) #PRINT LINE 1
    display.lcd_display_string(menuAscii[menuPosition], 2) #PRINT LINE 2
    
    if not GPIO.input(button1) and menuPosition > 0:
        menuPosition = menuPosition - 1

        print("Up Button - " + str(menuPosition))
        time.sleep(0.05)

    elif GPIO.input(button2) and menuPosition < len(mainMenu) - 1:
        menuPosition = menuPosition + 1

        print("Down Button - " + str(menuPosition))
        time.sleep(0.05)

    elif GPIO.input(button4):
        if menuPosition == 0:
            display.lcd_clear()
            display.lcd_display_string("Set instructions", 1) #PRINT LINE 1
            display.lcd_display_string("and run         ", 2) #PRINT LINE 2
            time.sleep(2)
        
        elif menuPosition == 1:
            display.lcd_clear()
            display.lcd_display_string("Run a 2-stg test", 1) #PRINT LINE 1
            display.lcd_display_string("Stg 1: 1000/15  ", 2) #PRINT LINE 2
            time.sleep(2)
            display.lcd_display_string("Stg 2: 5000/30  ", 2) #PRINT LINE 2
            time.sleep(2)

        elif menuPosition == 2:
            display.lcd_clear()
            display.lcd_display_string("Get information ", 1) #PRINT LINE 1
            display.lcd_display_string("about project   ", 2) #PRINT LINE 2
            time.sleep(2)

        else:
            None

    elif GPIO.input(button6):
        if menuPosition == 1:
            while True:
                
                display.lcd_clear()
                display.lcd_display_string(" TEST  SOFTWARE ", 1) #PRINT LINE 1
                display.lcd_display_string("TOTAL:  2 STAGES", 2) #PRINT LINE 2
                time.sleep(2)
                
                display.lcd_clear()
                display.lcd_display_string("  FIRST  STAGE  ", 1) #PRINT LINE 1
                display.lcd_display_string("1000 RPM  15 SEC", 2) #PRINT LINE 2
                time.sleep(2)

                Spinner.setExpectedRPM(1000)
                Spinner.setExpectedTime(15)
                Spinner.FirstStage()

                display.lcd_clear()
                display.lcd_display_string("   NEXT STAGE   ", 1) #PRINT LINE 1
                display.lcd_display_string("5000 RPM 30 SEC", 2) #PRINT LINE 2
                time.sleep(2)

                Spinner.setExpectedRPM(5000)
                Spinner.setExpectedTime(30)
                Spinner.NextStage()

                display.lcd_clear()
                display.lcd_display_string("      DONE      ", 1) #PRINT LINE 1
                time.sleep(2)

                break
                
        elif menuPosition == 2:

                display.lcd_clear()

                display.lcd_display_string("Name: SpinCoater", 1) #PRINT LINE 1
                display.lcd_display_string("Engr. Desg. Prj.", 2) #PRINT LINE 1
                time.sleep(3)

                display.lcd_display_string("By Yetkin AKYUZ ", 1) #PRINT LINE 1
                display.lcd_display_string("yetkinakyuz.com ", 2) #PRINT LINE 1
                time.sleep(3)

                display.lcd_display_string("Version: 1.0    ", 1) #PRINT LINE 1
                display.lcd_display_string("Date: 18.11.2020", 2) #PRINT LINE 1
                time.sleep(3)

        else:
            continue
    else:
        continue

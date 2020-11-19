##### LIBRARIES #####
import RPi.GPIO as GPIO #RASPBERRY PI GPIO LIBRARY WIKI: https://sourceforge.net/p/raspberry-gpio-python/wiki/Home/
import lcddriver #LCD I2C LIBRARY
import rpm_control as Spinner

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
mainMenu = ["    SET PROG ",
            "        TEST ",
            "        INFO "]

menuAscii = [   " " + chr(124) + chr(62),
                chr(60) + chr(124) + chr(62),
                chr(60) + chr(124) + " "]

menuPosition = 0 

while True:

    display.lcd_display_string("MENU            ", 1) #PRINT LINE 1
    display.lcd_display_string(mainMenu[menuPosition] + menuAscii[menuPosition], 2) #PRINT LINE 2
    
    if not GPIO.input(button1) and menuPosition > 0:
        menuPosition = menuPosition - 1

        print("Up Button - " + str(menuPosition))
        time.sleep(0.005)

    elif GPIO.input(button2) and menuPosition < len(mainMenu) - 1:
        menuPosition = menuPosition + 1

        print("Down Button - " + str(menuPosition))
        time.sleep(0.005)

    elif GPIO.input(button6):
        if menuPosition == 1:
            while GPIO.input(button6):
                
                display.lcd_clear()
                display.lcd_display_string(" TEST  SOFTWARE ", 1) #PRINT LINE 1
                display.lcd_display_string("TOTAL:  2 STAGES", 2) #PRINT LINE 2
                time.sleep(2)
                
                display.lcd_clear()
                display.lcd_display_string("  FIRST  STAGE  ", 1) #PRINT LINE 1
                display.lcd_display_string("1000 RPM  15 SEC", 2) #PRINT LINE 2
                time.sleep(2)

                Spinner.setExpectedRPM(1000)
                Spinner.setExpectedTime(30)
                Spinner.FirstStage()

                display.lcd_clear()
                display.lcd_display_string("   NEXT STAGE   ", 1) #PRINT LINE 1
                display.lcd_display_string("5000 RPM 30 SEC", 2) #PRINT LINE 2
                time.sleep(2)

                Spinner.setExpectedRPM(5000)
                Spinner.setExpectedTime(120)
                Spinner.NextStage()

                display.lcd_clear()
                display.lcd_display_string("      DONE      ", 1) #PRINT LINE 1
                time.sleep(2)

                break

        else:
            continue
    else:
        continue
            


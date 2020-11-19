##### LIBRARIES #####
import RPi.GPIO as GPIO #RASPBERRY PI GPIO LIBRARY WIKI: https://sourceforge.net/p/raspberry-gpio-python/wiki/Home/
import lcddriver #LCD I2C LIBRARY
import rpm_control as RPM

import time

##### SETUP ##### 

## DISPLAY
display = lcddriver.lcd()

spinner = RPM.program()

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

buttons = [ None,
            not GPIO.input(button1), 
            GPIO.input(button2), 
            GPIO.input(button3), 
            GPIO.input(button4), 
            GPIO.input(button5), 
            GPIO.input(button6)]

## MENU
menuPosition = 0
mainMenu = [" SET PROGRAM ", "       TEST ", "        INFO "]
menuAscii = [chr(124) + " " + chr(175), chr(124) + " " + chr(174)+chr(175), chr(124) + " " + chr(174)] 

while True:

    #display.lcd_display_string("SPIN COATER", 1) #PRINT LINE 1
    #display.lcd_display_string(" BY YETKIN AKYUZ", 2) #PRINT LINE 2
    #time.sleep(2)

    #display.lcd_clear()

    #display.lcd_display_string("     WELCOME!    ", 1) #PRINT LINE 1
    #time.sleep(2)

    display.lcd_clear()
    
    while True:

        display.lcd_display_string("MENU            ", 1) #PRINT LINE 1
        display.lcd_display_string(mainMenu[menuPosition] + menuAscii[menuPosition], 2) #PRINT LINE 2
        
        if not GPIO.input(button1) and menuPosition > 0:
            menuPosition = menuPosition - 1

            print("Up Button - " + str(menuPosition))
            time.sleep(0.1)

        elif GPIO.input(button2) and menuPosition < len(mainMenu) - 1:
            menuPosition = menuPosition + 1

            print("Down Button - " + str(menuPosition))
            time.sleep(0.1)

        else:
            continue

'''
SPIN COATER PROJECT MAIN SOFTWARE
                        by Yetkin AKYUZ

    Website: https://yetkinakyuz.com
    Email:   contact@yetkinakyuz.com
'''

##### LIBRARIES #####
from sys import version_info
import RPi.GPIO as GPIO #RASPBERRY PI GPIO LIBRARY WIKI: https://sourceforge.net/p/raspberry-gpio-python/wiki/Home/
import lcddriver #LCD I2C LIBRARY
import RpmControl as Spinner

import os
import time

##### SETUP #####

version_info = "1.0.5"
date_info = "09.12.2020"

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

versionText = "Version:   " + version_info
dateText = "Date: " + date_info

## MAIN MENU
mainMenu = ["SET PROGRAM     ",
            "TEST            ",
            "INFO            ",
            "VERSION UPDATE  "]
mainMenuAscii = [   "             " + " " + chr(124) + chr(62),
                "             " + chr(60) + chr(124) + chr(62),
                "             " + chr(60) + chr(124) + chr(62),
                "             " + chr(60) + chr(124) + " "]

## INFO MENU
infoMenuLine1 = ["Set instructions",
                 "Run a 2-stg test", 
                 "Get information ",
                 versionText        ]
infoMenuLine2 = ["and run         ",
                 "                ",
                 "about project   ",
                 dateText           ]

## SET MENU
setMenu = ["RUN QUICK PROG. ", "SET MANUAL PROG."]
setMenuAscii = ["             " + " " + chr(124) + chr(62),
                "             " + chr(60) + chr(124) + " "]

## QUICK MENU
quickSpeeds1 = ["STAGE 1", 500, 1000, 1500, 2000, 3000]
quickSpeeds2 = ["STAGE 2", 3500, 4000, 5000, 6000, 7000]

quickSeconds1 = ["STAGE 1", 45, 45, 45, 45, 45]
quickSeconds2 = ["STAGE 2", 15, 15, 15, 15, 15]

## MANUAL MENU
manualStages = 1
manualSecond = 5
manualSpeed = 500
manualSeconds = ["5"]
manualSpeeds = ["500"]

## POSITIONS
menuPosition = 0
setPosition = 0
manualPosition = 0

display.lcd_clear()
display.lcd_display_string("SPIN COATER     ", 1) #PRINT LINE 1
display.lcd_display_string("        PROJECT ", 2) #PRINT LINE 2

time.sleep(1)

display.lcd_display_string("BY YETKIN AKYUZ ", 1) #PRINT LINE 1
display.lcd_display_string("yetkinakyuz.com ", 2) #PRINT LINE 2

time.sleep(1)

display.lcd_clear()
display.lcd_display_string("    WELCOME!    ", 1) #PRINT LINE 1

time.sleep(1)

display.lcd_clear()

while True:

    display.lcd_display_string(mainMenu[menuPosition], 1) #PRINT LINE 1
    display.lcd_display_string(mainMenuAscii[menuPosition], 2) #PRINT LINE 2

    if not GPIO.input(button1) and menuPosition > 0:
        menuPosition = menuPosition - 1

        print("Up Button - " + str(menuPosition))
        time.sleep(0.1)

    elif GPIO.input(button2) and menuPosition < len(mainMenu) - 1:
        menuPosition = menuPosition + 1

        print("Down Button - " + str(menuPosition))
        time.sleep(0.1)

    elif GPIO.input(button4):
        display.lcd_display_string(infoMenuLine1[menuPosition], 1) #PRINT LINE 1
        display.lcd_display_string(infoMenuLine2[menuPosition], 2) #PRINT LINE 2
        time.sleep(2)

    elif GPIO.input(button6):
        if menuPosition == 0:
            while True:
                 
                display.lcd_display_string(setMenu[setPosition], 1) #PRINT LINE 1
                display.lcd_display_string(setMenuAscii[setPosition], 2) #PRINT LINE 2

                if not GPIO.input(button1) and setPosition > 0:
                    setPosition = setPosition - 1

                    print("Up Button - " + str(setPosition))
                    time.sleep(0.2)

                elif GPIO.input(button2) and setPosition < len(setMenu) - 1:
                    setPosition = setPosition + 1

                    print("Down Button - " + str(setPosition))
                    time.sleep(0.2)

                elif GPIO.input(button6):
                    time.sleep(0.5)

                    display.lcd_clear()
                    if setPosition == 0:
                        while True:
                            display.lcd_display_string("0000 - 0000 RPM", 1) #PRINT LINE 1
                            display.lcd_display_string("0000 - 0000 SEC", 2) #PRINT LINE 1

                    elif setPosition == 1:                       
                        while True:
                            display.lcd_display_string("NUMBER OF STAGES", 1) #PRINT LINE 1
                            display.lcd_display_string("STAGES: " + str(manualStages), 2) #PRINT LINE 2
                            
                            if not GPIO.input(button1) and manualStages < 10:
                                manualStages += 1
                                display.lcd_display_string("STAGES:         ", 2) #CLEAR LINE 2

                                print("Up Button - " + str(manualStages))
                                time.sleep(0.2)
                            
                            elif not GPIO.input(button1) and manualStages == 10:
                                manualStages = 1
                                print("Up Button - " + str(manualStages))
                                time.sleep(0.2)

                            elif GPIO.input(button2) and manualStages > 1:
                                manualStages -= 1
                                display.lcd_display_string("STAGES:         ", 2) #CLEAR LINE 2

                                print("Down Button - " + str(manualStages))
                                time.sleep(0.2)

                            elif GPIO.input(button2) and manualStages == 1:
                                manualStages = 10
                                display.lcd_display_string("STAGES:         ", 2) #CLEAR LINE 2

                                print("Down Button - " + str(manualStages))
                                time.sleep(0.2)

                            elif GPIO.input(button3):
                                manualStages = 1

                            elif GPIO.input(button5):
                                manualStages = 1
                                break
                            elif GPIO.input(button6):
                                manualStages += 1
                                
                                display.lcd_clear()
                                display.lcd_display_string("   STAGES SET   ", 1) #PRINT LINE 1
                                time.sleep(1)
                                break
                            else:
                                continue

                        for stage in range(1, manualStages):
                            manualSeconds.append(manualSecond)
                            manualSpeeds.append(manualSpeed)
                        
                        display.lcd_clear()

                        while True:
                            for stage in range(1,manualStages):
                                if GPIO.input(button5):
                                    manualStages = 1
                                    manualSeconds = [5]
                                    manualSpeeds = [500]
                                    break

                                else:
                                    while True:
                                        display.lcd_display_string("STAGE " + str(stage), 1) #PRINT LINE 1
                                        display.lcd_display_string("TIME: " + str(manualSeconds[stage]), 2) #PRINT LINE 2
                                        
                                        if not GPIO.input(button1) and manualSeconds[stage] < 3600:
                                            display.lcd_display_string("TIME:          ", 2) #CLEAR LINE 2

                                            if manualSeconds[stage] < 3600:
                                                manualSeconds[stage] += 5

                                            elif manualSeconds[stage] == 3600:
                                                manualSeconds[stage] = 5

                                        elif GPIO.input(button2):
                                            display.lcd_display_string("TIME:          ", 2) #CLEAR LINE 2

                                            if manualSeconds[stage] > 5:
                                                manualSeconds[stage] -= 5
                                            
                                            elif manualSeconds[stage] == 5:
                                                manualSeconds[stage] = 3600

                                        elif GPIO.input(button3):
                                            manualSeconds[stage] = 5

                                        elif GPIO.input(button5):
                                            manualSeconds[stage] = 5
                                            break

                                        elif GPIO.input(button6):                                        
                                            display.lcd_clear()
                                            display.lcd_display_string("    TIME SET    ", 1) #PRINT LINE 1
                                            time.sleep(1)
                                            display.lcd_clear()
                                            break
                                        else:
                                            continue

                                    while True:
                                        display.lcd_display_string("STAGE " + str(stage), 1) #PRINT LINE 1
                                        display.lcd_display_string("SPEED:" + str(manualSpeeds[stage]), 2) #PRINT LINE 2
                                        
                                        if not GPIO.input(button1) and manualSpeeds[stage] < 7200:
                                            manualSpeeds[stage] += 50
                                            display.lcd_display_string("SPEED:         ", 2) #CLEAR LINE 2

                                            print("Up Button - " + str(manualSpeeds[stage]))
                                            time.sleep(0.2)

                                        elif GPIO.input(button2) and manualSpeeds[stage] > 500:
                                            manualSpeeds[stage] -= 50
                                            display.lcd_display_string("SPEED:         ", 2) #CLEAR LINE 2

                                            print("Down Button - " + str(manualSpeeds[stage]))
                                            time.sleep(0.2)

                                        elif GPIO.input(button3):
                                            manualSpeeds[stage] = 500

                                        elif GPIO.input(button5):
                                            manualSpeeds[stage] = 500
                                            break

                                        elif GPIO.input(button6):                                        
                                            display.lcd_clear()
                                            display.lcd_display_string("   SPEED  SET   ", 1) #PRINT LINE 1
                                            time.sleep(1)
                                            display.lcd_clear()
                                            break
                                        else:
                                            continue
                            
                            display.lcd_clear()
                            display.lcd_display_string("    STARTING    ", 1) #PRINT LINE 1
                            time.sleep(2)

                            for stage in range (1,manualStages):
                                Spinner.setExpectedRPM(manualSpeeds[stage])
                                Spinner.setExpectedTime(manualSeconds[stage])
                                
                                if stage == 1:
                                    Spinner.FirstStage()
                                else:
                                    Spinner.NextStage()
                                
                                Spinner.clear()
                            
                            display.lcd_clear()
                            display.lcd_display_string("      DONE      ", 1) #PRINT LINE 1

                            time.sleep(3)

                            manualStages = 1
                            manualSeconds = [5]
                            manualSpeeds = [500]

                            break
                    
                    else:
                        continue
                elif GPIO.input(button5):
                    break
                
                else:
                    continue

        elif menuPosition == 1:
            while True:

                display.lcd_clear()
                display.lcd_display_string(" TEST  SOFTWARE ", 1) #PRINT LINE 1
                display.lcd_display_string("TOTAL:  2 STAGES", 2) #PRINT LINE 2
                time.sleep(2)

                display.lcd_clear()
                display.lcd_display_string("  FIRST  STAGE  ", 1) #PRINT LINE 1
                display.lcd_display_string("500 RPM  30 SEC", 2) #PRINT LINE 2
                time.sleep(2)

                display.lcd_clear()
                display.lcd_display_string("   NEXT STAGE   ", 1) #PRINT LINE 1
                display.lcd_display_string("7200 RPM 15 SEC", 2) #PRINT LINE 2
                time.sleep(2)

                Spinner.setExpectedRPM(2500)
                Spinner.setExpectedTime(15)
                Spinner.FirstStage()

                Spinner.clear()

                Spinner.setExpectedRPM(7200)
                Spinner.setExpectedTime(15)
                Spinner.NextStage()

                #Spinner.done()
                Spinner.clear()

                display.lcd_display_string("      DONE      ", 1) #PRINT LINE 1

                time.sleep(3)
                break

        elif menuPosition == 2:

                display.lcd_clear()

                display.lcd_display_string("Name: SpinCoater", 1) #PRINT LINE 1
                display.lcd_display_string("Engr. Desg. Prj.", 2) #PRINT LINE 1
                time.sleep(3)

                display.lcd_display_string("By Yetkin AKYUZ ", 1) #PRINT LINE 1
                display.lcd_display_string("yetkinakyuz.com ", 2) #PRINT LINE 1
                time.sleep(3)

                display.lcd_display_string("Version:   " + version_info, 1) #PRINT LINE 1
                display.lcd_display_string("Date: " + date_info, 2) #PRINT LINE 1
                time.sleep(3)

        elif menuPosition == 3:
            display.lcd_clear()
            display.lcd_display_string("    UPDATING    ", 1) #PRINT LINE 2
            display.lcd_display_string("  FROM  GITHUB  ", 2) #PRINT LINE 2

            os.system("git -C $(find ~ -iname SpinCoater)/Software pull")
            time.sleep(1)

            display.lcd_clear()
            display.lcd_display_string("      DONE      ", 1) #PRINT LINE 2

            time.sleep(0.5)

            display.lcd_clear()
            display.lcd_display_string("   RESTARTING   ", 1) #PRINT LINE 2

            os.system("sh $(find ~ -iname SpinCoaterRestart.sh)")

            exit()

        else:
            continue
    else:
        continue
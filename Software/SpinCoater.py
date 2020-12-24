'''
    SPIN COATER PROJECT
                    by Yetkin AKYUZ

    Website: https://yetkinakyuz.com
    Email:   contact@yetkinakyuz.com
'''

##### LIBRARIES #####

import RPi.GPIO as GPIO #RASPBERRY PI GPIO LIBRARY WIKI: https://sourceforge.net/p/raspberry-gpio-python/wiki/Home/
import lcddriver #LCD I2C LIBRARY
import RpmControl as Spinner

import os
import time

##### SETUP #####

versionInfo = "1.0.9"
dateInfo = "24.12.2020"

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

versionText = "Version:   " + versionInfo
dateText = "Date: " + dateInfo

## MAIN MENU
mainMenu = ["RUN PROGRAM       ",
            "INFO            ",
            "VERSION UPDATE  ",
            "REBOOT DEVICE   "]        

mainMenuAscii = ["             " + " " + chr(124) + chr(62),
                "             " + chr(60) + chr(124) + chr(62),
                "             " + chr(60) + chr(124) + chr(62),
                "             " + chr(60) + chr(124) + " "]

## INFO MENU
infoMenuLine1 = ["RUN OR SET PROG.",
                 "GET INFORMATION ",
                 versionText       ,
                 "REBOOT OPERATING"]

infoMenuLine2 = ["QUICK OR MANUAL ",
                 "ABOUT PROJECT   ",
                 dateText          ,
                 "SYSTEM          "]

## SET MENU
setMenu = ["QUICK PROGRAMS  ",
            "SET MANUAL PROG."]

setMenuAscii = ["             " + " " + chr(124) + chr(62),
                "             " + chr(60) + chr(124) + " "]

## QUICK MENU
program = 1

quickSpeeds1 = ["STAGE 1", 500, 1000, 2000, 3000, 4000]
quickSpeeds2 = ["STAGE 2", 3500, 4500, 5500, 6500, 7200]

quickSeconds1 = ["STAGE 1", 30, 30, 30, 30, 30]
quickSeconds2 = ["STAGE 2", 180, 180, 180, 180, 180]

## MANUAL MENU
manualStages = 1
manualSecond = 5
manualSpeed = 500

manualSeconds = ["-"]
manualSpeeds = ["-"]

## POSITIONS
menuPosition = 0
setPosition = 0
manualPosition = 0

######
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

        time.sleep(0.2)

    elif GPIO.input(button2) and menuPosition < len(mainMenu) - 1:
        menuPosition = menuPosition + 1

        time.sleep(0.2)

    elif GPIO.input(button4):
        display.lcd_display_string(infoMenuLine1[menuPosition], 1) #PRINT LINE 1
        display.lcd_display_string(infoMenuLine2[menuPosition], 2) #PRINT LINE 2
        time.sleep(2)

    elif GPIO.input(button6):
        display.lcd_clear()
        time.sleep(0.2)

        if menuPosition == 0:
            while True:
                 
                display.lcd_display_string(setMenu[setPosition], 1) #PRINT LINE 1
                display.lcd_display_string(setMenuAscii[setPosition], 2) #PRINT LINE 2

                if not GPIO.input(button1) and setPosition > 0:
                    setPosition = setPosition - 1

                    time.sleep(0.2)

                elif GPIO.input(button2) and setPosition < len(setMenu) - 1:
                    setPosition = setPosition + 1

                    time.sleep(0.2)

                elif GPIO.input(button6):
                    time.sleep(0.2)

                    display.lcd_clear()
                    time.sleep(0.2)

                    if setPosition == 0:
                        display.lcd_display_string("P            RPM", 1) #PRINT LINE 1
                        display.lcd_display_string("             SEC", 2) #PRINT LINE 2

                        while True:
                            display.lcd_display_string("P" + str(program) + " " + str(quickSpeeds1[program]) + "-" + str(quickSpeeds2[program]), 1) #PRINT LINE 1
                            display.lcd_display_string("   " + str(quickSeconds1[program]) + "-" + str(quickSeconds2[program]), 2) #PRINT LINE 2

                            if GPIO.input(button2):
                                display.lcd_display_string("P            RPM", 1) #PRINT LINE 1
                                display.lcd_display_string("             SEC", 2) #PRINT LINE 2

                                if program < len(quickSeconds1) - 1:
                                    program += 1
                                    
                                    time.sleep(0.2)
                                
                                elif program == len(quickSeconds1) - 1:
                                    program = 1

                                    time.sleep(0.2)
                                
                                else:
                                    continue

                            elif not GPIO.input(button1):
                                display.lcd_display_string("P            RPM", 1) #PRINT LINE 1
                                display.lcd_display_string("             SEC", 2) #PRINT LINE 2

                                if program > 1:
                                    program -= 1

                                    time.sleep(0.2)

                                elif program == 1:
                                    program = len(quickSeconds1) - 1

                                    time.sleep(0.2)

                                else:
                                    continue

                            elif GPIO.input(button6):
                                display.lcd_clear()
                                display.lcd_display_string("   PROGRAM: " + str(program) + "   ", 1) #PRINT LINE 1
                                display.lcd_display_string("    STARTING    ", 2) #PRINT LINE 2
                                time.sleep(2)

                                Spinner.setExpectedTime(quickSeconds1[program])
                                Spinner.setExpectedRPM(quickSpeeds1[program])
                                Spinner.FirstStage()

                                Spinner.clear()

                                Spinner.setExpectedTime(quickSeconds2[program])
                                Spinner.setExpectedRPM(quickSpeeds2[program])
                                Spinner.NextStage()                                

                                Spinner.clear()

                                display.lcd_clear()
                                display.lcd_display_string("      DONE      ", 1) #PRINT LINE 1

                                time.sleep(3)

                                break

                            elif GPIO.input(button5):
                                program = 1
                                
                                time.sleep(0.2)
                                break

                            else:
                                continue

                    elif setPosition == 1:   
                        manualStop = False        

                        while True:
                            display.lcd_display_string("NUMBER OF STAGES", 1) #PRINT LINE 1
                            display.lcd_display_string("STAGES: " + str(manualStages), 2) #PRINT LINE 2
                            
                            if not GPIO.input(button1):
                                display.lcd_display_string("STAGES:         ", 2) #CLEAR LINE 2

                                if GPIO.input(button4):
                                
                                    if manualStages < 100:
                                        manualStages += 10
                                        time.sleep(0.2)
                                
                                    elif manualStages == 100:
                                        manualStages = 1
                                        time.sleep(0.2)
                                
                                    else:
                                        continue

                                elif not GPIO.input(button4):
                                    if manualStages < 100:
                                        manualStages += 1
                                        time.sleep(0.2)
                                    
                                    elif manualStages == 100:
                                        manualStages = 1
                                        time.sleep(0.2)
                                    
                                    else:
                                        continue
                            
                                else:
                                    continue
                            
                            elif GPIO.input(button2):
                                display.lcd_display_string("STAGES:         ", 2) #CLEAR LINE 2
                                
                                if GPIO.input(button4):
                                    display.lcd_display_string("STAGES:         ", 2) #CLEAR LINE 2
                                    
                                    if manualStages > 10:
                                        manualStages -= 10
                                        time.sleep(0.2)
                                
                                    elif manualStages == 1:
                                        manualStages = 100
                                        time.sleep(0.2)
                                
                                    else:
                                        continue
                                
                                elif not GPIO.input(button4):
                                    if manualStages > 1:
                                        manualStages -= 1
                                        time.sleep(0.2)
                                    
                                    elif manualStages == 1:
                                        manualStages = 100
                                        time.sleep(0.2)
                                    
                                    else:
                                        continue
                                
                                else:
                                    continue

                            elif GPIO.input(button3):
                                display.lcd_display_string("STAGES:         ", 2) #CLEAR LINE 2

                                manualStages = 1

                            elif GPIO.input(button5):
                                manualStages = 1
                                manualStop = True
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
                                        display.lcd_display_string("TIME: " + str(manualSeconds[stage]) + " SEC", 2) #PRINT LINE 2
                                        
                                        if not GPIO.input(button1):
                                            display.lcd_display_string("TIME:          ", 2) #CLEAR LINE 2

                                            if GPIO.input(button4):

                                                if manualSeconds[stage] < 3540:
                                                    manualSeconds[stage] += 60

                                                    time.sleep(0.2)

                                                elif manualSeconds[stage] <= 5:
                                                    manualSeconds[stage] = 60

                                                    time.sleep(0.2)
                                                
                                                elif manualSeconds[stage] == 3600:
                                                    manualSeconds[stage] = 5

                                                    time.sleep(0.2)

                                                elif manualSeconds[stage] >= 3540:
                                                    manualSeconds[stage] = 3600

                                                    time.sleep(0.2)
                                                
                                                else:
                                                    continue

                                            elif not GPIO.input(button4):
                                                
                                                if manualSeconds[stage] < 3600:
                                                    manualSeconds[stage] += 5

                                                    time.sleep(0.2)

                                                elif manualSeconds[stage] == 3600:
                                                    manualSeconds[stage] = 5

                                                    time.sleep(0.2)

                                                else:
                                                    continue
                                            
                                            else:
                                                continue

                                        elif GPIO.input(button2):
                                            display.lcd_display_string("TIME:          ", 2) #CLEAR LINE 2

                                            if GPIO.input(button4):

                                                if manualSeconds[stage] > 60:
                                                    manualSeconds[stage] -= 60

                                                    time.sleep(0.2)

                                                elif manualSeconds[stage] > 5 and manualSeconds[stage] <= 60:
                                                    manualSeconds[stage] = 5

                                                    time.sleep(0.2)

                                                elif manualSeconds[stage] <= 5:
                                                    manualSeconds[stage] = 3600

                                                    time.sleep(0.2)
                                                
                                                else:
                                                    continue
                                            
                                            if not GPIO.input(button4):
                                                
                                                if manualSeconds[stage] > 5:
                                                    manualSeconds[stage] -= 5

                                                    time.sleep(0.2)
                                                
                                                elif manualSeconds[stage] == 5:
                                                    manualSeconds[stage] = 3600

                                                    time.sleep(0.2)
                                                
                                                else:
                                                    continue

                                        elif GPIO.input(button3):
                                            display.lcd_display_string("TIME:          ", 2) #CLEAR LINE 2

                                            manualSeconds[stage] = 5

                                        elif GPIO.input(button5):
                                            manualSeconds = [5]
                                            manualStop = True

                                            break

                                        elif GPIO.input(button6):                                        
                                            display.lcd_clear()
                                            display.lcd_display_string("    TIME SET    ", 1) #PRINT LINE 1
                                            time.sleep(1)
                                            display.lcd_clear()
                                            break
                                        else:
                                            continue
                                    
                                    if manualStop:
                                        break

                                    while not manualStop:
                                        
                                        display.lcd_display_string("STAGE " + str(stage), 1) #PRINT LINE 1
                                        display.lcd_display_string("SPEED:" + str(manualSpeeds[stage]) + " RPM", 2) #PRINT LINE 2
                                        
                                        if not GPIO.input(button1):
                                            display.lcd_display_string("SPEED:         ", 2) #CLEAR LINE 2

                                            if GPIO.input(button4):
                                                if manualSpeeds[stage] < 7000:
                                                    manualSpeeds[stage] += 500
                                                    time.sleep(0.2)
                                                
                                                elif manualSpeeds[stage] >= 7000 and manualSpeeds[stage] < 7200:
                                                    manualSpeeds[stage] = 7200
                                                    time.sleep(0.2)

                                                elif manualSpeeds[stage] >= 7200:
                                                    manualSpeeds[stage] = 500
                                                    time.sleep(0.2)
                                                
                                                else:
                                                    continue
                                            
                                            if not GPIO.input(button4):
                                                if manualSpeeds[stage] < 7200:
                                                    manualSpeeds[stage] += 50
                                                    time.sleep(0.2)
                                                
                                                elif manualSpeeds[stage] == 7200:
                                                    manualSpeeds[stage] = 500
                                                    time.sleep(0.2)
                                                
                                                else:
                                                    continue

                                        elif GPIO.input(button2):
                                            display.lcd_display_string("SPEED:         ", 2) #CLEAR LINE 2

                                            if GPIO.input(button4):

                                                if manualSpeeds[stage] >= 1000:
                                                    manualSpeeds[stage] -= 500
                                                    time.sleep(0.2)
                                                
                                                elif manualSpeeds[stage] > 500 and manualSpeeds[stage] < 1000:
                                                    manualSpeeds[stage] = 500
                                                    time.sleep(0.2)
                                                
                                                elif manualSpeeds[stage] <= 500:
                                                    manualSpeeds[stage] = 7200
                                                    time.sleep(0.2)

                                                else:
                                                    continue

                                            elif not GPIO.input(button4):
                                                if manualSpeeds[stage] > 500:
                                                    manualSpeeds[stage] -= 50
                                                    time.sleep(0.2)
                                                
                                                elif manualSpeeds[stage] == 500:
                                                    manualSpeeds[stage] = 7200
                                                    time.sleep(0.2)
                                                
                                                else:
                                                    continue
                                            
                                            else:
                                                continue

                                        elif GPIO.input(button3):
                                            display.lcd_display_string("SPEED:         ", 2) #CLEAR LINE 2

                                            manualSpeeds[stage] = 500

                                        elif GPIO.input(button5):
                                            manualSpeeds[stage] = 500
                                            manualStop = True
                                            
                                            break

                                        elif GPIO.input(button6):                                        
                                            display.lcd_clear()
                                            display.lcd_display_string("   SPEED  SET   ", 1) #PRINT LINE 1
                                            time.sleep(1)
                                            display.lcd_clear()
                                            break
                                        else:
                                            continue

                            if not manualStop:
                                display.lcd_clear()
                                display.lcd_display_string("    STARTING    ", 1) #PRINT LINE 1
                                time.sleep(1)

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

                                time.sleep(2)

                                setPosition = 0
                                manualStages = 1    
                                        
                                manualSeconds = [5]
                                manualSpeeds = [500]

                                break

                            else:

                                setPosition = 0
                                manualStages = 1    

                                manualSeconds = [5]
                                manualSpeeds = [500]

                                display.lcd_clear()
                                display.lcd_display_string("    CANCELED    ", 1) #PRINT LINE 1
                                time.sleep(1)
                                
                                break
                            
                elif GPIO.input(button5):
                    break
                
                else:
                    continue

        elif menuPosition == 1:

                display.lcd_clear()

                display.lcd_display_string(" EEM401 PROJECT ", 1) #PRINT LINE 1
                display.lcd_display_string("  SPIN  COATER  ", 2) #PRINT LINE 2
                time.sleep(3)

                display.lcd_display_string("  Yetkin AKYUZ  ", 1) #PRINT LINE 1
                display.lcd_display_string("      2020      ", 2) #PRINT LINE 2
                time.sleep(3)

                display.lcd_display_string("Duzce University", 1) #PRINT LINE 1
                display.lcd_display_string("E.E. Engineering", 2) #PRINT LINE 1
                time.sleep(3)

                display.lcd_display_string("Version:   " + versionInfo, 1) #PRINT LINE 1
                display.lcd_display_string("Date: " + dateInfo, 2) #PRINT LINE 1
                time.sleep(3)

        elif menuPosition == 2:
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

        elif menuPosition == 3:

            display.lcd_clear()
            display.lcd_display_string("  REBOOTING...  ", 1)  

            os.system("sh $(find ~ -iname SpinCoaterReboot.sh)")

            exit()

        else:
            continue
    else:
        continue
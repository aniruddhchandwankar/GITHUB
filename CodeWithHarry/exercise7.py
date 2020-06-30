# #Healthy programmer
#
# # 3.5 ltr water
#

# Water -  play water.mp3,remind user to drink 200ml water each time. He should input drank
#
# a log will be generated in a text file
#
# 3.5 ltrs water in a day between 9AM to 5PM
#
# Eyes - eyes.mp3
# every 30 minutes, he should do eye exercise and input eyedone, generate log
#
# Physical activity - physical.mp3 - All files in same directory
# every 45 minutes, exercise and input Exdone, generate log
#
# use wait before each
#
# use any modules
#
# MUST use pygame module to play audio

import pygame
import schedule
import time


def getdate():
    import datetime
    return datetime.datetime.now()

def water():
    print("Ta Da! Time to drink some water")
    pygame.mixer.init()
    pygame.mixer.music.load('water.mp3')
    pygame.mixer.music.play()
    time.sleep(10)
    with open("water.txt", "a") as f:
        f.write(f"\n[Date] {time.asctime()} \n")
        f.write(input("Have you drank a glass of water? [Drank]: \n"))

def eyes():
    print("Wo whooo! Time to do some eye exercises")
    pygame.mixer.init()
    pygame.mixer.music.load('eyes.mp3')
    pygame.mixer.music.play()
    time.sleep(10)
    with open("water.txt", "a") as f:
        f.write(f"\n[Date] {time.asctime()} \n")
        f.write(input("Have you done the eye exercise? [eyedone]: \n"))

def physical():.
    print("Finally! Time to do some physical exercises")
    pygame.mixer.init()
    pygame.mixer.music.load('physical.mp3')
    pygame.mixer.music.play()
    time.sleep(10)
    with open("water.txt", "a") as f:
        f.write(f"\n[Date] {time.asctime()} \n")
        f.write(input("Have you done some physical exercise? [exdone]: \n"))

schedule.every().day.at("18:24").do(water) and schedule.every(1).minutes.do(water)
schedule.every().day.at("18:24").do(eyes) and schedule.every(2).minutes.do(eyes)
schedule.every().day.at("18:24").do(physical) and schedule.every(3).minutes.do(physical)

while getdate().hour < 19:
    schedule.run_pending()
    time.sleep(1)

#!/usr/bin/env python

import time

def numName(num):
    if num == 1:
        return "one"
    elif num == 2:
        return "two"
    elif num == 3:
        return "three"
    elif num == 4:
        return "four"
    elif num == 5:
        return "five"
    elif num == 6:
        return "six"
    elif num == 7:
        return "seven"
    elif num == 8:
        return "eight"
    elif num == 9:
        return "nine"
    elif num == 10:
        return "ten"
    elif num == 11:
        return "eleven"
    elif num == 12:
        return "twelve"
    elif num == 13:
        return "thirteen"
    elif num == 14:
        return "fourteen"
    elif num == 15:
        return "fifteen"
    elif num == 16:
        return "sixteen"
    elif num == 17:
        return "seventeen"
    elif num == 18:
        return "eighteen"
    elif num == 19:
        return "nineteen"
    elif num == 20:
        return "twenty"
    elif num == 30:
        return "thirty"
    elif num == 40:
        return "forty"
    elif num == 50:
        return "fifty"
    elif num == 0:
        return "twelve"
    elif num > 20 and num < 30:
        return "twenty-"+numName(num-20)
    elif num > 30 and num < 40:
        return "thirty-"+numName(num-30)
    elif num > 40 and num < 50:
        return "forty-"+numName(num-40)
    elif num > 50 and num < 60:
        return "fifty-"+numName(num-50)
    
def paddedTime():
        timeNow = time.localtime()
        hour = timeNow.tm_hour
        minute = timeNow.tm_min
                      
        if minute == 15:
            ans = "A quarter after "+numName(hour % 12)
        elif minute == 30:
            ans = "Half past "+numName(hour % 12)
        elif minute == 45:
            ans = "A quarter to "+numName((hour+1) % 12)
        elif hour == 0 and minute == 0:
            ans = "Midnight"
        elif hour == 12 and minute == 0:
            ans = "Noon"
        elif minute == 0:
            ans = numName(hour % 12)+" o'clock"
        elif minute < 10:
            ans = numName(hour % 12)+" o-"+numName(minute)
        else:
            ans = numName(hour % 12)+" "+numName(minute)
        return ans

def printTime():
    print paddedTime()


if __name__ == "__main__":
    printTime()

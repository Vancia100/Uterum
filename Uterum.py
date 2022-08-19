#TODO implement a actualy good fan speed curve, perhaps PID
#TODO add correct PWM syntax
#TODO implemt that the buttons have different Default fan Setting.
#TODO cleanup FanAutoChange, Arrange Arguments, Custom fan speed.


import time
import threading
import Thermometer
import GPIO #fake to make it not spit out errors when testing
#import RPi.GPIO as GPIO #real script


Toltemp = 20, 22 #The tolerable temperatures.
Agrev = 25 #How agresive the fan curve is
Dif = 20  #How agresivly the fan curve dips when huge difference in temp outide and inside unsure if this is final.


FanAuto = False
FanOn = False

def Fan(hastighet):
        if hastighet > 100:
                GPIO.PWM(100) #TODO add in the correct PWM syntax
        elif  hastighet > 20:
                GPIO.PWM(20)
        else:
                GPIO.PWM(hastighet)      


#These functions can be called from outside the program to change the values.
def FanAutoChange():
        global FanAuto
        if FanAuto == True:
                FanAuto = False
                if FanOn == True:
                        Fan(100)
                else:
                        Fan(0)
        elif FanAuto == False:
                FanAuto == True
                StartAuto()
def FanOnChange():
        global FanOn
        if FanOn == False:
                FanOn = True
                Fan(100)
        if FanOn == True:
                FanOn = True
                Fan(0)

def CheckFan():
        global FanAuto, FanOn
        return(FanAuto, FanOn)


def Buttons():
        print("the buttons are now enabled!")
        while True:
                if GPIO.Button == True:
                        FanOnChange()
                        while GPIO.Button == True:
                                time.sleep(0.5)

                elif GPIO.Button2 == True and FanAuto == False:
                        FanAutoChange()
                        while GPIO.Button2 == True:
                                time.sleep(0.5)
                else:
                        time.sleep(0.2)


def StartAuto():
        T2 = threading.Thread(target=FanAutoSys)
        T2.start()           

def FanAutoSys():
        while True:
                UteTemp = Thermometer.read_temp()
                IneTemp = Thermometer.read_temp2()
                if not(Toltemp[0] <= IneTemp <= Toltemp[1]) and ((IneTemp > UteTemp and IneTemp > Toltemp[1]) or (IneTemp > UteTemp and IneTemp < Toltemp[0])):
                        Fan(round(Agrev*abs(IneTemp-(sum(Toltemp)/2))/(abs(IneTemp-UteTemp)*(1/Dif+1))))
                        time.sleep(1)
                else:
                        time.sleep(1)
                if FanAuto == False:
                        break


def main():
        GPIO.cleanupp()
        GPIO.setmode(GPIO.BCM)
        T1 = threading.Thread(target=Buttons)
        T1.start()
        StartAuto()
if __name__ == "__main__":
        main()

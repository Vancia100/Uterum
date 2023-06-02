#TODO implement a actualy good fan speed curve, perhaps some form of PID
#TODO add correct PWM syntax
#TODO implemt that the buttons have different Default fan Setting.
#TODO cleanup FanAutoChange, Arrange Arguments, Custom fan speed.


import time
import threading
import Thermometer
import GPIO #fake to make it not spit out errors when testing
#import RPi.GPIO as GPIO #real script

class PID:
    def __init__(self, Kp, Ki, Kd, setTemp):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.setTemp = setTemp

        self.lastValue = 0
        self.integral = 0
    
    def newValue(self, value, seperate):
        Amount = self.setTemp - value
        P = self.Kp * Amount
        self.integral += Amount
        I = self.Ki * self.integral
        D = self.Kd * Amount - self.lastValue
        self.lastValue = Amount
        if seperate == True:
            print(P, I, D)
        return abs(P+I+D)
    
    def reset(self):
        self.integral = 0


FanAuto = False
FanOn = False

def Fan(hastighet):
        if hastighet > 100:
                GPIO.PWM(100) #TODO add in the correct PWM syntax
        elif hastighet >= 0:
               GPIO.PWM(STOP)
        elif  hastighet > 20:
                GPIO.PWM(20)
        else:
                GPIO.PWM(hastighet)

def FanAutoSys():
        Toltemp = 20
        timeOut = 40
        # Kp, Ki, Kd, The dissired temperatur
        PIDSystem = PID(1,1,1,Toltemp)
        while FanAuto:
                UteTemp = Thermometer.read_temp()
                IneTemp = Thermometer.read_temp2()
                if ((IneTemp > UteTemp and IneTemp > Toltemp) or (IneTemp < UteTemp and IneTemp < Toltemp)):
                        
                        Fan(PIDSystem.newValue(IneTemp)*1)
                        time.sleep(timeOut)
                else:
                        time.sleep(timeOut)
        PIDSystem.reset()

def StartAuto():
        T2 = threading.Thread(target=FanAutoSys)
        T2.start()
        T2.join()


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
                Fan(100)
        if FanOn == True:
                Fan(0)
        FanOn != FanOn

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

def main():
        GPIO.cleanupp()
        GPIO.setmode(GPIO.BCM)
        T1 = threading.Thread(target=Buttons)
        T1.start()
        StartAuto()
if __name__ == "__main__":
        main()

import time
import threading
import Thermometer
import GPIO

#GPIO skit till RPi


#Sätter läget på GPIO pint till att räkna pin numer som BCM, Vilket man behöver googla upp.

#De variablar som vi kommer att behöva för att räkna ut temperaturerna och fläktarnas värde
Toltemp = 20, 22
Agrev = 25
Dif = 20 
#Dif är skilnaden i temperatur mellan inne och ute som behövs för att fläktarna ska gå hälften så långsamt

FanAuto = True
FanOn = True

def Fan(hastighet):
        if hastighet > 100:
                GPIO.PWM(100) #Kommer ej ihåg om det här är det faktiskt skriptet.
        elif  hastighet > 20:
                GPIO.PWM(20)
        else:
                GPIO.PWM(hastighet)
        #Funktion för att sätta fläkthastigheten

def Buttons():
        global FanAuto, FanOn
        while True:
                if GPIO.Button == True:
                        if FanAuto == True:
                                FanAuto = False
                                if FanOn == True:
                                        Fan(100)
                                else:
                                        Fan(0)
                        elif FanAuto == False:
                                FanAuto == True
                                StartAuto()
                        while GPIO.Button == True:
                                time.sleep(0.5)

                if GPIO.Button2 == True and FanAuto == False:
                        if FanOn == False:
                                FanOn = True
                                Fan(100)
                        if FanOn == True:
                                FanOn = True
                                Fan(0)
                        while GPIO.Button2 == True:
                                time.sleep(0.5)
                time.sleep(1)


def FanAutoSys():
        while True:
                print("This is also on")
                UteTemp = Thermometer.read_temp()
                IneTemp = Thermometer.read_temp2()
                if not(Toltemp[0] <= IneTemp <= Toltemp[1]) and ((IneTemp > UteTemp and IneTemp > Toltemp[1]) or (IneTemp > UteTemp and IneTemp < Toltemp[0])):
                        Fan(round(Agrev*abs(IneTemp-(sum(Toltemp)/2))/(abs(IneTemp-UteTemp)*(1/Dif+1))))
                        time.sleep(1)
                else:
                        time.sleep(1)
                if FanAuto == False:
                        pass
                        #break
                


#Denna del är det som faktiskt kommer att göra någonting:
#öppnar en thread på de olika funktionerna
def StartAuto():
        T2 = threading.Thread(target=FanAutoSys)
        T2.start()
        T2.join()


if __name__ == "__main__":
        GPIO.cleanupp()
        GPIO.setmode(GPIO.BCM)
        T1 = threading.Thread(target=Buttons)
        T1.start()
        StartAuto()
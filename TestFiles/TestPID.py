from time import sleep
#import TestFile2
from TestGraphs import readTemp as getValue # does not work with readLinnear

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


TempTime = []
Language = True #True for Exponential false for linnear

#Driver fram ett budget "I"
#def getValue():
#    if Language:
#        return(float(TestFile2.readTemp()))
#    else: 
#        return(float(TestFile2.readLinnear()))

def PIDOld():
    Temp1 = getValue()
    if Temp1 != None:
        TempTime.append(Temp1)
        if len(TempTime) > 120:
            TempTime.remove(TempTime[0])
        return(f'{TempTime} \n{round(Temp1 - sum(TempTime)/len(TempTime), 3)}')
        #print(TempTime)
        #print(round(Temp1 - sum(TempTime)/len(TempTime), 2))

def TestPID(X):
    Test = []
    while len(TempTime) < 60:
        Temp1 = getValue()
        if Temp1 != None:
            TempTime.append(Temp1)
    for _ in range(0,X):
        Temp1 = getValue()
        TempTime.append(Temp1)
        TempTime.remove(TempTime[0])
        Test.append(round(Temp1-sum(TempTime)/len(TempTime),3))
    print(Test)

def TestPIDNew(Temp = 20, X = 10, seperate = True):
    NewPID = PID(2, 0.5, 1, 20)
    for i in range(X):
        print(NewPID.newValue(Temp, seperate))


def main():
    while True:
        print(PID())
        sleep(0.8)
if __name__ == "__main__":
    pass
    TestPIDNew(30)
    #(main())
    #TestPID(int(input("Wright the number of tries to test: ")))
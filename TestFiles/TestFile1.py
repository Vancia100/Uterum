from time import sleep
#import TestFile2
from TestFile2 import readTemp as getValue # does not work with readLinnear


TempTime = []
Language = True #True for Exponetion false for linnear

#Driver fram ett budget "I"
#def getValue():
#    if Language:
#        return(float(TestFile2.readTemp()))
#    else: 
#        return(float(TestFile2.readLinnear()))

def PID():
    Temp1 = getValue()
    if Temp1 != None:
        TempTime.append(Temp1)
        if len(TempTime) > 60:
            TempTime.remove(TempTime[0])
        return(f'{TempTime} \n{round(Temp1 - sum(TempTime)/len(TempTime), 3)}')
        #print(TempTime)
        #print(round(Temp1 - sum(TempTime)/len(TempTime), 2))

def TestPID():
    Test = []
    for i in range(0,60):
        Temp1 = getValue()
        if Temp1 != None:
            TempTime.append(Temp1)
            if len(TempTime) > 60:
                TempTime.remove(TempTime[0])
            Test.append(round(Temp1-sum(TempTime)/len(TempTime),3))
    print(Test)

def main():
    while True:
        print(PID())
        sleep(0.8)
if __name__ == "__main__":
    pass
    #(main())
    TestPID()
import json
from ScriptFile import TestInput

class Jimjson:
    def __init__(self, Pr=None,Rep5=None,Rep8=None,Rep12=None, MaxRep = None):
        self.Pr=Pr
        self.Rep5=Rep5
        self.Rep8=Rep8
        self.Rep12=Rep12
        self.MaxRep = MaxRep

    def FileRaw(Value = None):
        with open("TestFiles/DaJimShit/Jim.json", "r+") as File:
            if Value != None:
                File.write(json.dumps(Value, indent=2))
            else:
                return(json.loads(File.read()))

    def jsonTools(Input = None):
        Jim = {}
        if Input:
            for i in Input:
                Jim[i] = Input[i].__dict__
            Jimjson.FileRaw(Jim)
        else:
            ImportedList = Jimjson.FileRaw()
            for i in ImportedList:
                try:
                    Jim[i] = Jimjson(ImportedList[i]["Pr"], ImportedList[i]["Rep5"], ImportedList[i]["Rep8"], ImportedList[i]["Rep12"], ImportedList[i]["MaxRep"])
                except TypeError:
                    print("Imported JSON has errors! \n Please fix issues and try again.")
                    exit
            return(Jim)

    def PrintDic(klass, name=None):
        print(klass)
        if name !=None:
            print(f"{name}:")
        for i in klass:
            if klass[i] != None:
                print(i,":",klass[i])

def assignValues(What = None):
    Things = ["Pr","Rep5","Rep8","Rep12", "MaxRep"]
    Inputs = []
    for i in range(len(Things)):
        try:
            inps = input(f"What do you want {Things[i]} to be?: ")
            inps = None if not(inps) else float(inps)
            Inputs.append(inps)
        except ValueError:
            print("You need to put in a number! \nYour input has been asumed to be None!")
            Inputs.append(None)
    return(Inputs)

def main():
    Jim = Jimjson.jsonTools()
    InpType = input("What if: ")
    if InpType:
        talks = ["Pr","Rep5","Rep8","Rep12", "MaxRep"]
        Inps = []
        try:
            Jimjson.PrintDic(Jim[InpType].__dict__, InpType)
            if TestInput(input("Do you want to change any of the values (blank for no): ")):
                Inps = assignValues()
                Jim[InpType].Pr = Inps[0]if Inps[0] != None else Jim[InpType].Pr
                Jim[InpType].Rep5 = Inps[1]if Inps[1] != None else Jim[InpType].Rep5
                Jim[InpType].Rep8 = Inps[2]if Inps[2] != None else Jim[InpType].Rep8
                Jim[InpType].Rep12 = Inps[3]if Inps[3] != None else Jim[InpType].Rep12
                Jim[InpType].MaxRep = Inps[4]if Inps[4] != None else Jim[InpType].MaxRep
                Jimjson.jsonTools(Jim)
        except KeyError:
            if TestInput(input(f"Do you want to add a new value for {InpType}: " )):
                Inps = assignValues()
                Jim[InpType] = Jimjson(Inps[0],Inps[1],Inps[2],Inps[3], Inps[4])
                Jimjson.jsonTools(Jim)
    else:
        for i in Jim:
            Jimjson.PrintDic(Jim[i].__dict__, i)

if __name__=="__main__":   
    while True:      
        main()
import json

class Jimjson:
    def __init__(self, Pr=None,Rep5=None,Rep8=None,Rep12=None):
        self.Pr=Pr
        self.Rep5=Rep5
        self.Rep8=Rep8
        self.Rep12=Rep12
    def file(Value = None):
        with open("TestFiles/Jim.json", "r+") as fake:
            if Value != None:
                fake.write(json.dumps(Value, indent=2))
            else:
                return(json.loads(fake.read()))
    def jsonTools(Inp = None):
        Jim = {}
        if Inp != None:
            for i in Inp:
                Jim[i] = Inp[i].__dict__
            Jimjson.file(Jim)
        else:
            ImportedList = Jimjson.file()
            for i in ImportedList:
                try:
                    Jim[i] = Jimjson(ImportedList[i]["Pr"], ImportedList[i]["Rep5"], ImportedList[i]["Rep8"], ImportedList[i]["Rep12"])
                except TypeError:
                    print("imported JSON has errors! \n Pease fix issues and try again.")
                    return(None)
            return(Jim)
    def PrintDic(klass, name=None):
        try:
            if name !=None:
                print(f"{name}:")
            for i in klass:
                print(i,":",klass[i])
        except TypeError:
            print(klass)



def main():
    Jim = Jimjson.jsonTools()
    InpType = input("What if: ")
    if InpType:
        try:
            Jimjson.PrintDic(Jim[InpType].__dict__, InpType)
        
            if input("Do you want to change any of the values (blank for no): "):
                print("Balls")
        except KeyError:
            if input("Do you want to add a new value (leave empty for no): " ):
                Inps = []
                talks = ["Pr","Rep5","Rep8","Rep12"]
                for i in range(4):
                    inps = input(f"How mush weight can you take on {InpType} for {talks[i]} reps?: ")
                    if not(inps):
                        inps = None
                    Inps.append(inps)
                Jim[InpType] = Jimjson(Inps[0],Inps[1],Inps[2],Inps[3])
                Jimjson.jsonTools(Jim)
                
    else:
        for i in Jim:
            Jimjson.PrintDic(Jim[i].__dict__, i)

if __name__=="__main__":
    while True:   
        main()
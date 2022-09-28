import json

class Jimjson:
    def __init__(self, Pr=None,Rep5=None,Rep8=None,Rep12=None):
        self.Pr=Pr
        self.Rep5=Rep5
        self.Rep8=Rep8
        self.Rep12=Rep12

def FileRaw(Value = None):
    with open("TestFiles/Jim.json", "r+") as fake:
        if Value != None:
            fake.write(json.dumps(Value, indent=2))
        else:
            return(json.loads(fake.read()))

def MakeDic(Thing):
    Dic = Thing.__dict__
    NewDic = {}
    for i in Dic:
        if Dic[i] != None:
            NewDic[i] = Dic[i]
    return(NewDic)
            
Squats = Jimjson(100,90,80,70)
print(MakeDic(Squats))

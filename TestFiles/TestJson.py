import json

def FileRaw(Value = None):
    with open("TestFiles/Jim.json", "r+") as fake:
        if Value != None:
            fake.write(json.dumps(Value, indent=2))
        else:
            return(json.loads(fake.read()))


def main():
    Inp = input("Skirv in värde:")
    Jim = FileRaw()
    if not(Inp):
        for item in Jim:
            try:
                for thing in item:
                    print(item,":",item[thing])
            except TypeError:
                print("this on error")
                print(item,":", Jim[item])
    else:
        try:
            for thing in Jim[Inp]:
                print(thing, Jim[Inp][thing])
            InputNew = input("skriv in om du vill lägga till yterligare ett sökvärde: ")
            if InputNew:
                Jim[Inp] = {InputNew:input(f"Skriv in det nya värdet för värdet {InputNew}: ")}
        except KeyError:
            val = input(f"Nytt sökvärde skriv skriv nytt sökvärde för {Inp}: ")
            if val:
                Jim[Inp] = {val:input(f"Skriv värdet för {val}: ")}
                FileRaw(Jim)
        except TypeError:
            print(Jim[Inp])

if __name__ == "__main__":
    while True:
        main()
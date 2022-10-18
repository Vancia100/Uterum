import json

def FileRaw(Value = None):
    with open("TestFiles/DaJimShit/Jim.json", "r+") as fake:
        if Value != None:
            fake.write(json.dumps(Value, indent=2))
        else:
            return(json.loads(fake.read()))


def main():
    Inp1 = input("Skirv in sökvärde: ")
    Jim = FileRaw()
    if not(Inp1):
        try:
            for item in Jim:
                try:
                    for thing in Jim[item]:
                        print(item,":", thing,":", Jim[item][thing])
                except TypeError:
                    print(item,":", Jim[item])
        except TypeError:
            print(Jim)
    else:
        try:
            for thing in Jim[Inp1]:
                print(thing,":", Jim[Inp1][thing])
            Inp2 = input("skriv in om du vill lägga till yterligare ett sökvärde: ")
            if Inp2:
                Jim[Inp1][Inp2] = input(f"Skriv om du vill lägga till ett värde för {Inp2}: ")
                FileRaw(Jim)
        except KeyError:
            Inp2 = input(f"Nytt sökvärde skriv skriv nytt sökvärde för {Inp1}: ")
            if Inp2:
                Inp3 = input(f"Skriv värdet för {Inp2}: ")
                if Inp3:
                    Jim[Inp1] = {Inp2:Inp3}
                else:
                    Jim[Inp1] = Inp2
                FileRaw(Jim)
        except TypeError:
            print(Inp1, ":", Jim[Inp1])
            Inp2 = input(f"Skriv värdet du vill byta ut {Jim[Inp1]} mot: ")
            if Inp2:
                Inp3 = input("Skriv in värdet om det ska bli en diktionär: ")
                if Inp3:
                    Jim[Inp1] = {Inp2:Inp3}
                else:
                    Jim[Inp1] = Inp2
                FileRaw(Jim)

def definer(Text):
    try:
        return(int(Text))
    except (TypeError):
        return(bool(Text))


if __name__ == "__main__":
    while True:
        main()

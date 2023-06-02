def TestInput(Input):
    if Input:
        if str(Input).lower() == "false" or str(Input).lower() == "nej" or str(Input).lower() == "no":
            return(False)
        else:
            return(True)
    else:
        return(False)
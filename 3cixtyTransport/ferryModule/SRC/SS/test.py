

def validateNaptan(Naptan):
    if (Naptan.find('E') != -1 and Naptan.find('.') != -1):
        return 5
    else:
        return 0

test = "x111111oo"
print validateNaptan(test)



def validateNaptan(Naptan):
    if Naptan[-1].isdigit() and Naptan[-2].isdigit():
        return 5
    else:
        if Naptan[0] == "9":
            return 0
        else:
            return 5
        return 0


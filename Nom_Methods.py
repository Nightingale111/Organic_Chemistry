# Nomenclature Methods

# Potential Future improvement --> Information Hiding
# Create a master class and input functional groups as arguments

# Functional Group   Name as Suffix  Name as Substituent
# Carboxylic acids   -oic acid       carboxy
# Esters             -oate           alkoxycarbonyl
# Acid halides       -oyl halide     halocarbonyl
# Amides             -amide          carbamoyl
# Nitriles           -nitrile        cyano
# Aldehydes          -al             oxo
# Ketones            -one            oxo
# Alcohols           -ol             hydroxy
# Amines             -amine          amino
# Ethers             ether           alkoxy

def nom_onboarding():
    print("   ")
    print("   ")
    print("Welcome to the Nomenclature of Polyfunctional Compounds Quiz")
    print("   ")
    print("You will be presented with a series of questions testing your")
    print("knowledge of functional group nomenclature. ")
    print("Type 'okay' to continue")
    print("   ")
    print("   ")

    answer = input("> ")


def carboxylicAcid(score):
    print("   ")
    print("   ")
    print("What is the name as suffix for Carboxylic Acids?")
    print("   ")
    print("   ")

    answer = input("> ")

    if answer == "-oic acid" or answer == "oic acid":
        print("Correct!")
        score = score + 10
        print("Your score is:", score)
    else:
        print("Incorrect")
        print("The correct answer was -oic acid")
        score = score - 10
        print("Your score is:", score)

    print("   ")
    print("   ")
    print("What is the name as substituent for Carboxylic Acids?")
    print("   ")
    print("   ")

    answer = input("> ")

    if answer == "carboxy" or answer == "carboxy-":
        print("Correct!")
        score = score + 10
        print("Your score is:", score)
    else:
        print("Incorrect")
        print("The correct answer was carboxy")
        score = score - 10
        print("Your score is:", score)
    return score


def Ester(score):
    print("   ")
    print("   ")
    print("What is the name as suffix for Esters?")
    print("   ")
    print("   ")

    answer = input("> ")

    if answer == "-oate" or answer == "oate":
        print("Correct!")
        score = score + 10
        print("Your score is:", score)
    else:
        print("Incorrect")
        print("The correct answer was -oate")
        score = score - 10
        print("Your score is:", score)

        print("   ")

    print("   ")
    print("What is the name as substituent for Esters?")
    print("   ")
    print("   ")

    answer = input("> ")

    if answer == "alkoxycarbonyl" or answer == "alkoxycarbonyl-":
        print("Correct!")
        score = score + 10
        print("Your score is:", score)
    else:
        print("Incorrect")
        print("The correct answer was alkoxycarbonyl")
        score = score - 10
        print("Your score is:", score)
    return score


def onboarding():

    print("   ")
    print("   ")
    print("Welcome to the Interactive Organic Chemistry Study Guide")
    print("   ")
    print("You will be presented with a series of questions, and")
    print("will respond by typing your answer directly into the program.")
    print("   ")
    print("Type 'okay' to continue")

    okay = input("> ")


def ether():
    print("   ")
    print("What is this functional group?")
    print("   ")
    print("   ..")
    print("R---O---R")
    print("    ..")
    print("   ")
    answer = input("> ")
    #score = 0

    if answer == "ether" or answer == "Ether":
        print("Correct!")
        #score += 10
        #print("Your score is:", score)
    else:
        print("Incorrect")
        print("The correct answer was ether")
        #score -= 10
        #print("Your score is:", score)
    return


def thiol():
    print("   ")
    print("What is this functional group?")
    print("   ")
    print("   ..")
    print("R---SH")
    print("    ..")
    print("   ")
    answer = input("> ")
    #score = 0

    if answer == "thiol" or answer == "Thiol":
        print("Correct!")
        #score += 10
        #print("Your score is:", score)
    else:
        print("Incorrect")
        print("The correct answer was thiol")
        #score -= 10
        #print("Your score is:", score)
    return


def alkene():
    print("   ")
    print("What is this functional group?")
    print("   ")
    print("R        R")
    print(" \      /")
    print("  C == C")
    print(" / " + "     \ ")
    print("R        R")
    print("   ")
    answer = input("> ")
    #score = 0

    if answer == "alkene" or answer == "Alkene":
        print("Correct!")
        #score += 10
        #print("Your score is:", score)
    else:
        print("Incorrect")
        print("The correct answer was alkene")
        #score -= 10
        #print("Your score is:", score)
    return

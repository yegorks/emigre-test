result = ["stay in Russia", "Israel", "Japan", "Canada", "Germany", "Australia", "Scandinvia",
"China", "Islandia", "Cuba", "Great Britain", "Chezch", "Baltics", "USA (Alaska)", "Denmark"]

emigre = input("Enter your name: ")

print("Hello," + emigre + "\n"+
"If you decide to pass this test then you want to go away from the Motherland.\n"+
"And it is desirable to go far.\n"+
"This test will help you!\n")

print("If " + emigre + " want to start test then print y. If " + emigre + " is a patriot then print n.")
choise = input()
if choise == "y":
    print("Let's determine which country is right for you!")
elif choise == "n":
    print("Respect! But anyway...")
while choise != "y" and choise != "n":
    choise = input("Incorrect answer (you should input only y or n)")

print(emigre + ", do you hardworker?")
choise = input()
if choise == "y" or "n":
    if choise == "y":
        print(emigre + ", are you always ready to die?")
        choise = input()
        if choise == "y":
            print(emigre + ", what kind of death do you prefer?")
            deathes = ["from overwork at work", "death by the hand of the enemy", "suicide"]
            print(deathes)
            choise = input()
            if choise == deathes[0]:
                print(emigre + ", you should move to " + result[2])
            if choise == deathes[1]:
                print(emigre + ", you should move to " + result[1])
            if choise == deathes[2]:
                print(emigre + ", you should " + result[0])
            else:
                print("Incorrect answer (you should input one of the three options)")
        elif choise == "n":
            print(emigre + ", do you want forget about Russia?")
            choise = input()
            if choise == "y":
                print(emigre + ", you should move to " + result[3])
            elif choise == "n":
                print(emigre + ", you should move to " + result[4])
            else:
                print("Incorrect answer (you should input only y or n)")
        else:
            print("Incorrect answer (you should input only y or n)")

    elif choise == "n":
        print(emigre + ", do you want not to work at all?")
        choise = input()
        if choise == "y":
            print(emigre + ", do you agree to a fictitious marriage?")
            choise = input()
            if choise == "y":
                print(emigre + ", you should move to " + result[14])
            elif choise == "n":
                print(emigre + ", you should move to " + result[13])
            else:
                print("Incorrect answer (you should input only y or n)")
        elif choise == "n":
            print(emigre + ", and so that there were fewer Russians?")
            choise = input()
            if choise == "y":
                print(emigre + ", do you like insects?")
                choise = input()
                if choise == "y":
                    print(emigre + ", which ones?")
                    insects = ["alive", "fried"]
                    print(insects)
                    choise = input()
                    if choise == insects[0]:
                        print(emigre + ", you should move to " + result[5])
                    elif choise == insects[1]:
                        print(emigre + ", you should move to " + result[7])
                    else:
                        print("Incorrect answer (you should input one of the two options)")
                elif choise == "n":
                    print(emigre + ", you should move to " + result[8])
                else:
                    print("Incorrect answer (you should input only y or n)")
            elif choise == "n":
                print(emigre + ", do you have money to move?")
                choise = input()
                if choise == "n":
                    print(emigre + ", you should move to " + result[12])
                elif choise == "y":
                    print(emigre + ", do you like be always drunk?")
                    choise = input()
                    if choise == "y":
                        print(emigre + ", you should move to " + result[11])
                    elif choise == "n":
                        print(emigre + ", do you obey the law?")
                        choise = input()
                        if choise == "y":
                            print(emigre + ", you should move to " + result[6])
                        elif choise == "n":
                            print(emigre + ", you should move to " + result[10])
                        elif choise == ":)":
                            print(emigre + ", you should move to " + result[9])
                        else:
                            print("Incorrect answer (you should input only y or n)")
                    else:
                        print("Incorrect answer (you should input only y or n)")
                else:
                    print("Incorrect answer (you should input only y or n)")
            else:
                print("Incorrect answer (you should input only y or n)")
        else:
            print("Incorrect answer (you should input only y or n)")
    else:
            print("Incorrect answer (you should input only y or n)")





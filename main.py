from wonderwords import RandomWord

settings = {
    "Words" : 3,
    "Char" : False,
    "Done" : False,
    "LengthofWords" : 6
}

password = ""

while settings["Done"] == False:
    if ans == 1:
        for i in range(settings["Words"]):
            temp = RandomWord().word()
            while (len(temp) > settings["LengthofWords"]):
                temp = RandomWord().word()
            temp.capitalize()
            password += temp
    
    print("Your password is ", password)

    print("Would you like to generate again? Y/N")
    ans = input()
    if ans != "Y" and ans != "y":
        settings["Done"] = True
    else:
        print("Press 1 to generate a password")
        print("Press 2 to change settings")
        ans = int(input())
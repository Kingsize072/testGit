userName = input("Please enter your Username : ")
password = input("Please enter your Password : ")
if userName == "admin" and password == "1234":
    print("Log in!!")
    print("What do you want to do please select?")
    print('Put "1" for Function -- Tax Calculate')
    print('Put "2" for Function -- Price calculater')
    userInput = input("Please input function : ")
    if userInput == "1":
        price1 = int(input("Price : "))
        vat = price1 * (7/100)
        total = price1 + vat
        print("Price with tax. :", total, "THB")
    elif userInput == "2":
        price2 = int(input("Please enter Price1 :"))
        price3 = int(input("Please enter Price2: "))
        total2 = price2 + price3
        print(total2)

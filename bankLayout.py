#writer heetp28

import os
import time
import random

#Variables
inWallet = 500
inBank = 0

#deposite
def deposite():
    global inWallet
    global inBank

    time.sleep(0.5)

    Amount = int(input("How much do you want to deposite?(Enter 0 to go Back)\n> ")) #Amount for Depositing


    if inWallet > 0 and Amount <= inWallet and Amount != 0:
        inWallet = inWallet - Amount
        inBank = inBank + Amount
        print("Amount Deposited Successfully.")
        time.sleep(0.5)

    elif Amount > inWallet:
        print("You don't have that much money.")
        time.sleep(1)

    elif Amount == 0: #To go back
        pass

    else:
        print("Invalid")
        time.sleep(0.5)


#withdraw
def withdraw():
    global inWallet
    global inBank

    time.sleep(0.5)

    Amount = int(input("How much would you like to Withdraw? (Enter 0 to go back)\n> ")) #Amount for Withdrawing
    if inBank > 0 and Amount <= inBank and Amount != 0:
        inBank = inBank - Amount
        inWallet = inWallet + Amount
        print("Withdrawal was Successful.")
        time.sleep(0.5)

    elif Amount > inBank:
        print("You don't have that much money.")

    elif Amount == 0: #To go back
        pass

    else:
        print("Invalid.")

#earn
def earn():
    global inWallet

    print("Type the Following paragraph to earn:")
    Para = "Python is Good for a lot of Things." #Paragraph to type
    typedPara = input(f"{Para} \n> ")
    Amount = random.randint(50,100) #Random amount to give between 50 and 100

    if typedPara == Para:
        print(f"Great work you got ₹{Amount}")
        inWallet = inWallet + Amount
        time.sleep(0.5)

    else:
        print("Sorry try again next time.")
        time.sleep(0.5)

#clear
def clear():
    os.system('cls')

#Loop
while True:
    time.sleep(0.5)
    print("What would you like to do?")
    print(f"""
Wallet: ₹{inWallet}
Bank: ₹{inBank}

1) Deposite
2) Withdraw
3) Earn
4) Exit
""")
    
    #Input
    selOption = input("Select an Option\n> ")
    selOption = selOption.upper()
    if selOption == "1" or selOption == "D" or selOption == "DEPOSITE":
        deposite()
        clear()

    elif selOption == "2" or selOption == "W" or selOption == "WITHDRAW":
        withdraw()
        clear()

    elif selOption == "3" or selOption == "EA" or selOption == "EARN":
        earn()
        clear()

    elif selOption == "4" or selOption == "EX" or selOption == "EXIT":
        break

    else:
        print("Invalid")
        time.sleep(0.5)

clear()
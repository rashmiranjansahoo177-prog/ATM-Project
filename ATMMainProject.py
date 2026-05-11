#ATMMainProject.py<--Main program
from ATMExcept import DepositError, WithDrawError, InSuffFundError
from ATMMenu import menu
from ATMOperations import deposit,withdraw,balenq
while(True):
    try:
        menu()
        ch=int(input("Enter your choice: "))
        match(ch):
            case 1:
                try:
                    deposit()
                except DepositError:
                    print("\tDON'T ENTER ZERO OR -VE VALUES FOR DEPOSITS")
                except ValueError:
                    print("\tDON'T ENTER ALNUMS,STRS AND SYMBOLS for deposit")
            case 2:
                try:
                    withdraw()
                except WithDrawError:
                    print("\tDON'T ENTER ZERO OR -VE VALUES FOR withdraw Operations")
                except InSuffFundError:
                    print("\tUR Account Does not Contain Suff. Funds")
                except ValueError:
                    print("\tDON'T ENTER ALNUMS,STRS AND SYMBOLS for withdraw")

            case 3:
                balenq()
            case 4:
                print("Thx for using Project")
                break
            case _:
                print("\tUR Selection of Operation is wrong-try again")
    except ValueError:
        print("\tDon't Enter alnums,strs and symbols for Choice-try again")

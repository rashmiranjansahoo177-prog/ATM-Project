#ATMOperations.py<---File Name and Module Name
from ATMExcept import DepositError,WithDrawError,InSuffFundError
bal=500.00 # Min amount in the account
def deposit():
    damt=float(input("Enter Ur Deposit Amount: ")) # ValueError
    if(damt<=0):
        raise DepositError
    else:
        global bal
        bal=bal+damt
        print("\tUR Account xxxxxxx123 Credited with INR:{}".format(damt))
        print("\tNOW UR Account xxxxxxx123 Balance after deposit: {}".format(bal))

def withdraw():
    global bal
    wamt=float(input("Enter Ur Withdraw Amount: ")) # ValueError
    if(wamt<=0):
        raise WithDrawError
    else:
        if((wamt+500)>bal):
            raise InSuffFundError
        else:
            bal=bal-wamt
            print("\tUR Account xxxxxxx123 Debited with INR:{}".format(wamt))
            print("\tNOW UR Account xxxxxxx123 Balance after withdraw: {}".format(bal))

def balenq():
    print("\tUR Account xxxxxxx123 Balance: {}".format(bal))


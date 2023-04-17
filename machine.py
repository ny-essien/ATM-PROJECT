#handle insufficient funds for transfer and withdraw
#use 8052 as your default pin

from re import I
import time
from file import filemark  

class Atm(object):

    def __init__(self):

        self.actions = [ "QuickTeller","Transfer","Withdrawal","Balance","Change Pin","Block Card"]

        self.banks = {1:"Access Bank",2:"Diamond Bank",
                        3:"Fidelity Bank",4:"FCMB",5:"First Bank",6:"GTBank",7:"Polaris Bank",
                        8:"UBA",9:"Union Bank",10:"Streling Bank"}

        self.amounts = {1:"1000", 2:"2000",3:"3000",4:"5000",5:"10000",6:"20000",7:"Others"}

        self.acc_type = {1:"Current",2:"Savings",3:"Debit"}

        self.balance  = 20000000

        self.card_pin = "8052"

        print("Welcome")
        time.sleep(0.5)
        print("Fidelity We keep our word")

        self.HomeScreen()

    def HomeScreen(self):
        atm = filemark()

        #enter card pin
        self.enter_pin = atm.enter_pin()
        #delay actions for 2 seconds
        time.sleep(2)
        #display actions to be carries out by user
        atm.display_options(self.actions)
        #Choose the action you will like to carry out
        print("Choose Action: ")
        self.action = input()

        if self.action == "1":
            self.QuickTeller()

        elif self.action == "2":
            self.Transfer()

        elif self.action == "3":
            self.Withdrawal()

        elif self.action == "4":
            self.Balance()

        elif self.action == "5":
            self.ChangePin()

        elif self.action == "6":
            self.BlockCard()


    def QuickTeller(self):
        print("QuickTeller")

    def Transfer(self):
        transfer = filemark()
        #choose benefactors account type
        print("Enter Beneficiary Account Type: ")
        transfer.display_dict(self.acc_type)
        self.benefactor_account_type = input()

        #enter the bank to which the transfer should be made
        print("Enter Destination Bank:")
        transfer.display_dict(self.banks)
        self.bank = input()

        #enter the account number of the benefactor
        while True:
            print("Enter Destination Acccount: ")
            self.account_number = input()
            if self.account_number:
                if len(self.account_number) < 10 or len(self.account_number) > 10:
                    print("Invalid Account Number")

                else: break

        #enter the amount you would like to send
       
        print("Choose Amount: ")
        transfer.display_dict(self.amounts)
        self.amount = int(input())
        if self.amount:

            if self.amount == "7":

                while True:
                    print("Enter Amount: ")
                    self.amount = input()
                    break

        if self.amount > self.balance:
            print("Insufficient Funds")

            self.another_transaction()

        #choose account type of the sender
        print("Choose Account Type: ")
        transfer.display_dict(self.acc_type)
        self.choose_account_type = input()

        #delay 1.5 seconds
        print("Please Wait...")
        time.sleep(1.5)
        print(f"Sending N{self.amounts[int(self.amount)]} to ...")
        print(f"Account Number: {self.account_number}")
        print(f"Account Name: Nsikan Yakmfiok Essien")
        print(f"Account Type: {self.acc_type[int(self.benefactor_account_type)]}")
        print(f"Bank Name: {self.banks[int(self.bank)]} ")
        print("")
        self.allow()
        print("")
        self.another_transaction()
        
    def Withdrawal(self):
        withdraw = filemark()
        withdraw.display_dict(self.acc_type)
        print("Choose Account Type: ")
        self.choose_account_type = input()

        #enter the amount you would like to withdraw
        print("Choose Amount: ")
        withdraw.display_dict(self.amounts)
        self.amount = input()

        if self.amount:

            if self.amount == "7":

                while True:
                    print("Enter Amount: ")
                    self.amount = input()
                    if self.amount > "20000":
                        print("Maximum Amount is 20000")

                    else: break

        self.allow()
        self.another_transaction()

    def Balance(self):
        bal = filemark()

        #choose account type
        print("Choose Account Type")
        bal.display_dict(self.acc_type)
        self.choose_account_type = input()

        if self.enter_pin == self.card_pin:
            #display balance to screen
            print(f"Balance: N{self.balance}")

        else:
            print("Incorrect pin")
            chances = 2

            while chances <= 2:
                self.enter_pin = bal.enter_pin()
                if self.enter_pin == self.card_pin:
                    #display balance to screen
                    print(f"Balance: N{self.balance}")
                    break

                elif self.enter_pin!= self.card_pin:
                    print("Incorrect Pin")
                    chances -= 1
                    if chances == 0:
                        print("Card Blocked Contact Financial Institution To Unblock")
                        break

        self.another_transaction()

    def ChangePin(self):

        changepin = filemark()
        #choose account type
        print("Choose Account Type: ")
        changepin.display_dict(self.acc_type)
        self.choose_account_type = input()

        if self.enter_pin:
            if self.enter_pin == self.card_pin:
                while True:
                    print("Enter New Pin: ")
                    self.new_pin = input()
                    print("Confirm New Pin")
                    self.confirm_new_pin = input()
                    
                    if self.new_pin == self.confirm_new_pin:
                        self.card_pin = self.confirm_new_pin
                        break

                    else:print("Pin Mismatch")

            else:
                print("Incorrect pin")
                chances = 2

                while chances <= 2:
                    self.enter_pin = changepin.enter_pin()
                    if self.enter_pin == self.card_pin:
                        #display balance to screen
                        while True:
                            print("Enter New Pin: ")
                            self.new_pin = input()
                            print("Confirm New Pin")
                            self.confirm_new_pin = input()
                            
                            if self.new_pin == self.confirm_new_pin:
                                self.card_pin = self.confirm_new_pin
                                break

                            else:print("Pin Mismatch")

                    elif self.enter_pin!= self.card_pin:
                        print("Incorrect Pin")
                        chances -= 1
                        if chances == 0:
                            print("Card Blocked Contact Financial Institution To Unblock")
                            break

        self.another_transaction()


    def BlockCard(self):
        print("Card Blocked")
        self.another_transaction()

    def allow(self):
        atm = filemark()

        print("1.Procced          2.Cancel")  
        self.authorize = input()
        print("Please Wait...")
        
        if self.authorize:
            if self.authorize == "1":
                if self.enter_pin == self.card_pin:
                    self.balance -= int(self.amounts[int(self.amount)])
                    print("Transaction Sucessful")

                else:
                    print("Incorrect pin")
                    chances = 2

                    while chances <= 2:
                        self.enter_pin = atm.enter_pin()
                        if self.enter_pin == self.card_pin:
                            self.balance -= int(self.amounts[int(self.amount)])
                            print("Transaction Sucessful")
                            break

                        elif self.enter_pin!= self.card_pin:
                            print("Incorrect Pin")
                            chances -= 1
                            if chances == 0:
                                print("Card Blocked Contact Financial Institution To Unblock")
                                break

            elif self.authorize == "2":
                print("Transaction Canceled")

            else:
                self.allow()

    def another_transaction(self):
        print("Perform Another Transaction: ")
        print("")
        print("1.Yes         2.No")
        self.ano_tran = input()

        if self.ano_tran:
            if self.ano_tran == "1":
                self.HomeScreen()

            elif self.ano_tran == "2":
                print("Please Take Your Card")
                time.sleep(2)
                self.__init__()

            else: self.another_transaction()

activate = Atm()

        


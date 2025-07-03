class Account:
    def __init__(self,account_number,account_name,id_number,account_type,initial_balance=0):
         self.account_number=Bank.last_account_number
         self.account_name=account_name
         self.id_number=id_number               
         self.account_type=account_type
         self.initial_balance=initial_balance
         
class Bank:
     last_account_number=0

     def __init__(self):
        self.accounts = {}


     def create_account(self, account_name, id_number, account_type, initial_balance=0):
        Bank.last_account_number += 1
        acc_num = f"{Bank.last_account_number:05d}"
        account = Account(acc_num, account_name, id_number, account_type, initial_balance)
        self.accounts[acc_num] = account
        print(f"Account created successfully! Your account number is: {acc_num}")
        print("Do you want to continue or exit? (y/n)")
        choice1 = input().strip().lower()
        if choice1 == 'y':   
            self.options()  
        elif choice1 == 'n':
            print("Thank you for using our services. Have a great day!")
        return acc_num


     def deposit(self, acc_num, amount):
      if acc_num in self.accounts:
        account = self.accounts[acc_num]
        if amount > 0:
            account.initial_balance += amount
            print(f"Rs.{amount} deposited successfully.\nNew balance: Rs.{account.initial_balance}")
            print("Do you want to continue or exit? (y/n)")
            choice1 = input().strip().lower()
            if choice1 == 'y':
                self.options()
            elif choice1 == 'n':
                print("Thank you for using our services. Have a great day!")
        else:
            print("Invalid deposit amount. Please enter a positive number.")
            print("Do you want to continue or exit? (y/n)")
            choice1 = input().strip().lower()
            if choice1 == 'y':
                self.options()
            elif choice1 == 'n':
                print("Thank you for using our services. Have a great day!")
      else:
        print("Account not found.")


     def withdraw(self, acc_num, amount):
      if acc_num in self.accounts:
        account = self.accounts[acc_num]
        if amount > 0:
          if amount < account.initial_balance:
            account.initial_balance -= amount
            print(f"Rs.{amount} withdrawn successfully.\nNew balance: Rs.{account.initial_balance}")
            print("Do you want to continue or exit? (y/n)")
            choice1 = input().strip().lower()
            if choice1 == 'y':
                self.options()
            elif choice1 == 'n':
                print("Thank you for using our services. Have a great day!")
          else:
            print("Insufficient balance for withdrawal.")
            print("Do you want to continue or exit? (y/n)")
            choice1 = input().strip().lower()
            if choice1 == 'y':
                self.options()
            elif choice1 == 'n':
                print("Thank you for using our services. Have a great day!")
        else:
            print("Invalid deposit amount. Please enter a positive number.")
            print("Do you want to continue or exit? (y/n)")
            choice1 = input().strip().lower()
            if choice1 == 'y':
                self.options()
            elif choice1 == 'n':
                print("Thank you for using our services. Have a great day!")
      else:
        print("Account not found.")


     def getbalance(self, acc_num):
        if acc_num in self.accounts:
            account = self.accounts[acc_num]
            print(f"Your current balance is: Rs.{account.initial_balance}")
            print("Do you want to continue or exit? (y/n)")
            choice1 = input().strip().lower()
            if choice1 == 'y':
                self.options()
            elif choice1 == 'n':
                print("Thank you for using our services. Have a great day!")
        else:
            print("Account not found.")
            print("Do you want to continue or exit? (y/n)")
            choice1 = input().strip().lower()
            if choice1 == 'y':
                self.options()
            elif choice1 == 'n':
                print("Thank you for using our services. Have a great day!")


     def feeSubmit(self, acc_num, amount):
        z = input("Select school name:\n1-Edify Science Model High School\n2-The Educators\n3-Rifaa Public School\n4-Effa School\n5-Dar-e-Arqam School\n6-Islamic Public School\n7-Punjab College\n8-Aspire College\n9-Superior College\n10-Roots International School\n11-Roots International College\n12-Roots International University\nInput corresponding school number here:")
        if acc_num in self.accounts:
            account = self.accounts[acc_num]
            if amount > 0:
                account.initial_balance -= amount
                print(f"Fee of Rs.{amount} submitted successfully.\nNew balance: Rs.{account.initial_balance}")
                print("Do you want to continue or exit? (y/n)")
                choice1 = input().strip().lower()
                if choice1 == 'y':
                    self.options()
                elif choice1 == 'n':
                    print("Thank you for using our services. Have a great day!")
            else:
                print("Invalid fee amount. Please enter a positive number.")
                print("Do you want to continue or exit? (y/n)")
                choice1 = input().strip().lower()
                if choice1 == 'y':
                    self.options()
                elif choice1 == 'n':
                    print("Thank you for using our services. Have a great day!")
        else:
            print("Account not found.")
            print("Do you want to continue or exit? (y/n)")
            choice1 = input().strip().lower()
            if choice1 == 'y':
                self.options()
            elif choice1 == 'n':
                print("Thank you for using our services. Have a great day!")


     def billSubmit(self, acc_num, amount):
        z = input("Select which service you want to pay for?\n1-Electricity\n2-Gas\nInput corresponding school number here:")
        if acc_num in self.accounts:
            account = self.accounts[acc_num]
            if amount > 0:
                account.initial_balance -= amount
                print(f"Fee of Rs.{amount} submitted successfully.\nNew balance: Rs.{account.initial_balance}")
                print("Do you want to continue or exit? (y/n)")
                choice1 = input().strip().lower()
                if choice1 == 'y':
                    self.options()
                elif choice1 == 'n':
                    print("Thank you for using our services. Have a great day!")
            else:
                print("Invalid fee amount. Please enter a positive number.")
                print("Do you want to continue or exit? (y/n)")
                choice1 = input().strip().lower()
                if choice1 == 'y':
                    self.options()
                elif choice1 == 'n':
                    print("Thank you for using our services. Have a great day!")
        else:
            print("Account not found.")
            print("Do you want to continue or exit? (y/n)")
            choice1 = input().strip().lower()
            if choice1 == 'y':
                self.options()
            elif choice1 == 'n':
                print("Thank you for using our services. Have a great day!")
        

     def amountTransfer(self, acc_num, amount):
         if acc_num in self.accounts:
           account=self.accounts[acc_num]
           recipient_account_number=input("Enter recipient account number:")
           if recipient_account_number in self.accounts:
                receipient_account = self.accounts[recipient_account_number]
                if amount > 0 and amount <= account.initial_balance:
                     account.initial_balance -= amount
                     receipient_account.initial_balance += amount
                     print(f"Rs.{amount} transferred successfully to account {recipient_account_number}.\nYour new balance: Rs.{account.initial_balance}")
                     print("Do you want to continue or exit? (y/n)")
                     choice1 = input().strip().lower()
                     if choice1 == 'y':
                          self.options()
                     elif choice1 == 'n':
                          print("Thank you for using our services. Have a great day!")
                else:
                     print("Invalid transfer amount or insufficient balance.")
                     print("Do you want to continue or exit? (y/n)")
                     choice1 = input().strip().lower()
                     if choice1 == 'y':
                          self.options()
                     elif choice1 == 'n':
                          print("Thank you for using our services. Have a great day!")

     def close_account(self, acc_num):
            if acc_num in self.accounts:
                del self.accounts[acc_num]
                print(f"Account {acc_num} closed successfully.")
                print("Do you want to continue or exit? (y/n)")
                choice1 = input().strip().lower()
                if choice1 == 'y':
                    self.options()
                elif choice1 == 'n':
                    print("Thank you for using our services. Have a great day!")
            else:
                print("Account not found.")
                print("Do you want to continue or exit? (y/n)")
                choice1 = input().strip().lower()
                if choice1 == 'y':
                    self.options()
                elif choice1 == 'n':
                    print("Thank you for using our services. Have a great day!")   



     def options(self):
       print("Welcome to My e-bank:\nWhat service would you like to do?\n1-Create Account\n2-Deposit Cash\n3-Withdraw Cash\n4-Fee Submit\n5-Bill Submit\n6-Amount Transfer\n7-Balance Check\n8-Account Close\nInput corresponding service number here:")
       x=int(input())
       if(x>0 and x<9):
        if(x==1):
            print("You want to Create Account with us. Thank you for trusting our services.\n Creating Acoount for you.Please input required things:/n")
            account_name=(input("Enter your name:"))
            id_number=int(input("Enter your ID number:"))
            account_type=input("Enter account type you want:\n1-Savings Account\n2-Current Account\nInput corresponding account type number here:")
            if account_type == '1':
                account_type = "Saving Account"
                print("Please deposit minimum Rs.1000/- to open a Savings Account.")
                #call credit function here
                initial_balance=1000
                print("Account created successfully with a Savings Account type.Your initial balance is Rs. 1000/-")
            elif account_type == '2':
                initial_balance=0
                print("Account created successfully with a Current Account type.Your initial balance is Rs. 0/-")
            else:
                print("Invalid Type Selected.")
                return
            self.create_account(account_name,id_number,account_type,initial_balance)
        elif(x==2):
            print("Deposit Cash")
            acc_num = input("Enter your account number: ")
            amount = int(input("Enter amount to deposit: "))
            self.deposit(acc_num,amount)
        elif(x==3):
            print("Withdraw Cash")
            # Implement withdraw logic here
            acc_num = input("Enter your account number: ")
            amount = int(input("Enter amount to withdraw: "))
            self.withdraw(acc_num,amount)
        elif(x==4):
            print("Fee Submit")
            acc_num = input("Enter your account number: ")
            amount = int(input("Enter amount to submit fee: "))
            self.feeSubmit(acc_num,amount)
            # Implement fee submit logic here
        elif(x==5):
            print("Bill Submit")
            acc_num = input("Enter your account number: ")
            amount = int(input("Enter amount to submit bill: "))
            self.billSubmit(acc_num,amount)
            # Implement bill submit logic here
        elif(x==6):
            print("Amount Transfer")
            acc_num = input("Enter your account number: ")
            amount = int(input("Enter amount to transfer: "))
            self.amountTransfer(acc_num,amount)
            # Implement amount transfer logic here
        elif(x==7):
            print("Balance Check")
            acc_num = input("Enter your account number: ")
            self.getbalance(acc_num)
        elif(x==8):
            print("Account Close")
            acc_num = input("Enter your account number: ")
            self.close_account(acc_num)
            # Implement account close logic here        
       else:
         print("Invalid Option Selected. Please try again.")

b1=Bank()
b1.options()
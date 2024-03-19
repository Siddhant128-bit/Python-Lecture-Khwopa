class Bank_Account:
    def __init__(self,user_name,pass_word,balance):
        self.name=user_name
        self.password=pass_word
        self.balance=balance
    
    def withdraw(self,amount):
        # self.balance=self.balance-amount
        self.balance-=amount
    
    def deposit(self,amount):
        self.balance+=amount
    

#Task 1 loop over N times (N provided by user) create N objects put it in a list 
#Task 2 take username and password from user check which object it belongs to 
#Task 3 display all information of that user
#Task 4 take username of person who you want to send money
#Task 5 find the object with that username and deposit the requried amount
#Task 6 withdraw amount from your object and deposit to target object.
        

import getpass
total_accounts=[]
for i in range(2):
    user_name=input('Enter username:')
    password=getpass.getpass('Enter password: ')
    balance=float(input('Enter bank balance: '))
    total_accounts.append(Bank_Account(user_name,password,balance))

print(total_accounts)
print(total_accounts[0])

# object_1=Bank_Account('Siddhant Sharma','password',float('500000000'))
# print(object_1.name,object_1.password,object_1.balance)


# object_2=Bank_Account('Prashant Ghimire','password',float('00000'))
# print('Before Withdraw: ')
# print(object_2.name,object_2.password,object_2.balance)

# object_2.withdraw(400)
# print('After withdraw: ')
# print(object_2.name,object_2.password,object_2.balance)



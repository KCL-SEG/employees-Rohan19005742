#"""Employee pay calculator."""
#"""ENTER YOUR SOLUTION HERE!"""

import re

class Employee:
    def __init__(self, name, contractType, hours, pay, commissionType, bonous, numberOfContractsLanded):
        self.name = name
        self.contractType = contractType
        self.hours = hours
        self.pay = pay
        self.totalPay = pay
        self.commissionType = commissionType
        self.bonous = bonous
        self.totalBonous = bonous
        self.numberOfContarctsLanded = numberOfContractsLanded
        self.set_pay()

    def set_pay(self):
        if (self.contractType == "hourly"):
            self.totalPay *= int(self.hours)
        if (self.commissionType == "variable"):
            self.totalBonous *= int(self.numberOfContarctsLanded)
        else:
          self.bonous +=0
        #self.pay = str(int(self.pay) + int(self.bonous))

    def get_pay(self):
        pay = 0
        if (self.contractType == "hourly"):
            pay += int(self.totalPay)
        else:
            pay += int(self.pay)
        if (self.commissionType == "variable"):
            pay += int(self.totalBonous)
        else:
            pay += int(self.bonous)
        return int(pay)
    def __str__(self):
        answer = self.name
        if(self.contractType == "monthly"):
            answer += " works on a monthly salary of " + str(self.pay)
        elif (self.contractType == "hourly"):
            answer += " works on a contract of " + str(self.hours) + " hours at " + str(int(self.totalPay/self.hours)) +"/hour"
        if(self.commissionType == "variable"):
            answer += " and receives a commission for " + str(self.numberOfContarctsLanded) + " contract(s) at " + str(self.bonous) + "/contract"
        elif(self.commissionType == "fixed"):
            answer += " and receives a bonus commission of " + str(self.bonous)
        answer += ".  Their total pay is " + str(self.get_pay()) + "."
        return answer
        
import re
# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie','monthly','-1','4000',"none",0,0)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie','hourly',100,25,'none',0,0)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee','monthly',-1,3000,'variable',200,4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan','hourly',150,25,'variable',220,3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie','monthly',-1,2000,"fixed",1500,0)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel','hourly',120,30,'fixed',600,0)
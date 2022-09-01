
#HGS System
class Counter:
    totalMoney=0
    dailyReport=[]
    def report(self,vehicle):
        v=[vehicle.hgs,type(vehicle).__name__,vehicle.ownerName,vehicle.ownerSurname,vehicle.balance,vehicle.passDate,vehicle.passTime,vehicle.paid]
        self.dailyReport.append(v)
    def getPay(self,vehicle):
        if vehicle.balance < vehicle.payment:
            print("Insufficent Balance!")
            self.report(vehicle)
            return
        self.totalMoney+=vehicle.payment
        vehicle.balance-=vehicle.payment
        vehicle.paid="Paid"
        self.report(vehicle)


class Class1:
    payment=50
    paid="Not Paid"
    def __init__(self,hgs,ownerName,ownerSurname,balance,passTime,passDate):
        self.hgs=hgs
        self.ownerName=ownerName
        self.ownerSurname=ownerSurname
        self.balance=balance
        self.passTime=passTime
        self.passDate=passDate


class Class2(Class1):#Only difference between vehicle classes are the amount they must pay, so we do not have to initialize the features in every class
    payment=100

class Class3(Class1):
    payment=200

class Administration:#To get report from a counter, add it to constructor while initializing administration
    balance=0
    report=[]
    def __init__(self,counter):
        self.balance=counter.totalMoney
        self.report=counter.dailyReport
    def printTotal(self):
        print(f"Total amount of money collected is {self.balance}.")

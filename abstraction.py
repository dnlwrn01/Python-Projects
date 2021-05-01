
#import abc mod
from abc import ABC, abstractmethod

#parent class
class payment(ABC):
    def saleTotal(self, total):
        print(f"Item Cost: {total}")

    #abstract method
    @abstractmethod
    def calcTotal (self, total):
        pass

#calculate and print
class taxCalc(payment):
    def calcTotal (self, total):
        tax = (total * .055) #clac tax
        salePrice = round(total + tax, 2) #round total to hundreths place
        print(f"Tax: {tax}")
        print(f'Your total is {salePrice} today. ')

#set var values
obj = taxCalc()
obj.saleTotal(5.00)
obj.calcTotal(5.00)


        
    
        

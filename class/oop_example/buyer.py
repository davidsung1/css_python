from person import Person
from retailer import Retailer

class Buyer(Person):
    def __init__(self, name, age, money, product = 0):
        super().__init__(name, age, money)
        self.product = product
        
    def buy(self, other, how_many):
        total = how_many * Retailer.price
        
        if self.money >= total:
            self.product += how_many
            other.product -= how_many
            
            self.give_money(other, total)
        else:
            print("No money. Cannot buy that much")
            
    def __str__(self):
        return super().__str__() + '''
I am a buyer.
I have {} products.
'''.format(self.product)

    
if __name__ == "__main__":
    b1 = Buyer("Yang", 18, 10000)
    r1 = Retailer("Kim", 20, 3000, 20)
    print(b1)
    print(r1)
    b1.buy(r1, 11)
    print(b1)
    print(r1)
    
    
    
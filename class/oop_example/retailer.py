from person import Person

class Retailer(Person):
    price = 1000
    
    def __init__(self, name, age, money, product):
        super().__init__(name, age, money)
        self.product = product
        
    def sell(self, other, how_many):
        total = self.price * how_many
        
        if self.product >= how_many:
            self.product -= how_many
            other.product += how_many
          
            other.give_money(self, total)
        else:
            print("Product is not available")
            
    def __str__(self): 
        return super().__str__() + '''
I am a retailer.
I have {} products left.
'''.format(self.product)
    
if __name__ == "__main__":
    r1 = Retailer("Yang", 20, 5000, 20)
    b1 = Person("Kim", 24, 10000)
    print(r1)
    print(b1)
    r1.sell(b1, 3)
    print(r1)
    print(b1)
    
    
        

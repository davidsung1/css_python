from retailer import Retailer
from buyer import Buyer

r1 = Retailer("Yang", 20, 5000, 20)
b1 = Buyer("Kim", 18, 10000)

print(r1)
print(b1)

print("Kim is going to buy 5 products")

r1.sell(b1, 5)

print(r1)
print(b1)

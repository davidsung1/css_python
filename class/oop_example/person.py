
# coding: utf-8

# In[2]:

# 공통 속성(상인과 소비자 사이의)을 person에 넣음
class Person:
    def __init__(self, name, age, money):
        self.name = name
        self.age = age
        self.money = money
        
    def give_money(self, other, how_much):
        if self.money >= how_much:
            self.money -= how_much
            other.money += how_much
        else:
            print("I do not have money. Can't give you")
            
        
    def __str__(self):
        return '''
my name is {}
I am {} years old
I have {} won.'''.format(self.name, self.age, self.money)
    
if __name__ == "__main__": 
    p1 = Person("Greg", 18, 5000)
    p2 = Person("Kim", 22, 1000)
    print(p1)
    print(p2)
    p1.give_money(p2, 2000)
    print(p1)
    print(p2)







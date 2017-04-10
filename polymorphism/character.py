# abstract class란?
# 객체를 만들 수 없는 클래스
# 기본 클래스 즉 부모 클래스 역할을 함

from abc import * #abc = abstract base class, * = 

class Character(metaclass = ABCMeta):
    def __init__(self):
        self.hp = 100
        self.attack_power = 20
        
    def attack(self, other, attack_kind):
        other.get_damage(self.attack_power, attack_kind)
        
    @abstractmethod
    def get_damage(self, attack_power, attack_kind):
        pass

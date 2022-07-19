class Player:
    def __init__(self) -> None:
        self.control함수 = '어떠한 기능'
        self.hp = 10

    def control_기능(self):
        pass
    
    def hit_damage(self):
        self.hp -= 1

    def die(self):
        print('죽었다')


class Tanker(Player):
    def __init__(self) -> None:
        super().__init__()
        self.hp = 300
    
    def hit_damage(self):
        super().hit_damage() # == Player().hit_damage()  _> hp -= 1
        super().hit_damage() # == Player().hit_damage()  _> hp -= 1
        self.hp -= 5
    
    def dontmichi(self):
        print('안밀쳐진다')


class lainheart(Tanker):
    def __init__(self) -> None:
        super().__init__()
        self.hp = 1000

    def dontmichi(self):
        print('밀쳐지지않는다')


class jari(Tanker):
    def __init__(self) -> None:
        super().__init__()
        self.hp = 400
    
    def dontmichi(self):
        print('밀쳐질지도?')
    
class hitter(Player):
    pass

a = jari()
print(a.hp)
a.dontmichi()
print(a.hp)


#테트리스 블록
#어떤 2차원 배열 연산 제가 하겠습니다
#pygame 다뤄 보면 뭐 재미있을지도
block_data = [(1,3), (2,2)]
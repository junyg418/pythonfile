class First:
    def __init__(self) -> None:
        self.a = 12
        self.s = 13

class A_1(First):
    def __init__(self) -> None:
        super().__init__()
        self.a = 16
    
    def print(self):
        print(self.a)

class A_2(First):
    def __init__(self) -> None:
        First.__init__(self)
        # First().__init__() 이것 아님

class A_3(First):
    def __init__(self) -> None:
        self.a = None
    


print(A_2().a)
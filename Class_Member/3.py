class Cs:
    count = 0       #class안쪽 & method 밖에 변수 정의하면 class변수
    def __init__(self):
        Cs.count = Cs.count +1
    @classmethod
    def getCount(cls):
        # print(cls)
        return Cs.count

i1 = Cs()
i2 = Cs()
i3 = Cs()
i4 = Cs()
print(Cs.getCount())

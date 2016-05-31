class C(object):            # object 유무는 관계 없음 (추후 상속에서 논의)
    def __init__(self, v):
        self.value = v
    def show(self):
        print(self.value)
    def getValue(self):
        return self.value
    def setValue(self,v):
        self.value = v

c1 = C(10)
print(c1.getValue())

c1.setValue(20)
print(c1.getValue())

class C(object):            # object 유무는 관계 없음 (추후 상속에서 논의)
    def __init__(self, v):
        self.value = v
    def show(self):
        print(self.value)

c1 = C(10)
print(c1.value)

c1.value = 20
print(c1.value)

c1.show()

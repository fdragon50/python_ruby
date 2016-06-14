class C1:
    def m(self):
        return 'parent'

class C2(C1):
    def m(self):
        return super().m() + ' child'
    pass        # 비어있는 클래스이니 안심하고 실행시켜도돼.. 라고 파이썬에 알려주는 것

o = C2()
print(o.m())

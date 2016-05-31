class Cal(object):
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2
    def add(self):
        return self.v1 + self.v2
    def subtract(self):
        return self.v1 - self.v2

# 생성자 constructor
# class가 instance화 될때..
# 실행되기로 약속되어있는 메소드(like 컴퓨터부팅, 자동차시동)
# 파이선의 메소드들은 첫번째 매개변수를 반드시 정의해야함
# 그 첫번째 매개변수는 언제나... 그 인스턴스가 됨
#
# 두번째 매개변수는 우리가 전달하기로 한...
# 첫번째 매개변수를 이용해서 변수를 지정할 수 있음
#

c1 = Cal(10,10)
print(c1.add())
print(c1.subtract())

c2 = Cal(30,20)
print(c2.add())
print(c2.subtract())

# Self가 instance를 의미함
# Python method들은 첫번째 매개변수 지정이 필수임 (이름관계없음)
# 1st매개변수 = method가 포함되어 있는 instance가 되도록 약속되어있음
#                > instance에 접근할 수 있게됨
#                > 1st 매개변수를 ㅣ용하여 instance에 소속되는 변수를 지정할수 있게됨

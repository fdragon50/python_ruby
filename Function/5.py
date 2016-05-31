# input_id = input("아이디를 입력해주세요!\n")
# members=['egoing','k8805']
# for member in members:
#     if member == input_id:
#         print('Hello!, '+member)
#         import sys
#         sys.exit()
# print('Who are you?')



input_id = input("아이디를 입력해주세요!\n")

def login(_id):
    members=['egoing', 'k8805', 'leezche','fdragon50']
    for member in members:
        if member == _id:
            return True
    return False

if login(input_id):
    print('Hello, '+input_id)
else:
    print('Who are you?')

# print('aaa')
# 함수는 앞에이름이 온다.       print
# 이름 뒤에는 괄호가 온다       ()
# 괄호 안에는 입력값이 온다     'aaa'
# 함수의 정의는 def 로.
# 1000줄 코드를 3번 실행한다는 가정시...    3번 함수로 끝낼수..

# 리턴
# 1.함수의 결과값으로 만든다
# 2.리턴이 등장하면 함수를 종료한다
#  > 함수는 리턴값을 알기위함 임으로.  이후 작업은 진행이 불필요함
# 코드는 상황에 따라 적합할수도.. 그렇지 않을수도 있다..  ex) 사거리..  시골길..  10차선 도로

# name = 'egoing'   #문자열 객체
# names = ['egoing','k8805']    #배열 객체
name1 = String.new('egoing')
name2 = String.new('k8805')
puts(name1.reverse())   #name1에 속해있는 리버스 함수를 실행시킨 것
puts(name2.reverse())
puts(name1.upcase())
puts(name1.size())
# ---------------------------------------
names=Array.new() # 배열 클래스에 대한 인스턴스 만들어서 네임스에 담김
                  # names는 Array에 대한 인스턴스임
names.push('egoing') # 어레이 인스턴스에 푸시라는 메소드 호출해서. 이고잉을 담음
                    # Array 인스턴스 안의 push method 호출naes인스턴스 안에
                    #  네임 인스턴스 변수 안에 이고잉이라는 데이터를 추가
names.push('k8805')
puts(names)
puts(names.join('-'))

# name1 변수가 가리키는 egoing 데이터
# name1 인스턴스에 reverse 함수를 실행시키면
# name1 값을 뒤집은값을 리버스함수가 리턴해주는것
# (name1 값을 리버스함수가 뒤집은 값을 리턴해주는것)

# name2는 k8805 리버스 함수를 호출하면 뒤집은 값을 리턴해줌

# 연관되어있는 데이터와 연관되어있는 함수를 담고있다.
# reverse 는 문자와 연관.. String에 포함되어 있음

# 함수는 객체 안에서 사용될때 method라는 이름으로 불리움
# method = function = 함수

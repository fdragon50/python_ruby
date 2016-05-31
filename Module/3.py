#import egoing, k8805
from egoing import a as z   #a 함수를 egoing으로부터 가져왔기 때문에 이후 모듈 함수 실행시 egoing은제외해야 함
import k8805 as k
#print(a())          #egoin.a()로 하면 오류.   from / import 했기 때문에.
#print(k8805.a())
print(z())      # egoing 모듈에서 a 함수를 가져왔기 때문에 모듈명 명기 하지 않음
print(k.a())    # 모듈만을 k로 가져왔기 때문에 모듈및 함수명 명기

#상호 수정작업시 오류 방지를 위해 이름을 추가하거나
#뒤에 번호를 붙여 이름을 바꾸는 방법을 검토

#from 화일/모듈이름 import 함수.
#import로 가져오는 것은 모듈 일수도. 함수일수도 있다

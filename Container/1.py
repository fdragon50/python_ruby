# 컨테이너: (포괄적인 표현. 파이썬은 리스트,  루비는 어레이(배열))
# 	변수는 하나의 값을 담을 수 있는 그릇
# 	하나의 그릇에 여려개의 값을 담을 수 있는 방법? >>  컨테이너를 사용
# 	컨테이너를 변수에 담으면... 변수를 통해 컨테이너에 접근 할 수 있음


print(type('fdragon50'))    #str
name = 'fdragon50'
print(name)

print(type(['fdragon50','79zzong','HJ']))   #list
names = ['fdragon50','79zzong','HJ',12]
print(names)

# index: 각각의 데이터들이 저장될때 식별번호가 있음.  0 1 2 3 순서
# 각각은 원소 /  element  라고 하며  각각의 식별번호가 index(색인)임.
# index에는 복합적인 형태 입력 가능

print(names[3])


fdragon50 = ["programmer",'seoul','male',30]
fdragon50[1]='inchoen'      # 컨테이너 내용 변경
print(fdragon50)


# 컨테이너 > list, array > index > element
# element가 index로 식별되며, list라는 이름의 형태로 컨테이너에 담긴다

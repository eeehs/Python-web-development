# 1. map 함수
# - 사용 이유
# 기존 리스트를 수정해서 새로운 리스트를 만들 때 

# - 사용방법
# map(함수, 순서가 있는 자료형)

print(list(map(int, ['3','4','5','6'])))

# - 예제
# 리스트 모든 요소의 공백 제거

items = [' 로지텍마우스 ',' 앱솔키보드 ']

# 1) for 사용
for i in range(len(items)):
	items[i] = items[i].strip()

# 2) map 사용했을 때 
def strip_all(x):
	return x.strip()
items = [' 로지텍마우스 ',' 앱솔키보드 ']
items = list(map(strip_all,items))

# 3) 람다와 map을 같이 사용했을 때 

items = [' 로지텍마우스 ',' 앱솔키보드 ']
items = list(map(lambda x:x.strip(),items))

# 2. filter 함수
# - 사용 이유
# 기존 리스트에서 조건을 만족하는 요소만 뽑고 싶을 때

# - 사용방법 
# filter(함수, 순서가 있는 자료형)

def func(x):
	return x < 0
filter(func,[-3,-2,0,5,7])

# - 예제
# 리스트에서 길이가 3이하인 문자들만 필터링

# 1) for 사용
animals = ['cat','tiger','dog','bird','monkey']
result = []
for i in animals:
	if len(i) <=3:
		result.append(i)

# 2) filter 사용

def word_check(x):
	return len(x) <= 3
result = list(filter(word_check,animals))

# 3) 람다와 filter를 같이 사용했을 때

result = list(filter(lambda x:len(x) <= 3,animals))

# 1. 위치 매개변수
# 가장 기본적인 매개변수 

# 함수 정의
def my_func(a,b):
	print(a,b)

# 함수 호출
my_func(1,2)

# 2. 기본 매개변수
# 매개변수의 기본값을 지정할 수 있다. 

# 함수 정의
def post_info(title, content='내용없음'):
	print('제목: ',title)
	print('내용: ',content)
# 함수 호출
post_info('출석합니다!')

# 3. 키워드 매개변수
# 함수 호출 시에 키워드를 붙혀서 호출
# 매개변수의 순서를 지키지 않아도 됩니다. 

# 함수 정의
def post_info(title,content):
	print('제목: ',title)
	print('내용: ',content)

# 함수 호출
post_info(content='없어요',title='여자친구 만드는방법')

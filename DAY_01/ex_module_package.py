# 모듈과 패키지
# - 관계
#   * 모  듈 : 특정 기능/목적의 변수, 함수, 클래스를 저장한 하나의 파이썬 파일
#   * 패키지 : 특정 기능/목적의 모듈들을 담고 있는 단위
# - 문법 : import 모듈명
#         import 패키지명.모듈명

# 사용할 모듈 로딩
import math                         # 내장 모듈, math 모듈 내 모든 변수, 함수, 클래스 다 사용
import math as m                    # 모듈명에 별칭/별명 지정
from math import factorial          # 모듈 내에서 factorial 함수만 사용
from math import factorial as fac   # 모듈 내에서 factorial 함수의 별칭

def factorial(x):
    print(f'{x}!')

# 모듈 내의 요소(변수, 함수, 클래스) 사용 방법
# => 모듈명.변수
# => 모듈명.함수()
print(math.pi, math.pow(2, 3))
print(m.pi, m.pow(2, 3))

# 모듈 내의 함수 1개를 직접 import한 경우 바로 사용 가능
print(factorial(4))
print(fac(4))
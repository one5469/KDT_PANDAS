# 자동차 클래스
# 클래스이름 : Car
# 클래스속성 : 바퀴, 색상, 엔진, 차번호, 차종류(인스턴스 속성), 제조사(클래스속성)
# 자동차기능 : 주행, 정지, 후진

class Car:
    # 클래스 속성
    maker = '현대'

    # 생성자 메소드 => 객체 즉, 인스턴스 생성 메소드
    def __init__(self, wheel, color, number, kind):
        # 힙 영역에 저장
        self.wheel = wheel
        self.color = color
        self.number = number
        self.kind = kind

    # 객체 즉, 카 인스턴스 메소드
    def driving(self, where):
        print(f'{where}에 {self.number} 차가 가고 있다.')

    def stop(self, place):
        print(f'{self.number} 차가 {place}에 정지한다.')

    def back(self):
        print(f'{self.number} 차가 후진한다.')


# 자동차 인스턴스 생성
myCar = Car(19, 'red', '1111', '새단')
secondCar = Car(20, 'hotpink', '7777', 'SUV')


# 계산기 클래스
# 클래스이름 : Calc
# 클래스속성 : 브랜드, 종류, 색깔, 크기, 가격
# 클래스기능 : 덧셈, 뺄셈, 곱셈, 나눗셈
# - 데이터 : 속성 또는 기능에서 매개변수

class Calc:
    # 클래스 변수
    maker = '카시오'
    __size = (7,15)    # 비공개 속성 __속성명 : 클래스 밖에서 속성 읽거나 쓰기 불가

    # 객체 즉 인스턴스 생성 메소드
    def __init__(self, kind, color, price, info):
        self.kind = kind
        self.color = color
        self.price = price
        self.__info = info       # 인스턴스 생성 시 계산기에 각인되는 정보
        self.data = 0

    # 비공개 인스턴스 속성 읽기/쓰기(getter/setter) 메소드
    def getInfo(self):
        return self.__info

    def setInfo(self, info):
        self.__info = info

    # 비공개 인스턴스 속성 읽기/쓰기(getter/setter) 메소드
    # => 속성 읽기/쓰기 방식으로 동작하도록 설정
    @property
    def info(self):
        return self.__info

    @info.setter
    def info(self, info):
        self.__info=info

    # 덧셈 기능
    def plus(self, nums):
        self.data += nums

    def minus(self, nums):
        self.data -= nums

    def multi(self, nums):
        self.data *= nums

    def div(self, nums):
        if not nums: return '0으로 나눌 수 없습니다.'
        else: self.data += self.data/nums

    def result(self):
        return self.data


# Calc 클래스로 인스턴스 생성 => 힙에 생성 : 인스턴스 변수 + 클래스 변수
#                                      인스턴스 메소드 사용 가능

c1 = Calc('공학용', '블랙', 10000, '인포')

# 인스턴스 속성 읽기 = 공개 속성만 읽기 가능
print(c1.data, c1.color)

# 인스턴스 비공개 속성 읽기 ==> 전용 메소드 getter/setter 통해서 읽기/쓰기
print(c1.getInfo())
print(c1.info)

# 인스턴스 비공개 속성 변경 ==> 전용 메소드 getter/setter 통해서 읽기/쓰기
c1.setInfo('내꺼')
print(c1.getInfo())
c1.info = '니꺼'
print(c1.info)

# Calc 클래스로 계산기 정보 확인 => 클래스 변수만 확인 가능
#                               인스턴스 변수가 메소드 사용 불가능!!
#                               self 값이 없음!!
print(Calc.maker)

# 인스턴스 메소드에 접근 불가!!
# Calc.plus(nums=10)
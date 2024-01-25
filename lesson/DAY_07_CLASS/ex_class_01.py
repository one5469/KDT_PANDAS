# 사용자 정의 클래스

# 클래스정의 : 밤하늘의 별을 저장하는 데이터
# 클래스이름 : Star
# 클래스속성 : 크기, 색상, 밝기    => 속성(attribute), 필드(field) => 변수
# 클래스기능 : 반짝거린다, 떨어진다 => 함수(function), 메소드(method) => 함수
class Star:
    # 최상위 부모클래스 object로부터 상속받은 함수 즉 메소드
    # 형태 def __XXX__()
    # 나의 클래스에 맞도록 수정 즉 리모델링해서 사용 => 오버라이드(override)
    def __init__(self, size, color, brightness):
        print(f'__init__() : {size}, {color}, {brightness}')
        # 힙 메모리 영역에 저장 => 속성 데이터의 주소 저장
        self.size = size
        self.color = color
        self.brightness = brightness


# 객체 생성 => 클래스에 정의된 속성 즉 변수와 함수들이 메모리 힙 영역에 생성
# 생성 방법 => 클래스명(      ) 생성자 함수/메소드
#            클래스명(매개변수) 생성자 함수/메소드
#            클래스명(매개변수1, 매개변수2, ..., 매개변수n) 생성자 함수/메소드
myStar = Star(5, 'dark_yellow', 10)

# 객체의 속성 정보 읽기 => 객체변수명.속성명
print(myStar.color, myStar.brightness)

# 객체의 속성 정보 변경 => 객체변수명.속성명 = 새로운값
myStar.brightness = 7
print(myStar.color, myStar.brightness)

# 클래스정의 : 밤하늘의 별을 저장하는 데이터
# 클래스이름 : Star
# 클래스속성 : 크기, 색상, 밝기, 이름   => 속성(attribute), 필드(field) => 변수
# 클래스기능 : 반짝거린다, 떨어진다     => 함수(function), 메소드(method) => 함수
class Star:
    # 클래스 변수/속성/필드 => 해당 클래스 생성된 객체 즉 인스턴스가 공유하는 속성
    timezone = '밤'
    __privateValue = 77

    # 최상위 부모클래스 object로부터 상속받은 함수 즉 메소드
    # 형태 def __XXX__()
    # 나의 클래스에 맞도록 수정 즉 리모델링해서 사용 => 오버라이드(override)
    def __init__(self, size, color, brightness, name='알수없음'):
        print(f'__init__() : {size}, {color}, {brightness}, {name}')
        # 힙 메모리 영역에 저장 => 속성 데이터의 주소 저장
        self.__size = size
        self.color = color
        self.brightness = brightness
        self.name = name

    # 별 클래스의 기능 => 메소드
    def drop(self):
        print(f'{self.name} 별이 하늘에서 떨어집니다. 소원 빌어요~!')

    # 비공개 인스턴스 속성에 접근하기 위한 메소드
    # 비공개 인스턴스 속서 읽어오는 메소드 get속성명() ===> 속성값
    # 비공개 인스턴스 속성에 값 설정하는 메소드 set속성명(새로운값)
    def getSzie(self):
        return self.__size

    def setSize(self, size):
        self.__size = size

    # 비공개 인스턴스 메소드 => 클래스 내부에서만 호출되는 메소드
    def __inner(self):
        print("나는 비공개 인스턴스 메소드")

    # 객체 즉 인스턴스 생성 없이 사용하는 메소드
    @staticmethod
    def add():
        pass

    @classmethod
    def cc(cls):
        pass


# 객체의 메소드 실행 => 객체변수명.메소드명()
myStar = Star(5, 'dark_yellow', 10)
yourStar = Star(10, 'red', 20, 'Red Star')

myStar.drop()
yourStar.drop()

print(f'클래스명.__dict__ : {Star.__dict__}')
print(f'인스턴스명.__dict__ : {myStar.__dict__}')
print(f'인스턴스명.__dict__ : {yourStar.__dict__}')

# 인스턴스 속성에 간접 접근 => 메소드 제공 필수 getter/setter 메소드 ==> 개발자 선택사항
print('현재 속성값 읽기 : ', myStar.getSzie())
# 현재 비공개 속성값 변경
myStar.setSize(100)

print('현재 비공개 속성값 읽기 : ', myStar.getSzie())
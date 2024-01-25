# 2차원 점 클래스
# 클래스이름 : Print2D
# 클래스속성 : x, y, color, shape, size
# 클래스기능 : 그리기, 지우기, 정보출력

class Point2D:
    # 클래스 속성  => 없음

    # 객체 즉 인스턴스 생성
    def __init__(self, x, y, color, shape, size):
        print('Point2D')
        self.x = x
        self.y = y
        self.color = color
        self.shape = shape
        self.size = size

    def draw(self):
        print(f'좌표 ({self.x}, {self.y})에 {self.shape} 그리기')

    def printInfo(self):
        print(f'위치 : {self.x}, {self.y}')
        print(f'색상 : {self.color}')
        print(f'형태 : {self.shape}')

# 3차원 점 클래스
# 클래스이름 : Print3D
# 클래스속성 : x, y, z, color, shape, size
# 클래스기능 : 그리기, 지우기, 정보출력

class Point3D(Point2D):
    # 클래스 속성  => 없음

    # 객체 즉 인스턴스 생성
    def __init__(self, x, y, z, color, shape, size):
        print('Point3D')
        super().__init__(x, y, color, shape, size)
        self.z = z

    # 상속받은 부모의 메소드를 나의 취향에 맞게 수정 => 오버라이딩
    def printInfo(self):
        print('3D')
        print(f'위치 : {self.x}, {self.y}, {self.z}')
        print(f'색상 : {self.color}')
        print(f'형태 : {self.shape}')



p2 = Point2D(10, 10, 'red', 'circle', (10, 10))
p3 = Point3D(5, 5, 5, 'red', 'rectangle', (3, 3, 3))
print()

p2.printInfo()
p3.printInfo()

from ex_class_02 import Car

class selfDriveCar(Car):
    def __init__(self, wheel, color, number, kind):
        super().__init__(wheel, color, number, kind)

    def startSelfDrive(self, where):
        print(f'{where}(으)로 {self.number} 차가 자율주행을 시작한다.')

    def endSelfDrive(self, where):
        print(f'{where}(으)로 {self.number} 차가 자율주행을 종료한다.')

class FlyingCar(Car):
    def __init__(self, wheel, color, number, kind):
        super().__init__(wheel, color, number, kind)

    def flying(self, where):
        print(f'{where}(으)로 {self.number} 차가 이륙한다.')

    def landing(self, where):
        print(f'{where}(으)로 {self.number} 차가 착륙한다.')

class selfFlyingCar(selfDriveCar, FlyingCar):
    def __init__(self, wheel, color, number, kind):
        super().__init__(wheel, color, number, kind)

car1 = selfDriveCar(12, 'Red', '1234', 'SUV')
car2 = FlyingCar(12, 'Red', '4567', 'SUV')
car3 = selfFlyingCar(12, 'Red', '1234', 'SUV')


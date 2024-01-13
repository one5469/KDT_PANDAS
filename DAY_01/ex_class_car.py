# 자동차 관리 프로그램 만들기
# - 엔진, 연료, 브랜드, 색상, 번호
# - 전진, 후진, 좌회전, 우회전, 정지

# ??
# engine = '휘발유'
# food = '휘발유'
# maker = '현대'
# color = '흰색'
# number = '111가1111'
#
# def go(): print('전진')
# def back(): print('전진')
# def left_go(): print('좌회전')
# def right_go(): print('우회전')
# def stop(): print('정지')
#
# print(f'첫번째 판매 차량 [{number}')
# print(f'- 엔진 종류: {engine}')
# print(f'- 연료 종류: {food}')
# print(f'- 브랜드 종류: {maker}')
# print(f'- 색상: {color}')

# 자동차 클래스
# - 역할 : 자동차 관련 데이터와 기능을 모두 저장 관리하는 클래스
# - 문법
#   class 클래스명 :
#           코드
class Car:
    maker = '현대'
    # 클래스 생성 시 필수로 생성되는 메소드
    # 힙 메모리에 속성들의 값을 저장해주는 역할
    def __init__(self, engine, food, color, number):
        print('__init__')
        # 자동차 클래스가 가지는 속성 메모리 힙에 저장
        self.engine = 'engine'
        self.food = 'food'
        self.color = 'color'
        self.number = 'number'

    # 자동차 기능 => 함수형식
    def go(self):
        print(f'{self.number} 자동차 전진')

    def back(self):
        print(f'{self.number} 자동차 후진')

    def stop(self):
        print(f'{self.number} 자동차 정지')



# 클래스로 자동차 객체 생성
myCar = Car('휘발유', '휘발유', '흰색', '111가1111')
myCar2 = Car('휘발유', '휘발유', '핑크색', '111가7777')
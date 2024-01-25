DEBUG_NUM = int(input("Choose your solution : "))

# 연습문제: 리스트에 기능 추가하기
if DEBUG_NUM == 1:
    class AdvancedList(list):
        def replace(self, a, b):
            for i in self:
                if i == a:
                    self[self.index((i))] = b

    x = AdvancedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    x.replace(1, 100)
    print(x)


# 심사문제: 다중 상속 사용하기
if DEBUG_NUM == 2:
    class Animal:
        def eat(self):
            print('먹다')

    class Wing:
        def flap(self):
            print('파닥거리다')

    class Bird(Animal, Wing):
        def fly(self):
            print("날다")

    b = Bird()
    b.eat()
    b.flap()
    b.fly()
    print(issubclass(Bird, Animal))
    print(issubclass(Bird, Wing))
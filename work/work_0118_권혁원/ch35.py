DEBUG_NUM = int(input("Choose your solution : "))

# 연습문제: 날짜 클래스 만들기
if DEBUG_NUM == 1:
    class Date:
        def __init__(self):
            pass

        @staticmethod
        def is_date_valid(str):
            list = str.split('-')
            if len(list) != 3:
                return False
            else:
                for i in list:
                    if not i.isdecimal():
                        return False

            list = map(int, list)

            if list[1] > 12 or list[1] < 1:
                return False
            elif list[2] > 31 or list[2] < 1:
                return False
            else:
                return True

    if Date.is_date_valid('2000-10-31'):
        print('올바른 날짜 형식입니다.')
    else:
        print('잘못된 날짜 형식입니다.')

# 심사문제: 시간 클래스 만들기
if DEBUG_NUM == 2:
    class Time:
        def __init__(self, hour, minute, second):
            self.hour = hour
            self.minute = minute
            self.second = second

        def from_string(string):
            h, m ,s = string.split(':')
            return Time(h, m, s)

        @staticmethod
        def is_time_valid(string):
            str_list = string.split(':')

            if len(str_list) != 3:
                return False
            else:
                for i in str_list:
                    if not i.isdecimal():
                        return False

            hour, minute, second = map(int, str_list)

            if hour > 23 or hour < 0:
                return False
            elif minute > 60 or minute < 0:
                return False
            elif second > 60 or second < 0:
                return False
            else:
                return True

    time_string = input()

    if Time.is_time_valid(time_string):
        t = Time.from_string(time_string)
        print(t.hour, t.minute, t.second)
    else:
        print('잘못된 시간 형식입니다.')
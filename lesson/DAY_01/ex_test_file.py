# 입력받은 내용을 파일에 저장하는 프로그램
# - 조건 : 'X', 'x' 입력 시 입력 받기 중단
import time
from datetime import date, datetime

filename = 'test.txt'

today = date.today()
print(today.year, today.month, today.day)

today2 = datetime.today()
print(today2.year, today2.month, today2.day, today2.hour, today2.minute, today2.second)

print(today.strftime("%y/%m/%d"))

# 파일에 쓰기 즉 저장
# with open(filename, mode = 'a', encoding='utf8') as f:
#     while True:
#         data = input("메시지 입력 (종료-X, x) : ")
#
#         # 종료 검사
#         if data in ('X', 'x'):
#             print("종료합니다.")
#             break  # 즉시 종료로 while 문에서 아래 코드 실행 안됨
#
#         f.write(data + '\n')
#
#         time.sleep(1)
#
#     f.write(f'저장시간 : {time.ctime()}\n')

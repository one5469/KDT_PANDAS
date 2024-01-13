# 파일을 하나 선택 후 복사본 파일 생성 하기
# - 예) message.txt ===> message_copy.txt

filename = 'message.txt'

# with open(filename, 'r', encoding='utf-8') as f:
#     msg = f.read()

copyfile = 'message_copy.txt'

# with open(copyfile, 'w', encoding='utf-8') as f:
#     f.write(msg)

with open(filename, 'r', encoding='utf-8') as f:
    msg = f.read()
    with open(copyfile, 'w', encoding='utf-8') as f:
        f.write(msg)


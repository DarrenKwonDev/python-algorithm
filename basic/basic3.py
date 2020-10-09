a = int(input())

# 2, 8, 16 진수로 출력
print(a)
print(bin(a))
print(oct(a))
print(hex(a))

# 16진수 출력이지만 대, 소문자
print("{:x}".format(a))
print("{:X}".format(a))

# int 형변환 시에 2번째 인자로 진수롤 주어 진법 변환 가능
b = int(input(), 8)
print("{:}".format(b))


# ord는 아스키문자를 정수로 변환
# chr는 정수를 아스키 문자로 변환
ascii_char = input()
print(ord(a))
interger = int(input())
print(chr(a))

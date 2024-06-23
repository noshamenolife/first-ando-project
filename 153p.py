a = input("밑변의 길이를 입력해주세요: > ")
b = input("높이의 길이를 입력해주세요: > ")

fa = float(a)
fb = float(b)

r = (fa**2 + fb**2) ** (1/2)

print("빗 변의 길이는 ", r, "입니다.")
print(type(r))
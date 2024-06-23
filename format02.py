# 정수
output_a = "{:d}".format(52)

# 특정 칸에 출력
output_b = "{:5d}".format(52) # 5칸을 빈칸으로 잡고 뒤에서부터
output_c = "{:10d}".format(52) # 10칸

# 빈칸을 0으로 채우기
output_d = "{:05d}".format(52) # 양수
output_e = "{:05d}".format(-52) # 음수

print("output_a", output_a)
print("output_b", output_b)
print("output_c", output_c)
print("output_d", output_d)
print("output_e", output_e)
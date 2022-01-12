import itertools

문자열 = '012345689'  # 패스워드로 쓸 수 있는 숫자를 뜻함

# for i in 문자열:
#   for j in 문자열:
#      print(i, j)
# 두 자리

# for i in 문자열:
#   for j in 문자열:
#      for k in 문자열:
#         print(i, j, k)
# 세 자리

# 자동으로 할 수 있는 라이브러리가 itertools이므로 이를 사용하면

for 패스워드길이 in range(1, 5):
    for password in itertools.product(문자열, repeat=패스워드길이):
        # 앞의 for문과 같은 코드임
        # print(password)
        print(''.join(password))

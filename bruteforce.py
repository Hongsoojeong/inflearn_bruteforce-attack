#import itertools

import requests

로그인패킷={
    'id' : 'krystal',
    'pw' : '1234', #마지막에도 콤마 잊지말기
}


address = requests.post(f'http://127.0.0.1:8080/',data=로그인패킷) # local host
# 응답한 값이 들어간 address (response라는 변수로 보통 많이 씀)

#문자열 = '012345689'  # 패스워드로 쓸 수 있는 숫자를 뜻함

#for 패스워드길이 in range(1, 5):
#    for password in itertools.product(문자열, repeat=패스워드길이):
        # 앞의 for문과 같은 코드임
        # print(password)
#       print(''.join(password))


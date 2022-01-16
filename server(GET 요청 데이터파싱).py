from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse as parse

class ServerHandler(BaseHTTPRequestHandler):

    def do_GET(self):  # URL로 요청이 오는 경우
        self.send_response(200)  # 성공했다는 의미
        self.send_header('content-type', 'text/html')
        # 응답값으로 보내주는 것이 html
        self.end_headers()  # 헤더를 마무리
        
        f=open("C:/Users/my_yo/Desktop/inflearn_bruteforce-attack/index.html",'r') #index.html를 read모드로 읽는다.
        data=f.read() #data에 담은 후 file을 닫는다
        f.close()
        self.wfile.write(data.encode())


    def do_POST(self):
        self.send_response(200)  # 성공했다는 의미
        self.send_header('content-type', 'text/html')
        # 응답값으로 보내주는 것이 html
        self.end_headers()  # 헤더를 마무리
        print('post 요청이 들어왔습니다.')
        data=self.rfile.read(int(self.headers['Content-length']))
        if data is not None:  # post 패킷을 보낸것을 파싱해서 dict 형식으로 저장한다.
            data_decode=dict(parse.parse_qs(data.decode()))
            
        if data_decode['id']==['krystal'] and data_decode['pw']==['1234']:
            self.wfile.write('login success'.encode())
        else:
            f=open("C:/Users/my_yo/Desktop/inflearn_bruteforce-attack/index_fail.html",'r') #index.html를 read모드로 읽는다.
            data=f.read() #data에 담은 후 file을 닫는다
            f.close()
            self.wfile.write(data.encode())
            
        print(f'post params = {data_decode}')
        #post값으로 들어간 데이터가 제대로 들어갔는지 확인한다. 
        

PORT = 8080  # 8080포트로 서비스를 하겠다는 의미
server = HTTPServer(('', PORT), ServerHandler)
print(f'서버가 {PORT}로 서비스 되고 있습니다.')
server.serve_forever()
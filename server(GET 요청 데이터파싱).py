from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse as parse

class ServerHandler(BaseHTTPRequestHandler):

    def do_GET(self):  # URL로 요청이 오는 경우
        self.send_response(200)  # 성공했다는 의미
        self.send_header('content-type', 'text/html')
        # 응답값으로 보내주는 것이 html
        self.end_headers()  # 헤더를 마무리
        
        self.wfile.write('<p>hello world get</p>'.encode())
        print('get 요청이 들어왔습니다.')
        self.wfile.write(self.path.encode()) #우리가 입력한 URL을 볼 수 있음
        self.wfile.write('<br>'.encode())
        if '?' in self.path: #? 기준으로 나눠진다 
            self.wfile.write(str(self.path.split('?')[1].split('&')).encode())
            print(parse.parse_qsl(self.path.split('?')[1]))
            print(dict(parse.parse_qsl(self.path.split('?')[1])))
            #dic으로 감싸는 형태

    def do_POST(self):
        self.send_response(200)  # 성공했다는 의미
        self.send_header('content-type', 'text/html')
        # 응답값으로 보내주는 것이 html
        self.end_headers()  # 헤더를 마무리
        print('post 요청이 들어왔습니다.')
        self.wfile.write('<p>hello world post</p>'.encode())
        self.wfile.write(self.path.encode()) #우리가 입력한 URL을 볼 수 있음
        self.wfile.write('<br>'.encode())
        data=self.rfile.read(int(self.headers['Content-length']))
        if data is not None:  # post 패킷을 보낸것을 파싱해서 dict 형식으로 저장한다.
            data_decode=dict(parse.parse_qs(data.decode()))
        print(f'post params = {data_decode}')
        #post값으로 들어간 데이터가 제대로 들어갔는지 확인한다. 
        

PORT = 8080  # 8080포트로 서비스를 하겠다는 의미
server = HTTPServer(('', PORT), ServerHandler)
print(f'서버가 {PORT}로 서비스 되고 있습니다.')
server.serve_forever()
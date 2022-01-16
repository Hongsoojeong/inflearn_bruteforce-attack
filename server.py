#from http.server import HTTPServer, BaseHTTPRequestHandler


#class ServerHandler(BaseHTTPRequestHandler):

 #   def do_GET(self):  # URL로 요청이 오는 경우
  #      self.send_response(200)  # 성공했다는 의미
   #     self.send_header('content-type', 'text/html')
        # 응답값으로 보내주는 것이 html
    #    self.end_headers()  # 헤더를 마무리
     #   self.wfile.write('hello world'.encode())

#    def do_POST(self):
 #       pass


#PORT = 8080  # 8080포트로 서비스를 하겠다는 의미
#server = HTTPServer(('', PORT), ServerHandler)
#print(f'서버가 {PORT}로 서비스 되고 있습니다.')
#server.serve_forever()

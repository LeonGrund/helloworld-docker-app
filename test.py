import sys
import socket
import select
import struct
import time


print("\n***D O C K E R  T E S T  A P P  S T A R T E D***\n")

ip = '0.0.0.0'
port = 5000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((ip, port))
#s.connect((ip, port))
s.listen(1)

def helloworld(errorNum, errorType):
    header = 'HTTP/1.1 %d %s \r\nContent-Type: text/html\n' % (errorNum, errorType)
    body = '<html>\r\n\t<head>\r\n\t\t<title>Docker-App\r\n\t\t</title>\r\n\t</head>\r\n\r\n<body>\r\n\t<p><b>Hello to GreenApple Test!!!! (-:</p></b>\r\n</body>\r\n</html>'
    msg = header + body + '\r\n\r\n'
    return msg

print('Hello World App is listening on %s:%d' % (ip, port))

while 1:
    (clientsocket, address) = s.accept()
    toSend = helloworld(200, 'OK')
    clientsocket.send(toSend.encode())
    clientsocket.shutdown(1)
    clientsocket.close()

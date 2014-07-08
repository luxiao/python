from socket import *
from time import ctime

host=''
port=21567
bufsiz=1024
addr=(host,port)

def tcpServer():
  tcpSerSock=socket(AF_INET,SOCK_STREAM)
  tcpSerSock.bind(addr)
  tcpSerSock.listen(5)
  while True:
    print 'waiting for connect...'
    tcpCliSock,addr=tcpSerSock.accept()
    print '...connected from: ',addr
    while True:
      data=tcpCliSock.recv(bufsiz)
      if not data:
        break
      tcpCliSock.send('[[%s] %s' %(ctime(),data))
  tcpCliSock.close()
  tcpSerSock.close()

def udpServer():
  addr=(host,port)
  udpSerSock=socket(AF_INET,SOCK_DGRAM)
  udpSerSock.bind(addr)
  while True:
    print 'waiting for message...'
    data,addr=udpSerSock.recvfrom(bufsiz)
    udpSerSock.sendto('[%s] %s' % (ctime(),data),addr)
    print '...received from and returned to:',addr

  udpSerSock.close()
if __name__=='__main__':
  
  udpServer()

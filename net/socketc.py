from socket import *

host='localhost'
port=21567
bufsiz=1024


def tcpClient():
  tcpCliSock=socket(AF_INET,SOCK_STREAM)
  tcpCliSock.connect(addr)
  while True:
    data=raw_input('>')
    if not data:
      break
    tcpCliSock.send(data)
    data=tcpCliSock.recv(bufsiz)
    if not data:
      break
    print data
  tcpCliSock.close()
def udpClient():
  addr=(host,port)
  udpCliSock=socket(AF_INET,SOCK_DGRAM)
  while True:
    data=raw_input('>')
    if not data:
      break
    udpCliSock.sendto(data,addr)
    data,addr=udpCliSock.recvfrom(bufsiz)
    if not data:
      break
    print data
  udpCliSock.close()

if __name__=='__main__':
  udpClient()

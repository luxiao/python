import base64,os,datetime
from Crypto.Cipher import AES
def aes():
  key = '9e3cf586f11a0a478bfhyd6c1f3beb4a'
  mode = AES.MODE_CBC
  encryptor = AES.new(key, mode)

  text = 'dsadm3850'
  print encryptor.encrypt('9e3cf586f11a0a478bfhyd6c1f3beb4a',text)

def dec():
  log=open(datetime.date.today().isoformat()+'.log','a+')
  log.write('start decrypt: '+str(datetime.datetime.now()))
  encrypt_file='encrypt.txt'
  df='decrypt.txt'
  if os.path.isfile(encrypt_file):
    f=open(encrypt_file)
    p=open(df,'w+')
    i=1;
    for line in f.readlines():
      encrypt=line[line.index('=')+1:]
      print encrypt,
      if encrypt=='':
        pass
      else:
        passwd=base64.b64decode(encrypt.decode('base64'))
        p.write('decrypt%d=%s\n' % (i,passwd))
      i+=1
    p.close()
    f.close()
  else:
    log.write('Can not find a encrypt password file. Please check it.\n')
  log.write('end decrypt: '+str(datetime.datetime.now()))  
if __name__=='__main__':
  aes()

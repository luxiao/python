# -*- coding: cp936 -*-
import re,sys



def level0():
  print 2**38

def level1():
  print ord('K'),ord('M')
  print ord('O'),ord('Q')
  print ord('E'),ord('G')
  s="g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
  #s='map'
  t=''
  for c in s:
    o=ord(c)
    if o>=97 and o<=120:
      t=t+chr(o+2)
    elif o>=121 and o<=122:
      t=t+chr(o-24)
    else:
      t=t+chr(o)
  print t

def level2():
  txt=r'D:\lux\pyscripts\contest\level2_src.txt'
  d={}
  with open(txt) as src:
    for l in src.readlines():
      for c in l:
        d[c]=d.get(c,1)+1
  print d
  
  #组成equality，填入url

def level3():
  txt=r'D:\lux\pyscripts\contest\level3_src.txt'
  p=re.compile(r'[a-z]+[A-Z]{3}([a-z]){1}[A-Z]{3}[a-z]+')  
  with open(txt) as src:
    for l in src.readlines():
      match=re.findall(p,l)
      if match:
        for g in match:
          print match[0],  
  #组成linkedlist，填入url

def level4():
  sys.path.append(r'D:\lux\pyscripts\aia\proxy')
  import access_internet_with_proxy as aproxy 
  prefix='http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
  url=prefix+'12345'
  for i in range(3):
    s=aproxy.open(url)
    print s
    afix=s.split()[-1]
    url=prefix+afix
    #中间会出现一个peak.html，that's the answer.

def level5():
  """这道题我卡住了，因为对pickle不熟，所以咋也和’peak hell'联系不起来"""
  import pickle,pprint
  sys.path.append(r'D:\lux\pyscripts\aia\proxy')
  import access_internet_with_proxy as aproxy
  
  url = 'https://raw.githubusercontent.com/luxiao/python/master/youknowme.pkl'

  lines = aproxy.open(url)
  data = pickle.loads( ''.join(lines) )
  #print data
  for row in data:
    result = ''
    for chars in row:
      result += chars[0] * chars[1]
    print result
    """输出由#号组成的channel单词，程序员还是比较幽默的"""

def readtest():
  import pickle
  p=[]
  flag=''
  count=1  
  with open('malec.txt') as inp:
    for l in inp.readlines():
      #l=l.strip('\\n')
      flag=l[0]
      s=[]
      for c in l:        
        if c==flag:
          count+=1
        else:
          s.append((flag,count))
          count=1
          flag=c
        
      p.append(s)
  #p=[[(' ',86)],[(' ', 39), ('#', 5)], [(' ', 40), ('#', 4)], [(' ', 40), ('#', 4)], [(' ', 40), ('#', 4)], [(' ', 40), ('#', 4)], [(' ', 40), ('#', 4)], [(' ', 40), ('#', 4)], [(' ', 40), ('#', 4)], [('#', 5), (' ', 3), ('#', 3), (' ', 6), ('#', 3), (' ', 10), ('#', 3), (' ', 7), ('#', 4), (' ', 7), ('#', 3), (' ', 3)], [(' ', 1), ('#', 4), (' ', 1), ('#', 7), (' ', 2), ('#', 7), (' ', 6), ('#', 2), (' ', 2), ('#', 3), (' ', 5), ('#', 4), (' ', 4), ('#', 3), (' ', 2), ('#', 3), (' ', 4)], [(' ', 1), ('#', 5), (' ', 4), ('#', 5), (' ', 4), ('#', 4), (' ', 3), ('#', 3), (' ', 3), ('#', 4), (' ', 4), ('#', 4), (' ', 3), ('#', 3), (' ', 5), ('#', 3), (' ', 2)], [(' ', 1), ('#', 4), (' ', 5), ('#', 4), (' ', 5), ('#', 4), (' ', 3), ('#', 3), (' ', 4), ('#', 3), (' ', 4), ('#', 4), (' ', 2), ('#', 3), (' ', 6), ('#', 4), (' ', 1)], [(' ', 1), ('#', 4), (' ', 5), ('#', 4), (' ', 5), ('#', 4), (' ', 10), ('#', 3), (' ', 4), ('#', 4), (' ', 2), ('#', 3), (' ', 7), ('#', 3), (' ', 1)], [(' ', 1), ('#', 4), (' ', 5), ('#', 4), (' ', 5), ('#', 4), (' ', 5), ('#', 2), (' ', 3), ('#', 3), (' ', 4), ('#', 4), (' ', 1), ('#', 4), (' ', 7), ('#', 3), (' ', 1)], [(' ', 1), ('#', 4), (' ', 5), ('#', 4), (' ', 5), ('#', 4), (' ', 3), ('#', 10), (' ', 4), ('#', 4), (' ', 1), ('#', 14), (' ', 1)], [(' ', 1), ('#', 4), (' ', 5), ('#', 4), (' ', 5), ('#', 4), (' ', 2), ('#', 3), (' ', 4), ('#', 4), (' ', 4), ('#', 4), (' ', 1), ('#', 4), (' ', 11)], [(' ', 1), ('#', 4), (' ', 5), ('#', 4), (' ', 5), ('#', 4), (' ', 1), ('#', 4), (' ', 5), ('#', 3), (' ', 4), ('#', 4), (' ', 1), ('#', 4), (' ', 11)], [(' ', 1), ('#', 4), (' ', 5), ('#', 4), (' ', 5), ('#', 4), (' ', 1), ('#', 4), (' ', 5), ('#', 3), (' ', 4), ('#', 4), (' ', 2), ('#', 3), (' ', 11)], [(' ', 1), ('#', 4), (' ', 5), ('#', 4), (' ', 5), ('#', 4), (' ', 2), ('#', 3), (' ', 4), ('#', 4), (' ', 4), ('#', 4), (' ', 3), ('#', 3), (' ', 6), ('#', 2), (' ', 2)], [(' ', 1), ('#', 4), (' ', 5), ('#', 4), (' ', 5), ('#', 4), (' ', 3), ('#', 11), (' ', 3), ('#', 4), (' ', 4), ('#', 3), (' ', 4), ('#', 2), (' ', 3)], [('#', 6), (' ', 4), ('#', 4), (' ', 5), ('#', 5), (' ', 4), ('#', 2), (' ', 4), ('#', 4), (' ', 1), ('#', 6), (' ', 6), ('#', 3), (' ', 6)], [(' ',86)]]
  pkl=pickle.dumps(p)
  print pkl
  
  for row in p:
    result = ''
    for chars in row:
      result += chars[0] * chars[1]
    print result

def level6():
  import zipfile
  zf=zipfile.ZipFile(r'C:\Users\nsnp419\Downloads\channel.zip','r')
  files= zf.namelist()
  start='90052.txt'
  comments=[]
  while(start in files):
    #comments.append(zf.getinfo(start).comment)
    fc=zf.open(start).read()
    if not fc.startswith('Next nothing is '):
      print fc
    start=fc.split()[-1]+'.txt'
  import re
  r=re.compile(r'(\d+)$')

  nextnothing='90052'
  f=zipfile.ZipFile(r'C:\Users\nsnp419\Downloads\channel.zip','r')
  while(1):
    try:
      comments.append(f.getinfo('%s.txt' % nextnothing).comment)
      nextnothing=r.search(f.read('%s.txt' % nextnothing)).group()
    except:
      print ''.join(comments)
      break
  """hockey，这里本应该是答案的，但是题目留了一句话：it's in the air, look at the letters."""

def level7():
  
if __name__=='__main__':
  level6()

  

  

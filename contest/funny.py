# -*- coding: cp936 -*-
import random,sys

def wordcount(src,targ):
  result={}
  with open(src) as inp:
    with open(targ,'w+') as out:
      for line in inp.readlines():
        words=line.split(' ')
        for word in words:
          pass
        

def validate(name):
  """
  1. 用户名要大于8个字节
  2.测试无空格或特殊字符,只能用数字或字母
  3.至少有一个大写字母
  4.至少有一个小写字母
  5.至少有一个数字"""
  result=[0,0,0]
  if len(name)>8:
    for i in name:
      ascii=ord(i)
      if ascii>=48 and ascii<=57:#数字
        result[0]+=1
      elif ascii>=65 and ascii<=90:#大写
        result[1]+=1
      elif ascii>=97 and ascii<=122:#小写
        result[2]+=1
      else:#其他字符
        result[0]=0
        break
  return result

def vcf2json(vcf):
  if os.path.exists(vcf):
    pass
      
  else:
    print 'please check '+vcf+' is a valid file'
def findC(s):
  """通过用户输入一些字母，从联系人中查找并返回"""
  pass

def SJB():
  """剪刀1, 石头2, 布3"""
  m={-1:'lose',-2:'win',1:'win',2:'lose'}
  l={1:'剪刀',2:'石头',3:'布'}
  s=random.randrange
  for i in range(15):    
    you,machine=s(1,4,1),s(1,4,1)
    print l[you]+'vs'+l[machine]+':'+m.get(you-machine,'equal')

def reduc(func,seq,init=None):
  if init is None:
    res=seq.pop(0)
  else:
    res=init
  for i in seq:
    res=func(res,i)
  return res
def fbnq(x):
  if x==1:
    return 1
  else:
    return x+fbnq(x-1)

def closure():
  i=0
  def sub(i):
    i=i+1
    print i
  return sub

def printx():
  """print on your screen
           *
          * *
         * * *
        * * * *
         * * *
          * *
           *
  """
  flag='*'
  space=' '
  row=9
  leng=(row+1)/2
  for i in range(row):
    j=(i<leng and i+1 or row-i)-1  
    mid=flag
    while(j>0):
      mid=mid+space+flag
      j-=1
    slen=(row-len(mid))/2
    print space*slen+mid+space*slen
class C():
  def __call__(self):
    print '__call__'
  def doit(self):
    print 'C'


if __name__=='__main__':
  SJB()
  """
  name=raw_input('Please enter your name: ')
  result=validate(name)
  while(result[0]*result[1]*result[2]<=0):    
    print 'Invalid name!'
    name=raw_input('Please re-enter your name: ')
    result=validate(name)
  else:
    print 'OK, your name is '+name
  """



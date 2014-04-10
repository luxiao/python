# -*- coding: utf-8 -*-
import types
opr=('+','-','*','/','(',')')

class stack:
  def __init__(self,srclist=None):
    self.data=[]
    self.leng=0
    if srclist is not None:
      self.data=srclist
      self.leng=len(srclist)
  def isEmp(self):
    if self.leng==0:
      True
    else:
      False
  def pop(self):
    if not self.isEmp():
      self.leng-=1
      tmp=self.data[self.leng]
      self.data=self.data[:-1]
    else:
      print 'Stack is Empty'      
    return tmp
  def push(self,x):    
    self.leng+=1
    self.data.append(x)
    #print self.data
     
def calc(exp):
  tmp=''
  inlist=[]
  for i in exp:
    if i in opr:
      tmp=tmp+' '+i+' '
    else:
      tmp=tmp+i      
  for i in tmp.split():
    if i in opr:
      inlist.append(i)
    else:
      inlist.append(float(i))
  result=str(toNpl(inlist)).strip().replace('[','').replace(']','').replace("'",'')
  #print result
  tmp=[]
  for x in result.split(', '):
    if type(x)==types.ListType:
      tmp.extend(x)
    else:
      tmp.append(x)
  #print tmp
  s=stack()
  for i in tmp:
    if i not in opr:
      s.push(float(i))
    else:
      x=s.pop()
      y=s.pop()      
      s.push(doit(y,x,i))
  #print 'the Result of is '+str(s.pop())
  return s.pop()
def doit(x,y,op):  
  if op=='+':
    r=x+y
  elif op=='-':
    r=x-y
  elif op=='*':
    r=x*y
  elif op=='/':
    r=x/y
  else:
    r=None
    print 'Unknown operator!'
  return r
  
def toNpl(explist):
  """中缀表达式处理成逆波兰表达式"""
  kh=('(',')')
  result=[]
  #eliminate brackets
  c=explist.count(kh[0])
  if c>0:
    i=explist.index(kh[0])
    result=explist[:i]
    subl=explist[i+1:]
    j=1
    for e in xrange(len(subl)):
      if j>0:
          if subl[e]==kh[0]:
            j+=1
          elif subl[e]==kh[1]:
            j-=1
            if j==0:
              break
    tmp=[]
    tmp=toNpl(subl[:e])
    if e<len(subl)-1:      
      result.append(tmp)
      result.extend(subl[e+1:])
      return toNpl(result)
    result.append(tmp)
    result=parse(result)
  else:
    result=parse(explist)
  return result
  
def parse(explist):  
  xc=('*','/')
  result=[]   
  i=0
  while(i<len(explist)):
    if explist[i] in xc:      
      tmp=(type(result[-1])==types.ListType and [x for x in result[-1]] or [result[-1]]) +[explist[i+1],explist[i]]
      result=result[:-1]
      result.append(tmp)      
      i+=1                          
    else:
      result.append(explist[i])
    i+=1
  i=1
  while(i<len(result)):
    result[i],result[i+1]=result[i+1],result[i]
    i+=2
  return result
  

def test():
  for e in ['1+(2-3*(4/5))-6+7/4*(8-9)','1-(2-3)-4','1*(2-(0+4)/5)','((128+35)*3)','4000/((25-13)*12)','89*(((2+86)))']:
    print calc(e),float(eval(e)),int(calc(e))==eval(e)
  
  
if __name__=='__main__':
  test()
  

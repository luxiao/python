def MaoPaoSort():
  """insert sort"""
  li=[1,3,4,2,9,5,8,6,7]
  print li
  for l in xrange(8):
    i=0
    while(i<len(li)-l-1):
      if li[i+1]<li[i]:
        li[i],li[i+1]=li[i+1],li[i]
      i+=1
    print li
  print li
def ChaRuSort():
  "":::""
  li=[1,3,4,2,9,5,8,6,7]
  for j in xrange(len(li)):
    if li[j+1]<li[j]:
      li[j],li[j+1]=li[j+1],li[j]
  
if __name__=="__main__":
  ChaRuSort()

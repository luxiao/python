import re


text='速速联系，luxiao@tom.com， 电话15731657800，QQ553732713'

lib={}
lib["gemail"]= re.compile(r'[\w.-]+@[\w.-]+')    
lib["cphone"] = re.compile(r"1[-\d\s-]{10,}")    
lib["qqnum"] = re.compile(r"[1-9][\d\s-]{5,}")

def makerelib():
    lib = {}
    lib["gemail"]= re.compile(r'[\w.-]+@[\w.-]+')
    lib["email"] = re.compile(r"(?:^|\s)[-a-z0-9_.]+@(?:[-a-z0-9]+\.)+[a-z]{2,6}(?:\s|$)",re.IGNORECASE)
    lib["postcode"] = re.compile("[a-z]{1,2}\d{1,2}[a-z]?\s*\d[a-z]{2}",re.IGNORECASE)
    lib["zipcode"] = re.compile("\d{5}(?:[-\s]\d{4})?")
    lib["ukdate"] = re.compile \
("[0123]?\d[-/\s\.](?:[01]\d|[a-z]{3,})[-/\s\.](?:\d{2})?\d{2}",re.IGNORECASE)
    lib["time"] = re.compile("\d{1,2}:\d{1,2}(?:\s*[aApP]\.?[mM]\.?)?")
    lib["fullurl"] = re.compile("https?://[-a-z0-9\.]{4,}(?::\d+)?/[^#?]+(?:#\S+)?",re.IGNORECASE)
    lib["visacard"] = re.compile("4\d{3}[\s-]?\d{4}[\s-]?\d{4}[\s-]?\d{4}")
    lib["mastercard"] = re.compile("5[1-5]\d{2}[\s-]?\d{4}[\s-]?\d{4}[\s-]?\d{4}")
    lib["ninumber"] = re.compile("[a-z]{2}\s?\d{2}\s?\d{2}\s?\d{2}\s?[a-z]",re.IGNORECASE)
    lib["isbn"] = re.compile("(?:[\d]-?){9}[\dxX]")
    lib["cphone"] = re.compile(r"1[-\d\s-]{10,}")    
    lib["qqnum"] = re.compile(r"[1-9][\d\s-]{5,}")
    return lib

def getRe(instr,retype):
  outstr=''
  match=re.findall(lib[retype],instr)
  if match:
    for tmp in match:
      if retype=='gemail' and outstr=='':
        outstr=tmp
      if retype=='qqnum' and outstr=='':
        tmp=tmp.replace(' ','').replace('-','')
        if len(tmp)>=5 and len(tmp)<11:
          outstr=tmp
      if retype=='cphone' and outstr=='':
        tmp=tmp.replace(' ','').replace('-','')
        if len(tmp)==11:
          outstr=tmp
  return outstr

def re_chinese():
  sp=u'I am from 美国。We should be friends. 朋友。'
  for n in re.findall(ur'[\uc3c0]+',sp):
    print n
    
if __name__=="__main__":
  print getRe(text,'qqnum')
  print getRe(text,'cphone')
  print getRe(text,'gemail')
    

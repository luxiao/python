import urllib2,os

proxy = urllib2.ProxyHandler({'https': 'http://aia\\nsnp419:aia201404$@10.64.34.237:8080'})
#proxy = urllib2.ProxyHandler({'https': 'http://aia\\nsnp419:aia201404$@cn-aiaproxy.aia.biz:8080'})
auth = urllib2.HTTPBasicAuthHandler()
opener = urllib2.build_opener(proxy, auth, urllib2.HTTPHandler)
urllib2.install_opener(opener)

conn=urllib2.urlopen('https://github.com/')
conn=urllib2.urlopen('https://raw.githubusercontent.com/luxiao/python/master/youknowme.pkl')

#conn=urllib2.urlopen('http://www.pythonchallenge.com/pc/def/ocr.html')
#conn=urllib2.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=94485')
print(conn.read())
"""

conn = urllib2.urlopen('http://mirror.bit.edu.cn/apache//jmeter/binaries/apache-jmeter-2.11.tgz')
lf='c:\\test.tgz'
with open(lf,'wb') as output:
  output.write(conn.read())
if os.path.exists(lf):
  print 'download successfully!'
"""
def open(url):
  conn=urllib2.urlopen(url)
  return conn.read()

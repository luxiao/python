import urllib2, pickle

url = 'https://raw.githubusercontent.com/luxiao/python/master/youknowme.pkl'

lines = urllib2.urlopen(url).readlines()
data = pickle.loads( ''.join(lines) )

for row in data:
    result = ''
    for chars in row:
        result += chars[0] * chars[1]
    print result

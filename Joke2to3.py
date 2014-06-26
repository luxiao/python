import urllib.request, pickle,os

lines = opener.open(url).readlines()
data = pickle.loads( b''.join(lines) )

for row in data:
    result = ''
    for chars in row:
        result += chars[0] * chars[1]
    print(result)

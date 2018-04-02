
# urllib allows python to access the internet
import urllib.request
import urllib.parse

x = urllib.request.urlopen('https://www.google.com')

print(x.read())

url = 'http://pythonprogramming.net'
values = {'s': 'basic',
          'submit': 'Search'}

data  = urllib.parse.urlencode(values) # encoding the query parameters
data = data.encode('utf-8') # encoding in utf-8
req = urllib.request.Request(url, data)
resp = urllib.request.urlopen(req)
respData =  resp.read()

with open('sample_urllib.html', 'w') as f:
    f.write(str(respData))


# this fails as google prohibits access from python
try:
    x = urllib.request.urlopen('https://www.google.com/search?q=test')
    print(x.read())
except Exception as e:
    print(str(e))

# using trick we can overwrite header information
try:
    url = 'https://www.google.com/search?q=python'

    # now, with the below headers, we defined ourselves as a simpleton who is
    # still using internet explorer.
    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    req = urllib.request.Request(url, headers = headers)
    resp = urllib.request.urlopen(req)
    respData = resp.read()

    saveFile = open('sample_urllib_2.html','w')
    saveFile.write(str(respData))
    saveFile.close()
except Exception as e:
    print(str(e))








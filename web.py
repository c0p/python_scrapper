import urllib2
try:
    urllib2.urlopen('http://www.google.com')
    html = response.read()
    print(html)
except urllib2.HTTPError, e:
    print(e.code)
except urllib2.URLError, e:
    print(e.args)
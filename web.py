import urllib





class WebScraper(object):


  def __init__(self, url):
    #checks and verifys
    self.url = url
    f = urllib.urlopen(url)
    print ("pinging to " + self.url)

    try:
      f = urllib.urlopen(url)
    except urllib.error.HTTPError as e:
       print('HTTPError: '+e.code)
       print('invalid HTTP')
    except urllib.error.URLError as e:
     print('URLError: '+e.reason)
     print('invalid URL')
    else:

      print('Connection Success! What do you wanna do?')
      print('[ a ] : Display HTML Contents')
      print('[ b ] : Display Data Contents')
      print('[ c ] : Display HTML Contents')
      userOption = raw_input("Choose Option >  ")

      if userOption == "a":
        self.viewHTMLContents(f)
      elif userOption =="b":
        self.Web_Headers(f)


  def viewHTMLContents(self, url):
    #print HTML contents
    print url.read()

  def Web_Headers(self, url):
    print "     "
    print 'RESPONSE:', url
    print 'URL     :', url.geturl()

    headers = url.info()
    print 'DATE    :', headers['date']
    print 'HEADERS :'
    print '----------'
    print headers

    data = url.read()
    print 'DATA LENGTH  :', len(data)





###random bluaghwqeqwe
try:
    while True:
      websiteInput = raw_input("Enter Desired URL > ")
      User_URL = "https://" + websiteInput
      demo = WebScraper(User_URL)
except KeyboardInterrupt:
    pass


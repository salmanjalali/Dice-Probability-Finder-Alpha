import urllib2
from urllib2 import urlopen
import re
import cookielib
from cookielib import CookieJar
import time

def main():
    try:
        
        cj = CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        opener.addheaders = [('User-agent','Mozilla/5.0')]
        
        thePage = "http://themoneyconverter.com/rss-feed/USD/rss.xml"
        sourceCode = opener.open(thePage).read()

        try:
            description = re.findall(r"<description>(.*?)</description>", sourceCode)
            time = re.findall(r"<lastBuildDate>(.*?)</lastBuildDate>", sourceCode)
            
            b = open("testXML.txt", "w")
            for t in time:
                b.write(t + "\n")
            for d in description:
                b.write(d + "\n")
            b.close()

        except Exception, e:
            print str(e)

    except Exception, e:
        print str(e)

main()
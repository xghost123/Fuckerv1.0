#!/usr/bin/python


try:
  import os, sys , random , httplib , urllib2
except:
  print 'You need print os , httplib , urllib2 , random and sys librarys installed.'
  
try:
  from platform import system
except:
  print 'You need print platform library installed.'

sys.stdout.write("\x1b]2;Fucker v1.0\x07") # setting the title

from modules import drupal


logo = ''' 
  ___        _                 _   __  
 | __|  _ __| |_____ _ _  __ _/ | /  \ 
 | _| || / _| / / -_) '_| \ V / || () |
 |_| \_,_\__|_\_\___|_|    \_/|_(_)__/ 
                                       
'''                                                                
menu = '''  
         [1] Get Wordpress Website
         [2] Get Joomla Website
         [3] Sql Scanner
         [4] Drupal Exploiter
         [5] Find Login Page
         [6] About Us
    ''' 
def About():
  print '''
  ___        _                 _   __  
 | __|  _ __| |_____ _ _  __ _/ | /  \ 
 | _| || / _| / / -_) '_| \ V / || () |
 |_| \_,_\__|_\_\___|_|    \_/|_(_)__/                                                                                                              
    FB : https://www.facebook.com/khalil.ch.5059
    YTB : https://www.youtube.com/channel/UCNEctOSA_jyPiivieBsKQEQ
 '''                                                               

def wpscan():
    ip = raw_input('2- IP : ')
    page = 1
    sites = list()
    while page <= 50 :

    	url    ="http://www.bing.com/search?q=ip%3A"+ip+"+wordpress&go=Valider&qs=ds&form=QBRE&first="+str(page)
    	re     = urllib2.Request(url)
    	opreq  = urllib2.urlopen(req).read()
    	findurl = re.findall('<div class="b_title"><h2><a href="(.*?)" h=',opreq)
    	page += 1

    	for url in findurl :
    		                   split = urlparse(url)
    		                   site   = split.netloc
    		                   if site not in sites :
    		                            print site
    		                            site.append(site) 
def joom():
    ip = raw_input('2- IP : ')
    page = 1
    sites = list()
    while page <= 50 :

      url    ="http://www.bing.com/search?q=ip%3A"+ip+"+wordpress&go=Valider&qs=ds&form=QBRE&first="+str(page)
      re     = urllib2.Request(url)
      opreq  = urllib2.urlopen(req).read()
      findurl = re.findall('<div class="b_title"><h2><a href="(.*?)" h=',opreq)
      page += 1

      for url in findurl :
                           split = urlparse(url)
                           site   = split.netloc
                           if site not in sites :
                                    print site
                                    site.append(site) 
def adminpanel():
    var1 = 0
    var2 = 0
    adminpanels = ['admin/', 'adminpanel/', 'login/', 'wp-admin/', 'administrator/', 'admin/login.php' ]
    try:

     site = raw_input('2- Site : ')  
     site = site.replace("http://","")
     print ("\tChecking website " + site + "...")
     conn = httplib.HTTPConnection(site)
     print "\t[$] Get Ready ... Server is Online."
    except (httplib.HTTPResponse, socket.error) as Exit:
      raw_input("\t [!] Oops Error occured, Server offline or invalid URL")
      exit()
    print("\t[$]Scanning " + site + " ...\n\n")
    for admin in adminpanels:
      admin = admin.replace("\n","")
      admin = "/" + admin
      host = site + admin
      print ("\t [#] Checking " + host + "...")
      connection = httplib.HTTPConnection(site)
      connection.request("GET",admin)
      response = connection.getresponse()
      var2 = var2 + 1
      if response.status == 200:
          var1 = var1 + 1
          print "%s %s" % ( "\n\  n>>>" + host, "Admin page found!")
          raw_input("Press enter to continue scanning.\n")
      elif response.status == 404:
          var2 = var2
      elif response.status == 302:
          print "%s %s" % ("\n>>>" + host, "Possible admin page (302 - Redirect)")
      else:
          print "%s %s %s" % (host, " Interesting response:", response.status)
      connection.close()
    print("\n\nCompleted \n")
    print var1, " #Admin pages found"
    print var2, " #total pages scanned"
    raw_input("[/] Game Over BB ; Press Enter to Exit") 
def checksql():
     momo = raw_input("Please specify the full vulnerable url:  ")

     resp = urllib2.urlopen(momo + "'")
     body = resp.read()
     fullbody = body.decode('utf-8')

     if "You have an error in your SQL syntax" in fullbody:
          print ("The website is classic SQL injection vulnerable!")
     else:
	       print ("The website is not classic SQL injection vulnerable!")
def main():
 print logo
 print menu
 choose = raw_input("choose a number :")
 while True :
 
  if choose == "1":
    wpscan()
  if choose == "2":
    joom()
  if choose == "3":
    checksql()
  if choose == "4":
    drupal.init()  
  if choose == "5":
    adminpanel()  
  if choose == "6":
    About()
  if choose == "11":
        print "#By"
        exit()
  con = raw_input('Continue [Y/n] -> ')
  if con[0].upper() == 'N' :
                                exit()
  if con[0].upper() == 'Y' :
                                main()
                               
 
if __name__ == '__main__':
  main()                                

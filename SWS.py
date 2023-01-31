
from pyfiglet import Figlet
custom_fig = Figlet(font='ivrit')
print(custom_fig.renderText('SWS'))
def startmassage():
    print("#"+"*"*77+"#")
    print("| Script Name : Scan Web Security (SWS)|")
    print("| About Me    :[ 5plint3r ] -CyberSecurity Engineer |")
    print("| About Me    :Security engenier] |")
    print("#"+"*"*77+"#")
    print("\n")
startmassage()

from urllib import response
import requests
from bs4 import BeautifulSoup
from responses import target
from urllib.request import urlopen


while True:
    print("Seleccione una opcion: ")
    print("1.Scraper")
    print("2.Fuzzer")
    print("3.Crawler")    
    print("4.XSS")
    print("5.Salir")
    

    choice=int(input("Seleccione una opcion:"))
    
    if choice==1:
        target = input("Ingrese Pagina web:")
        response = requests.get(target)
        soup = BeautifulSoup(response.text, 'html.parser')
        for a in soup.find_all("a", href=True):
          print("Encontrado:", a['href'] if a['href'].startswith("http") else
        str(response.url[:-1] + a['href']))
    
    elif choice==2:
        def load_dict():
            with open("dict.txt", "r") as dict_file:
                return dict_file.readlines()            
        wordlist = load_dict()
        target = input("Ingrese Pagina web: ")

        response = requests.get(target)
        for word in wordlist:

            if response.status_code in [200,301,302]:
                    print("Encontrado: %s - %s" % (target + word.strip(), response.status_code))

    elif choice == 3:
        def load_dict():
            with open("dict.txt", "r") as dict_file:
                return dict_file.readlines()            
        wordlist = load_dict()
        target = input("Ingrese Pagina web: ")

        response = requests.get(target)
        for word in wordlist:

            if response.status_code in [200,301,302]:
                    print("Encontrado: %s - %s" % (target + word.strip(), response.status_code))
    
    elif choice==4:
    
        urli=input("Ingrese Pagina web: ")
        header={"Cookie": "security=low; PHPSESSID=a0b29e43b154e8cf261c3a93686bdd94"}
        xssl=["cookie","<h1>cookie","<script>alert('cookie')</script>"]
        for payload in xssl:
            print(payload)
            url=urli+str(payload)
            sonuc=requests.get(url=url,headers=header)
            if str(payload) in str(sonuc.content):
                print("xss var, payloadlar: ",str(payload))
            else:
                print("¡ERROR!, xss no encontrado. Vuelva a intentarlo más tarde.")   
    
    elif choice == 5:


        break
    else:
        print("Wrong Choice")

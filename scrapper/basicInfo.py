import requests
from responses import about_user
from bs4 import BeautifulSoup
from colorama import Fore
from connection import conn

def basic(userName):
    
    obConn = conn()
    
    response = about_user(userName)
    soup = BeautifulSoup(response.content , "html.parser")
    all = soup.find_all('span' , class_="stat")
    
    
    ###Dictionary  ........
    basicDict = {
        "Basic Information:":[]
    }       
    
    print(" ")
    print(Fore.LIGHTBLUE_EX+"Basic Information of : "+Fore.LIGHTCYAN_EX+userName)
    if(all):
        for all_info in all:
          print(Fore.LIGHTGREEN_EX+all_info.text)
          basicDict["Basic Information:"].append(all_info.text)
    else:
        print("no user found")
    return basicDict
    
    

if(__name__=='__main__'):
    basic('hwilliams10')
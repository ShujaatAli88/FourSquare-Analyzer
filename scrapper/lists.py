from responses import lists_Info
from bs4 import BeautifulSoup
from colorama import Fore
from connection import conn

def myList_info(userName):
    
    ob_conn = conn()
    response = lists_Info(userName)
    soup = BeautifulSoup(response.content , "html.parser")
    
    places_Names = soup.find_all('p' , class_="venueName")
    addresses = soup.find_all('span' , class_ = "address")
    
    print(" ")
    print(Fore.LIGHTCYAN_EX+"List of Places That "+Fore.LIGHTGREEN_EX+userName+Fore.BLUE+" Liked:")
   
   
    places_Liked = {
        "Places Liked":[]
    }
    counter = 0
    places_list = []
    places_address = []
    for place in places_Names:
        placeNamed = place.text
        places_list.append(placeNamed)
    for add in addresses:
        addreed = add.text
        places_address.append(addreed)
    
    for i in range(len(places_address)):
        places_Liked["Places Liked"].append(places_list[i]+" Location : "+places_address[i])
        print(Fore.LIGHTGREEN_EX+places_list[i]+Fore.LIGHTBLUE_EX+" Location : "+Fore.LIGHTGREEN_EX+places_address[i])
    
    ob_conn.index(index='squarefour' , doc_type='doc' ,body=places_Liked)

if(__name__=='__main__'):
    myList_info('hwilliams10')
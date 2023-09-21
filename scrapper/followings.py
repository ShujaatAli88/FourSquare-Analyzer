import requests
import json
from colorama import Fore
from connection import conn

def my_followings(id):
    
    myOb = conn()
    
    req_url = 'https://api.foursquare.com/v2/users/'+id+'/following?locale=en&explicit-lang=false&v=20230919&id=6677827&limit=197&afterMarker=&m=foursquare&wsid=2VHU0ZEATZ5BRLOACKBDBHYUUKZUCT&oauth_token=4JJZD434VF3MTZERIOTCKSJVUMBMY3LQXCO1L50LKBSOXC2Q'
    response = requests.get(req_url)
    data = json.loads(response.content)
    main_data = data.get("response")["following"]["items"]
    
    
    #Following Dictionary...
    following_list = {
        "following":[]
    }
    
    if(main_data):
        print(" ")
        print(Fore.LIGHTCYAN_EX+"Total Followings:")
        counter = 1
        for each_user in main_data:
            user = each_user["user"]
            firstName = user.get("firstName")
            lastName = user.get("lastName")
            homeCity = user.get("homeCity")
            
            dictMy = {
                "First Name:":firstName,
                "Last Name:":lastName,
                "Home City:":homeCity
            }
            
            following_list["following"].append(dictMy)
            
            if(lastName):
                print(str(counter)+"."+Fore.LIGHTGREEN_EX+firstName+" "+lastName+Fore.LIGHTBLUE_EX+" Home-City : "+homeCity)
            else:
                print(str(counter)+"."+Fore.LIGHTMAGENTA_EX+firstName+Fore.LIGHTBLUE_EX+" Home-City : "+homeCity)
            counter = counter +1
        
    else:
        print("No followers..")

    return following_list

if(__name__=='__main__'):
    my_followings('6677827')
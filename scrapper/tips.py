import requests
import json
from colorama import Fore
from connection import conn

def my_tips(id):
    
    obj_conn = conn()
    req_url = 'https://api.foursquare.com/v2/users/'+id+'/tips?locale=en&explicit-lang=false&v=20230919&id=6677827&limit=18&offset=0&sort=recent&m=foursquare&wsid=2VHU0ZEATZ5BRLOACKBDBHYUUKZUCT&oauth_token=4JJZD434VF3MTZERIOTCKSJVUMBMY3LQXCO1L50LKBSOXC2Q'
    response = requests.get(req_url)
    data = json.loads(response.content)
    main_data = data.get("response")["tips"]["items"]
    tips_count = data.get("response")["tips"]["count"]
    
    
    ##Tips Dictionary...
    tips_Query = {
        "Tips:": []
    }
    
    res_Name = main_data = data.get("response")["tips"]["items"]
    if(main_data):
        print(" ")
        print(Fore.LIGHTCYAN_EX+"Total Tips : "+Fore.LIGHTBLUE_EX+str(tips_count))
        counter = 1
        for each_user in main_data:
           my_text = each_user["text"]
           print(Fore.LIGHTGREEN_EX+str(counter)+"."+Fore.LIGHTBLUE_EX+my_text)
           print(Fore.LIGHTGREEN_EX+"Name :"+each_user["venue"]["name"])
           my_Dict = {
               "Text:": my_text,
               "Name of Service:":each_user["venue"]["name"]
           }
           tips_Query["Tips:"].append(my_Dict)
           print(" ")
           counter = counter + 1
           
    else:
        print("No followers..")
    return tips_Query

if(__name__=='__main__'):
    my_tips('6677827')
    
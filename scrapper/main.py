from basicInfo import basic
from followers import my_followers
from followings import my_followings
from lists import myList_info
from tips import my_tips
from connection import conn

def main_exe(id , userName):
    basicOB =basic(userName)
    listOB = myList_info(userName)
    followerOb = my_followers(id)
    followingOb = my_followings(id)
    myTips = my_tips(id)
    
    dumpIt = {
        "Basic of User:":basicOB,
        "List:":listOB,
        "Following:":followingOb,
        "Followers:":followerOb,
        "Tips:":myTips
    }
    
    connObject = conn()
    connObject.index(index='squarefour' ,id=userName, doc_type='doc' , body=dumpIt)
    
if(__name__=='__main__'):
    main_exe('68732419' , 'jonmuir')
    
## id = '6677827'  & userName = 'hwilliams10'

##Another user id = '68732419' & userName = 'jonmuir'
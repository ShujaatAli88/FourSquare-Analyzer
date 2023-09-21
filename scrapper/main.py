from basicInfo import basic
from followers import my_followers
from followings import my_followings
from lists import myList_info
from tips import my_tips

def main_exe(id , userName):
    basic(userName)
    myList_info(userName)
    my_followers(id)
    my_followings(id)
    my_tips(id)
    
if(__name__=='__main__'):
    main_exe('68732419' , 'jonmuir')
    
## id = '6677827'  & userName = 'hwilliams10'

##Another user id = '68732419' & userName = 'jonmuir'
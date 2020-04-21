#bomber functions
#author : Samartha
import requests
import getpass
import json
un=getpass.getuser();
def ifExists(un):
    request_string="http://og-bomber-server/isExist.php?un="+username
    exists_response=requests.get(request_string).text
    if 'true' in exists_response:
        return True
    elif 'false' in exists_response:
        return False

def blackList(phno):
    request_string="http://og-bomber-server/blackList.php"
    # bl=requests.get(request_string).text
    # print(bl.split())
    bl=requests.get(request_string).text
    bl_json=json.loads(bl)
    for i in bl_json:
        if int(i)==phno:
            return False
    return True

def getUserDetails(un):
    request_string="http://og-bomber-server/userDetails.php?un="+un
    user_details=requests.get(request_string).text.split('\x00',2)[1]
    user_details_json=json.loads(user_details)
    u=user_details_json
    return u

def checkQuota(x):
    request_string="http://og-bomber-server/checkQuota.php?id="+x["uid"]
    daily_quota=requests.get(request_string).text.split('\x00',2)[1]
    if daily_quota<50:
        return True
    else:
        return False
checkQuota(getUserDetails(un))

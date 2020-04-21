#setup to install og-bomber
#author : Samartha
import platform
import getpass
import os
import json
banner="""

    ██████╗  ██████╗       ██████╗  ██████╗ ███╗   ███╗██████╗ ███████╗██████╗
    ██╔═══██╗██╔════╝       ██╔══██╗██╔═══██╗████╗ ████║██╔══██╗██╔════╝██╔══██╗
    ██║   ██║██║  ███╗█████╗██████╔╝██║   ██║██╔████╔██║██████╔╝█████╗  ██████╔╝
    ██║   ██║██║   ██║╚════╝██╔══██╗██║   ██║██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗
    ╚██████╔╝╚██████╔╝      ██████╔╝╚██████╔╝██║ ╚═╝ ██║██████╔╝███████╗██║  ██║
    ╚═════╝  ╚═════╝       ╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝
                    ---------text & call bomber-spoofing---------
                            -----author : Samartha-----
                                 ---build v1.0---
"""
os.system('cls')
print(banner)
print('::Checking Requirements::')
try:
    import requests
    print("[+]requests - available")
except ImportError:
    print("[-]requests - not available")
    try:
        print("::Trrying to install requests::")
        os.system("pip install requests")
        print("[+]requests installed")
    except Exception :
        print("Couldnt install [-]requests\nTry again later")
        exit()
myOs=platform.system()
username = getpass.getuser()
print("::Registering the user::")
request_string="http://og-bomber-server/isExist.php?un="+username
exists_response=requests.get(request_string).text
if 'true' in exists_response:
    print("[+]user Already registered")
elif 'false' in exists_response:
    request_string="http://og-bomber-server/register.php?un="+username+"&os="+myOs
    print("[+]User registered")
print("::User profile::")
request_string="http://og-bomber-server/userDetails.php?un="+username
user_details=requests.get(request_string).text.split('\x00',2)[1]
user_details_json=json.loads(user_details)
u=user_details_json
print("[+]Username : ",u["uname"],"\n[+]Subscription : ",u["urole"], "\n[+]Quota    : ",u["uquota"])
if u["urole"]=="free":
    print("""Now you are having free membership. You are limited to sent 50 messages everyday
Subscribe to premium and get 1000+ messages everyday
::Use this to prank your friends only::
::dont misuse::""")

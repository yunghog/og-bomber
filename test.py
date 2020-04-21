import requests
import platform
import getpass
myOs=platform.system()
username = getpass.getuser()
request_string="http://og-bomber-server/register.php?un="+username+"&os="+myOs
reg_response=requests.get(request_string)
print(reg_response.json())

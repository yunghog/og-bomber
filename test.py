import requests,json
request_string="http://og-bomber-server/blackList.php"
bl=requests.get(request_string)
print(bl)

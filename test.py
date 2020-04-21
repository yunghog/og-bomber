import json
f=open('siteApis.json','r')
data=json.loads(f.read())
print(data["author"])
sites=data["sites"]
for i in sites:
    print(i["name"])

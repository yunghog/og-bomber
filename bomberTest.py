import requests
cc='91'
pn='8310001420'
url = "https://rest-ww.telesign.com/v1/anonymous/session/sms"

payload = "{\"phone_number_1\":\"918310001420\",\"phone_number_2\":\"918904460742\",\"validity_period\":1}"
headers = {'content-type': 'application/json'}

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)

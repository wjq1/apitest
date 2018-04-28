import requests
import json
s=requests.session()
response=s.post('http://pc4.shein.com/user/auth/login',{'email':'test2@666.com','password':'123456'})
cookie=response.cookies
c=requests.cookies.RequestsCookieJar()
c.set('memberId',cookie['memberId'])
c.set('userinfo_email',cookie['userinfo_email'])
c.set('userinfo_userId',cookie['userinfo_userId'])
s.cookies.update(c)

r=s.get('http://pc4-au.shein.com/user/wishlist/add?goods_id=70')
print(r)
print(r.text)
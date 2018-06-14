import requests
import json
s=requests.session()
response=s.post('https://www.shein.com/user/auth/login',{'email':'test@s.com','password':'123456'})
cookie=response.cookies
c=requests.cookies.RequestsCookieJar()
c.set('memberId',cookie['memberId'])
c.set('userinfo_email',cookie['userinfo_email'])
c.set('userinfo_userId',cookie['userinfo_userId'])
s.cookies.update(c)

r=s.get('http://www.shein.com/user/wishlist/add?goods_id=7090')
print(r)
print(r.text)
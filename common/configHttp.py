import requests
import config.readconfig
h=config.readconfig.Getconfigvalue()
class ConfigHttp:
    def __init__(self):
        global host
        host=h.get_conf("host1")
        self.headers={}
        self.params={}
        self.data={}
        self.url=None
    def set_url(self,url):
        self.url=host+url
    def set_headers(self,header):
        self.headers=header
    def set_params(self,param):
        self.params=param
    def set_data(self,data):
        self.data=data
    def get(self):
        try:
            response=requests.get(url=self.url,params=self.params,headers=self.headers)
            return response
        except TimeoutError:
            print("time out")

    def post(self):
        try:
            response = requests.post(self.url, headers=self.headers, data=self.data)
            return response
        except TimeoutError:
            print("Time out!")



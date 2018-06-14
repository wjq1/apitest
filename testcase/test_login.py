import common.httpqingqiu
import common.getexcel
import unittest
logincase=common.getexcel.getcase(r"d:\apitest\testcase.xlsx","login")
import json
class Testlogin(unittest.TestCase):
    def setUp(self):
        pass
        #self.header={'Content-Type': 'application/json; charset=utf-8'}
    def test_loginapi(self):
        for i in range(len(logincase)):
            response_text=common.httpqingqiu.HttpReq(logincase[i]['url'],json.loads(logincase[i]['data']),logincase[i]['method']).httprequest()
            res=json.loads(response_text)
            self.assertEqual(res["msg"],logincase[i]['qiwang'])
    def tearDown(self):
        pass
if __name__=="__main__":
    unittest.main()





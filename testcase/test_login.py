import common.httpqingqiu
import common.getexcel
import unittest
logincase=common.getexcel.getcase("testcase.xlsx","login")
import json
class Testlogin(unittest.TestCase):
    def setUp(self):
        pass
    def test_loginapi(self):
        for i in range(len(logincase)):
            response_text=common.httpqingqiu.HttpReq(logincase[i]['url'],json.loads(logincase[i]['casedata']),logincase[i]['casemethod']).httprequest()
            res=json.loads(response_text)
            self.assertEqual(res["msg"],logincase[i]['caseqiwang'])
    def tearDown(self):
        pass
if __name__=="__main__":
    unittest.main()





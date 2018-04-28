import unittest
import common.httpqingqiu
import common.getexcel
class Test_addwishlist(unittest.TestCase):
    def setUp(self):
        self.header=
    def test_addwish(self):
        casewish=common.getexcel.getcase('testcase.xlsx','addwishlist')
        for i in range(len(casewish)):
            response=common.httpqingqiu.HttpReq(casewish[i]['url'],casewish[i]['casedata'],casewish[i]['casemethod']).httprequest()
            print(response)
            print(casewish[i]['caseqiwang'])
            #self.assertEqual(response,casewish[i]['caseqiwang'])
    def tearDown(self):
        pass
if __name__=='__main__':
    unittest.main()

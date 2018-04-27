import HTMLTestRunner
import datetime
import unittest
import common.sendmail
import config.readconfig
def gettestsuite():
    testsuite=unittest.TestSuite()
    discover=unittest.defaultTestLoader.discover(r"d:\apitest\testcase",pattern='test*.py')
    for case in discover:
        testsuite.addTests(case)
    return testsuite
if __name__=='__main__':
    time=datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    fujian=r'd:\apitest\result\testreport%s.html'%time
    file=open(fujian,'wb')
    runner=HTMLTestRunner.HTMLTestRunner(description="测试结果",stream=file,title="自动化测试报告")
    runner.run(gettestsuite())
    file.close()
    a=config.readconfig.getconfvalue("email")
    common.sendmail.send_mail(a[0],a[4],a[1],a[2],a[3],fujian)

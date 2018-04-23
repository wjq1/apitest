#excel xlrd
# import xlrd
# file=xlrd.open_workbook(r'd:\test.xls')
# a=file.sheet_names()
# sheet=file.sheets()[0]
# nrows=sheet.nrows
# ncols=sheet.ncols
# for i in range(sheet.nrows):
#     print(sheet.row_values(i))
#
# print(sheet.row_values(1))
# print(sheet.col_values(1))
# print(sheet.cell(0,0).value)
# print(sheet.row(0)[1].value)
# # print(a)
# # print(sheet)
# # print(nrows)
# # print(ncols)


#requests get
#import requests
# url="http://www.romwe.co.in/IN-Blouses-Skirts-vc-350731.html"
# response=requests.get(url)
# print(response.text)


#requests post
# import requests
# import json
# url="https://pc8.shein.com/user/auth/login"
# email="test2@666.com"
# password='123456'
# data={"email":email,"password":password}
# dj=json.dumps(data)
# head={"Content-Type":"application/json"}
# reponse=requests.post(url=url,data=dj,headers=head,verify=False)
# print(reponse.text)
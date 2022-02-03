import requests
import pandas as pd
import os
data = []
url = "http://ehall.szu.edu.cn/jwapp/sys/kccx/modules/kccx/kcxxcx.do?pageSize=16940&pageNumber=1"

headers = {
  'Accept':'*/*',
  'Accept-Encoding':'gzip, deflate',
  'Accept-Language':'zh-CN,zh;q=0.9',
  'Connection':'keep-alive',
  'Cookie':'route=dca48fec126b3d7c5e6354cda3035b78; EMAP_LANG=zh; THEME=teal; _WEU=ZUI765MgGn8dcDisTsnbXKT1Ub6X8MxqqIaJ_UxOyill8lm0FrWE0xDEJSjfbzYZFku3MN8d2mGWFPgdaOFGpOTbJXqoAXVrcdJbwXLb0Kj.; insert_cookie=28057208; route=2a475b73d3a6cf787725a7528f7b427e; zg_did={"did":"17e61661af6485-0ec5d2ff049b8b-f791b31-1fa400-17e61661af7da3"}; zg_={"sid":1642311588603,"updated":1642311588607,"info":1642311588605,"superProperty":"{}","platform":"{}","utm":"{}","referrerDomain":"ehall.szu.edu.cn","cuid":"2019274001"}; MOD_AUTH_CAS=MOD_AUTH_ST-1491257-9vHngJjacpYtRhAduewu1643900443075-RSAY-cas; asessionid=722e7c23-b638-4e9d-bf5b-e28ca3f697f2; amp.locale=undefined; JSESSIONID=hKLAGt45Lc8qEQA_jdxDWQPg5e7sZQf62yEyXmpyIIvJqE5uX7c7!-1307058481',
  'Host':'ehall.szu.edu.cn',
  'Origin':'http://ehall.szu.edu.cn',
  'Referer':'http://ehall.szu.edu.cn/jwapp/sys/kccx/*default/index.do?t_s=1641623594340&amp_sec_version_=1&gid_=Y3dRTHJqSU9NeXM2VGRUT25kOW14bnYvdEl3c0pQOVVNTWJGRlJSRjlqc3ZlK3kyRWtxajUwZzdud2RTRm1rNW44eVRVQXhWT3VnY2lpZitUbXZQZXc9PQ&EMAP_LANG=zh&THEME=teal',
  'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
  'X-Requested-With':'XMLHttpRequest',
  'Content-Type':'application/x-www-form-urlencoded'
}
print(os.getcwd())
for i in range(18):
    payload = {'pageNumber':i+1,'pageSize':999}
    response = requests.request("POST", url, headers=headers, data=payload)
    element  = response.json()['datas']['kcxxcx']['rows']
    # print(element)
    data = data + element
    # print(data)

all_pdData = pd.json_normalize(data)
print(all_pdData)
# all_pdData.to_csv('data/allCourseBaseData.csv',encoding='utf-8-sig',index=None)
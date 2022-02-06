import requests
import pandas as pd
import os
data = []
url = "http://ehall.szu.edu.cn/jwapp/sys/kccx/modules/kccx/kcxxcx.do"

headers = {
  'Accept':'*/*',
  'Accept-Encoding':'gzip, deflate',
  'Accept-Language':'zh-CN,zh;q=0.9',
  'Connection':'keep-alive',
  'Cookie':'route=dca48fec126b3d7c5e6354cda3035b78; EMAP_LANG=zh; THEME=teal; _WEU=prwKLcA*FzBvcwUf80S13VK_f1qjq7gbZA_AiAmk6HwihUQ4tAnvJhBZ8*3hfukpQI7fH3Kh8WHTTlO8pha44VBoXg7W1ZgZ_NphtLq8kMG.; insert_cookie=28057208; route=2a475b73d3a6cf787725a7528f7b427e; zg_did={"did": "17e61661af6485-0ec5d2ff049b8b-f791b31-1fa400-17e61661af7da3"}; zg_={"sid": 1642311588603,"updated": 1642311588607,"info": 1642311588605,"superProperty": "{}","platform": "{}","utm": "{}","referrerDomain": "ehall.szu.edu.cn","cuid": "2019274001"}; UM_distinctid=17eca94c517f8-039ee5592dde41-f791539-144000-17eca94c518e04; MOD_AUTH_CAS=MOD_AUTH_ST-1497752-0yPfCGbyASZZSBZdTRNz1644087925668-RSAY-cas; asessionid=3d265354-526c-4c63-bef8-613181f8026a; amp.locale=undefined; JSESSIONID=xXjLRulJS6lA9stBzWHi-3L5zPcaFNrkM_Uw4uTMHWNZy4spk4iK!-1307058481',
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
all_pdData.to_csv('data/allCourseBaseData.csv',encoding='utf-8-sig',index=None)
import requests

import jsonpath


class TestA:
    def test_get_login1(self):
        params = {"limit": "2"}
        re = requests.get(url="https://testerhome.com/api/v3/topics.json", params=params, verify=False)
        print(re.json())
        user = re.json()["topics"][-1]["user"]["login"]
        print(user)
        assert user == "liangqiangWang"

    def test_xueqiu_search(self):
        params = {"code": "sougou", "size": "3", "page": "1"}
        url = "https://xueqiu.com/stock/search.json"
        headers = {"Accept": "application/json",
                   "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
                   "Cookie": "acw_tc=2760820415695559354018725efc2eb7e0d2d3f33cd52e8eb0c7dfcce2fa70; s=c111j6iu1c; device_id=9e5528d5683d5bdea5716cee16446e58; aliyungf_tc=AQAAACI++AQG2woA7AcedLDHBqBLT+xE; xq_a_token=d831cd39b53563679545656fba1f4efd8e48faa0; xq_r_token=fd2f0f487c8298cad8e7519f1560abb7a18c589d; u=801570952990762; __utma=1.1985070286.1570954568.1570954568.1570954568.1; __utmc=1; __utmz=1.1570954568.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; Hm_lvt_1db88642e346389874251b5a1eded6e3=1570952991,1570954563,1570954568,1570954804; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1570972501"}
        re = requests.get(url=url, params=params, headers=headers, verify=False)
        print(re.status_code)
        print(re.json()["stocks"][0]["name"])
        assert re.json()["stocks"][0]["name"] == "搜狗"

    def test_xueqiu_search1(self):
        params = {"code": "sougou", "size": "3", "page": "1"}
        url = "https://xueqiu.com/stock/search.json"
        headers = {"Accept": "application/json",
                   "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
                   "Cookie": "acw_tc=2760820415695559354018725efc2eb7e0d2d3f33cd52e8eb0c7dfcce2fa70; s=c111j6iu1c; device_id=9e5528d5683d5bdea5716cee16446e58; aliyungf_tc=AQAAACI++AQG2woA7AcedLDHBqBLT+xE; xq_a_token=d831cd39b53563679545656fba1f4efd8e48faa0; xq_r_token=fd2f0f487c8298cad8e7519f1560abb7a18c589d; u=801570952990762; __utma=1.1985070286.1570954568.1570954568.1570954568.1; __utmc=1; __utmz=1.1570954568.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; Hm_lvt_1db88642e346389874251b5a1eded6e3=1570952991,1570954563,1570954568,1570954804; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1570972501"}
        re = requests.get(url=url, params=params, headers=headers, verify=False)
        name = jsonpath.jsonpath(re.json(), "$..stocks[0].name")
        print(name)
        value = jsonpath.jsonpath(re.json(), "$..[name]")
        print("value:", value[0])

    def test_get_token(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        params = {"corpid": "XXXX", "corpsecret": "XXXX"}
        response = requests.get(url=url, params=params, verify=False)
        print(response.json())
        if response.status_code == 200:
            errcode = response.json()["errcode"]
            if errcode == 0:
                print(errcode)
                access_token = response.json()["access_token"]
            else:
                print(errcode)
                access_token = None
        else:
            access_token = None
        return access_token

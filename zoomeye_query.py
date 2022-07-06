# -*- coding: utf-8 -*-
import requests
import json


class ZoomEye(object):
    def __init__(self):
        self.username = ""
        self.password = ""
        self.access_token = ""
        self.login()

    def login(self):
        data = {
            'username': self.username,
            'password': self.password
        }

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'
        }

        data_encoded = json.dumps(data)
        try:
            resp = requests.post(url='https://api.zoomeye.org/user/login', data=data_encoded, headers=headers)
            r_decoded = json.loads(resp.text)
            access_token = r_decoded['access_token']
            self.access_token = access_token
        except:
            print('[-] 错误信息 : 用户名或密码错误，请重试 ')
            exit()

    def search(self):

        if not self.access_token:
            self.login()
        headers = {
            'Authorization': 'JWT ' + self.access_token,
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'
        }
        query = input('\033[32m[o][*] 输入zoomeye搜索语句 : \033[0m')
        save_query_target = input('\033[32m[o][*] 输入保存结果的文件名 : \033[0m').encode('utf-8')
        page = int(input('\033[32m[o][*] 请输入起始页 : \033[0m'))
        num = int(input('\033[32m[o][*] 请输入您要检索的页数 : \033[0m'))
        index = 0
        while True:
            try:
                if index == num:
                    break
                msg = '\033[32m[o][{}/{}] 正在获取第{}页...\033[0m'.format(index+1, num, page)
                print(msg)
                api = 'https://api.zoomeye.org/host/search'
                print('query==>', query)
                page += 1
                index += 1
                resp = requests.get(api, headers=headers, params={"query": query, "page": page})
                r_decoded = json.loads(resp.text)
                for x in r_decoded['matches']:
                    print(x['ip'], ':', x['portinfo']['port'])
                    with open(save_query_target,'a') as fw:
                        fw.write(x['ip'] + ':' + str(x['portinfo']['port'])+ '\n')

            except Exception as e:
                if str(e) == 'matches':
                    print('[-] 错误信息 : 帐户已中断，超过最大限制')
                    break
                else:
                    print('[-] 错误信息 : ', str(e))
        print("\033[32m[o]搜索完成！\033[0m")
        pass


if __name__ == '__main__':
    zoomeye = ZoomEye()
    zoomeye.search()
    pass

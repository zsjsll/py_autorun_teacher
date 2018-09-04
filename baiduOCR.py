import requests
import base64


class OCR:
    def __init__(self):
        self.client_id = ''
        self.client_secret = ''
        self.url_token = 'https://aip.baidubce.com/oauth/2.0/token'
        self.get_params = {}
        self.header = {'Content-Type': 'application/x-www-form-urlencoded'}
        self.url_OCR = r'https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic'
        self.post_params = {}
        self.post_data = {}
        self.get_token()

    # 获取access_token
    def get_token(self,
                  client_id='N0gN2j46DugZ6Gz1XD6BFPY5',
                  client_secret='Ypcy9CV3STAArfnvMeLOluYyk4FkHOwx'):
        self.get_params = {
            'grant_type': 'client_credentials',
            'client_id': client_id,
            'client_secret': client_secret
        }
        r = requests.get(
            self.url_token, params=self.get_params, headers=self.header)
        access_token = r.json()["access_token"]
        self.post_params = {"access_token": access_token}
        return self.post_params

    def get_pic_str(self,
                    url_pic='',
                    dir_pic='',
                    token='如果没有token，修改id和secret 运行get_token()来获取'):
        if dir_pic != '':
            f = open(dir_pic, 'rb')
            img = base64.b64encode(f.read())
            self.post_data = {"image": img}
        if url_pic != '':
            self.post_data = {"url": url_pic}
        token = self.post_params
        r = requests.post(
            self.url_OCR,
            params=token,
            headers=self.header,
            data=self.post_data)
        wd = r.json()
        wd = wd['words_result'][0]['words']
        print(wd)
        return wd

def main():
    print('请从外部调用本包：\
    from baiduOCR import OCR')

if __name__=='__main__':
    main()

# client_id = 'N0gN2j46DugZ6Gz1XD6BFPY5'
# client_secret = 'Ypcy9CV3STAArfnvMeLOluYyk4FkHOwx'
# url_token = 'https://aip.baidubce.com/oauth/2.0/token'
# get_params = {
#     'grant_type': 'client_credentials',
#     'client_id': client_id,
#     'client_secret': client_secret
# }
# header = {'Content-Type': 'application/x-www-form-urlencoded'}
# post_data = {
#     "url":
#     "http://5b0988e595225.cdn.sohucs.com/images/20180130/4d0a0836a3084ce287eee0dc27f3b851.jpeg"
# }

# url_OCR = r'https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic'
# r = requests.get(url_token, params=get_params, headers=header)
# access_token = r.json()["access_token"]
# print(access_token)
# post_params = {"access_token": access_token}

# r = requests.post(url_OCR, params=post_params, headers=header, data=post_data)

# print(r.url)
# print(r.text)

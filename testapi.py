import requests

url = "https://api.lolicon.app/setu?r18=1&size1200=ture/"

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}


def download_image():
    # resp = requests.get(url, stream=True)
    # from contextlib import closing
    # with closing(requests.get(url, stream=True)) as resp:
    with requests.get(url, headers=header, stream=True) as resp:
        with open('demo.jpg', 'wb') as fd:
            for chunk in resp.iter_content():
                fd.write(chunk)
    # print(resp.text)
    print(resp.request.headers)
    print(resp.status_code)


resp = requests.get(url)

print(resp.text)
import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    url = 'https://www.bilibili.com/v/popular/rank/all'
    header = {
        "authority": "api.bilibili.com",
        "method": "GET",
        "path": "/x/web-interface/ranking/v2?rid=0&type=all&web_location=333.934&w_rid=b3d19841b8dc118b83986a3a83988c7d&wts=1723442749",
        "scheme": "https",
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "zh-CN,zh;q=0.9",
        "cookie": "buvid3=E8A4C5D1-EFEA-42A9-BD1A-7556E7D1A96227214infoc; b_nut=1723442727; b_lsid=64D8D6A1_19145310A7E; bsource=search_google; _uuid=CBAB92510-7D65-102EC-2361-DD74101041735D27562infoc; enable_web_push=DISABLE; home_feed_column=5; browser_resolution=1920-963; buvid4=CDA41940-0CA1-2EF2-02FA-4E5F02B66EC528053-024081206-HmGpS1PxpWcbEaTZ6O+p9w%3D%3D; buvid_fp=09dab95c0aeb45586e95205db3fc5be0; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjM3MDE5MzUsImlhdCI6MTcyMzQ0MjY3NSwicGx0IjotMX0.Q0krzzniJkj_fkOpglZsi56sGBU4tl22nJx4eA_vQBs; bili_ticket_expires=1723701875",
        "origin": "https://www.bilibili.com",
        "priority": "u=1, i",
        "referer": "https://www.bilibili.com/v/popular/rank/all",
        "sec-ch-ua": "\"Not)A;Brand\";v=\"99\", \"Google Chrome\";v=\"127\", \"Chromium\";v=\"127\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
    }

    res = requests.get(url, headers=header)
    # res = requests.request(method="GET",url=url, header=header)
    # print(res.encoding)

    res.encoding = res.apparent_encoding
    print(res.text)

    # print(res.encoding)
    # soup = BeautifulSoup(res.content, 'html.parser')
    # title = soup.title.text
    # print(title)

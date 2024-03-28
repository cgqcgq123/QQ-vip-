import requests
import execjs
import sys

sys.path.append(".\\")
import qqmusic_play
import keyboard

cookies = {
}

headers = {
    'authority': 'u6.y.qq.com',
    'accept': 'application/json',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'pgv_pvid=4688964470; fqm_pvqid=dcaa24c6-0000-420e-8567-79af53657baa; fqm_sessionid=286a44f7-bfbb-45e3-914e-56b75b79c051; pgv_info=ssid=s3165393034; ts_uid=7023138560; skey=@GeBKNJ893; RK=ob/9wEbW9G; ptcz=cfea719b128e4f32588a313af543d5909c64a8dde8b4fe654191825208191ef4; _qpsvr_localtk=0.8155265055309324; ts_refer=cn.bing.com/; login_type=1; wxunionid=; psrf_qqrefresh_token=870A850BE0BEDCB8B4ACE53523AAB0E4; qm_keyst=Q_H_L_63k3NWT46FaaA_darb0CPZTqCUamiuaJ0R-Cytz8R0a05xduDvHPPoKSzitBBTQHtKPeDkVHkBvBhHTo; euin=ow4PNeSq7KEkNv**; qqmusic_key=Q_H_L_63k3NWT46FaaA_darb0CPZTqCUamiuaJ0R-Cytz8R0a05xduDvHPPoKSzitBBTQHtKPeDkVHkBvBhHTo; psrf_musickey_createtime=1711516592; psrf_access_token_expiresAt=1719292592; tmeLoginType=2; psrf_qqunionid=8DAFDC33788873F346194F638C99DDB0; psrf_qqaccess_token=8A4D4D7CAD23E91EB7D68CD70CDAD9C5; uin=2548795959; wxrefresh_token=; wxopenid=; music_ignore_pskey=202306271436Hn@vBj; psrf_qqopenid=624E1105EE946EC8D58F4C4E8C54C3B5; ts_last=y.qq.com/n/ryqq/search',
    'origin': 'https://y.qq.com',
    'referer': 'https://y.qq.com/',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="122", "Google Chrome";v="122"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
}
global flag

def keyPress(key):
    global flag
    if key.name == '`':
        flag = True

def getPlayUrl(list_):
    global flag, song_mid, song_id, album_id
    num = input("请输入想要下载的歌曲序号,按`键返回:")
    if flag:
        # flag = False
        # getMusicInfo()
        return
    try:
        song_mid = list_[int(num) - 1]['mid']
        song_id = list_[int(num) - 1]['id']
        album_id = list_[int(num) - 1]['album']['mid']
    except:
        print("输入格式错误,请重新输入")
        return
    print(f'已为您找到{list_[int(num) - 1]["name"]}的播放链接\n{qqmusic_play.getPlayUrl(song_mid, str(song_id), album_id)}')


def getMusicInfo():
    global flag
    song = input("请输入要查询的歌手或歌名:")
    if len(song) == 0:
        print("不能输入空值")
        getMusicInfo()
        return
    while True:
        keyboard.on_press(keyPress)
        page = input("请输入页码,按`返回:")
        if flag:
            flag = False
            getMusicInfo()
            break
        while True:
            try:
                int(page)
                break
            except:
                print("页码格式错误!!!")
                page = input("请输入页码:")
        # data = '{"comm":{"cv":4747474,"ct":24,"format":"json","inCharset":"utf-8","outCharset":"utf-8","notice":0,"platform":"yqq.json","needNewCode":1,"uin":2548795959,"g_tk_new_20200303":922992349,"g_tk":1240599962},"req_1":{"method":"DoSearchForQQMusicDesktop","module":"music.search.SearchCgiService","param":{"remoteplace":"txt.yqq.top","searchid":"57164631778091653","search_type":0,"query":"周杰伦","page_num":1,"num_per_page":10}}}'
        # data = '{"comm":{"cv":4747474,"ct":24,"format":"json","inCharset":"utf-8","outCharset":"utf-8","notice":0,"platform":"yqq.json","needNewCode":1,"uin":2548795959,"g_tk_new_20200303":922992349,"g_tk":1240599962},"req_1":{"method":"DoSearchForQQMusicDesktop","module":"music.search.SearchCgiService","param":{"remoteplace":"txt.yqq.top","searchid":"57164631778091653","search_type":0,"query":' + f'"{song}"' + ',"page_num":' + f'"{page}"' + ',"num_per_page":10}}}'
        data = '{"comm":{"g_tk":70122919,"uin":2548795959,"format":"json","inCharset":"utf-8","outCharset":"utf-8","notice":0,"platform":"h5","needNewCode":1,"ct":23,"cv":0},"req_0":{"method":"DoSearchForQQMusicDesktop","module":"music.search.SearchCgiService","param":{"remoteplace":"txt.mqq.all","searchid":"56290893686828402","search_type":0,"query":'f'"{song}"'',"page_num":'f"{page}"',"num_per_page":20}}}'
        with open('./js/qqmusic.js', 'r', encoding='utf-8') as f:
            js_code = f.read()
        sign = execjs.compile(js_code).call('getSign', data)
        params = {
            '_': '1711516600981',
            # 'sign': sign,
            '_webcgikey': 'DoSearchForQQMusicDesktop'
        }
        print("正在检索，请稍后...")
        response = requests.post('https://u.y.qq.com/cgi-bin/musicu.fcg', params=params, cookies=cookies, headers=headers, data=data.encode())
        list_ = response.json()['req_0']['data']['body']['song']['list']
        print("共找到以下歌曲")
        index = 1
        for l in list_:
            if len(l["album"]["name"]) == 0:
                l["album"]["name"] = "无"
            print(f' {index}:--歌曲名:{l["name"]}------歌手:{l["singer"][0]["name"]}-----所属专辑:{l["album"]["name"]}')
            index += 1
        while True:
            keyboard.on_press(keyPress)
            getPlayUrl(list_)
            if flag:
                flag = False
                break



if __name__ == '__main__':
    flag = False
    print("欢迎使用QQ音乐播放链接获取软件")
    getMusicInfo()

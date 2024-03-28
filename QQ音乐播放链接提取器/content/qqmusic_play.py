import requests
import execjs

with open('.\cookies\qm_cookie', 'r', encoding='utf-8') as f:
    cookie = f.read()
split = cookie.split('&')

qm_keyst = split[0]
uin = split[1]
cookies = {
    'qm_keyst': qm_keyst,
    'uin': uin,
}

headers = {
    'authority': 'u6.y.qq.com',
    'accept': 'application/json',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'pgv_pvid=4688964470; fqm_pvqid=dcaa24c6-0000-420e-8567-79af53657baa; fqm_sessionid=286a44f7-bfbb-45e3-914e-56b75b79c051; pgv_info=ssid=s3165393034; ts_uid=7023138560; skey=@GeBKNJ893; RK=ob/9wEbW9G; ptcz=cfea719b128e4f32588a313af543d5909c64a8dde8b4fe654191825208191ef4; _qpsvr_localtk=0.8155265055309324; ts_refer=cn.bing.com/; login_type=1; wxunionid=; psrf_qqrefresh_token=870A850BE0BEDCB8B4ACE53523AAB0E4; qm_keyst=Q_H_L_63k3NWT46FaaA_darb0CPZTqCUamiuaJ0R-Cytz8R0a05xduDvHPPoKSzitBBTQHtKPeDkVHkBvBhHTo; euin=ow4PNeSq7KEkNv**; qqmusic_key=Q_H_L_63k3NWT46FaaA_darb0CPZTqCUamiuaJ0R-Cytz8R0a05xduDvHPPoKSzitBBTQHtKPeDkVHkBvBhHTo; psrf_musickey_createtime=1711516592; psrf_access_token_expiresAt=1719292592; tmeLoginType=2; psrf_qqunionid=8DAFDC33788873F346194F638C99DDB0; psrf_qqaccess_token=8A4D4D7CAD23E91EB7D68CD70CDAD9C5; uin=2548795959; wxrefresh_token=; wxopenid=; music_ignore_pskey=202306271436Hn@vBj; psrf_qqopenid=624E1105EE946EC8D58F4C4E8C54C3B5; ts_last=y.qq.com/n/ryqq/player',
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

def getPlayUrl(song_mid, song_id, albuMid):
    bofang_url = 'https://ws6.stream.qqmusic.qq.com/'
    # song_mid = '0016aXcd24qSC8'
    # song_id = '457240977'
    # albuMid = '001ln9YB420a7b'

    # data = '{"comm":{"cv":4747474,"ct":24,"format":"json","inCharset":"utf-8","outCharset":"utf-8","notice":0,"platform":"yqq.json","needNewCode":1,"uin":2548795959,"g_tk_new_20200303":922992349,"g_tk":1240599962},"req_1":{"module":"vkey.GetVkeyServer","method":"CgiGetVkey","param":{"guid":"8711062190","songmid":["0027oMO61wWi55"],"songtype":[0],"uin":"2548795959","loginflag":1,"platform":"20"}},"req_2":{"module":"music.musicasset.SongFavRead","method":"IsSongFanByMid","param":{"v_songMid":["0027oMO61wWi55"]}},"req_3":{"module":"music.musichallSong.PlayLyricInfo","method":"GetPlayLyricInfo","param":{"songMID":"0027oMO61wWi55","songID":718475}},"req_4":{"method":"GetCommentCount","module":"music.globalComment.GlobalCommentRead","param":{"request_list":[{"biz_type":1,"biz_id":"718475","biz_sub_type":0}]}},"req_5":{"module":"music.musichallAlbum.AlbumInfoServer","method":"GetAlbumDetail","param":{"albumMid":"0024bjiL2aocxT"}},"req_6":{"module":"vkey.GetVkeyServer","method":"CgiGetVkey","param":{"guid":"2894715100","songmid":["0027oMO61wWi55"],"songtype":[0],"uin":"2548795959","loginflag":1,"platform":"20"}},"req_7":{"module":"music.trackInfo.UniformRuleCtrl","method":"CgiGetTrackInfo","param":{"ids":[718475],"types":[0]}}}'
    data = '{"comm":{"cv":4747474,"ct":24,"format":"json","inCharset":"utf-8","outCharset":"utf-8","notice":0,"platform":"yqq.json","needNewCode":1,"uin":2548795959,"g_tk_new_20200303":922992349,"g_tk":1240599962},"req_1":{"module":"vkey.GetVkeyServer","method":"CgiGetVkey","param":{"guid":"8711062190","songmid":['f'"{song_mid}"''],"songtype":[0],"uin":"2548795959","loginflag":1,"platform":"20"}},"req_2":{"module":"music.musicasset.SongFavRead","method":"IsSongFanByMid","param":{"v_songMid":['f'"{song_mid}"'']}},"req_3":{"module":"music.musichallSong.PlayLyricInfo","method":"GetPlayLyricInfo","param":{"songMID":'f'"{song_mid}"'',"songID":' + song_id + '}},"req_4":{"method":"GetCommentCount","module":"music.globalComment.GlobalCommentRead","param":{"request_list":[{"biz_type":1,"biz_id":'f'"{song_id}"'',"biz_sub_type":0}]}},"req_5":{"module":"music.musichallAlbum.AlbumInfoServer","method":"GetAlbumDetail","param":{"albumMid":'f'"{albuMid}"''}},"req_6":{"module":"vkey.GetVkeyServer","method":"CgiGetVkey","param":{"guid":"2894715100","songmid":['f'"{song_mid}"''],"songtype":[0],"uin":"2548795959","loginflag":1,"platform":"20"}},"req_7":{"module":"music.trackInfo.UniformRuleCtrl","method":"CgiGetTrackInfo","param":{"ids":[' + song_id + '],"types":[0]}}}'
    with open('./js/qqmusic.js', 'r', encoding='utf-8') as f:
        js_code = f.read()
    sign = execjs.compile(js_code).call('getSign', data)
    params = {
        '_': '1711518704916',
        'sign': sign,
    }
    response = requests.post('https://u6.y.qq.com/cgi-bin/musics.fcg', params=params, cookies=cookies, headers=headers,
                             data=data)
    return bofang_url + response.json()['req_6']['data']['midurlinfo'][0]['purl']


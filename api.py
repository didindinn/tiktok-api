import requests
import json
import re

headers = {'User-Agent': 'com.ss.android.ugc.trill/584 (Linux; U; Android 5.1.1; en_US; LG-H961N;',
           'X-SS-REQ-TICKET': '1541500434739',
           'X-Tt-Token': '002447bd7d6a5c792cb223b1151e399e0402e5fdcf768ab9f96930b63dc169d353480340ec7abaa1856d8133dcfe12363b42',
           'sdk-version': '1',
           'X-SS-TC': '0',}

payload = {
    "source": "discover",
    "ts": "1556178331",
    "js_sdk_version": "",
    "app_type": "normal",
    "manifest_version_code": "583",
    "_rticket": "1556178332328",
    "app_language": "en",
    "iid": "6683055906148435713",
    "channel": "googleplay",
    "device_type": "MIX%202",
    "language": "en",
    "account_region": "VN",
    "resolution": "1080*2030",
    "openudid": "b19f5ff713b925ef",
    "update_version_code": "5830",
    "sys_region": "US",
    "os_api": "26",
    "uoo": "0",
    "is_my_cn": "0",
    "timezone_name": "Asia%2FHo_Chi_Minh",
    "dpi": "440",
    "carrier_region": "VN",
    "ac": "wifi",
    "device_id": "6620810330052445697",
    "pass-route": "1",
    "mcc_mnc": "45204",
    "os_version": "8.0.0",
    "timezone_offset": "25200",
    "version_code": "583",
    "carrier_region_v2": "452",
    "app_name": "trill",
    "ab_version": "5.8.3",
    "version_name": "5.8.3",
    "device_brand": "Xiaomi",
    "ssmix": "a",
    "pass-region": "1",
    "device_platform": "android",
    "build_number": "5.8.3",
    "region": "US",
    "aid": "1180",
    "as": "a1qwert123",
    "cp": "cbfhckdckkde1"}

class Api:
    def __init__(self):
        pass

    def get_home_page(self, username):
        try:
            home = str(requests.post("https://tikitoks.com/@" + username, data=json.dumps(payload), headers=headers).content)
        except Exception as e:
            print(e)
        return home

    def get_user_videos(self, username):
        videos = []
        home = self.get_home_page(username)
        home = str(home)
        matches = re.findall(r'http.+?"' , home)
        for match in matches:
            if "video" in match:
                match = str(match)
                match = match.replace('"', '')
                video = videos.append(match)
        
        return videos

    def get_popular_videos(self):
        videos = []
        home = str(requests.post("https://tikitoks.com/popular", data=json.dumps(payload), headers=headers).content)
        home = str(home)
        print(home)
        matches = re.findall(r'http.+?"' , home)
        for match in matches:
            if "video" in match:
                match = str(match)
                match = match.replace('"', '')
                video = videos.append(match)

    def get_likes_count(self, url):
        home = str(requests.post(url, data=json.dumps(payload), headers=headers).content)
        home = str(home)
        likes = re.findall(r'video-meta-count">.+?.Like' , home)
        likes = str(likes).replace('video-meta-count">', '')
        likes = likes.replace(" Like", "")
        likes = likes.replace("['", "")
        likes = likes.replace("']", "")
        return str(likes)

    def get_comment_count(self, url):
        home = str(requests.post(url, data=json.dumps(payload), headers=headers).content)
        home = str(home)
        likes = re.findall(r'xb7.+?.Comment' , home)
        likes = str(likes)
        likes = likes.replace("['xb7 ", "")
        likes = likes.replace("Comment']", "")
        return likes


    def get_videos_hashtags(self, url):
        pass

api = Api()

videos = api.get_user_videos("maskofshiva")

for video in videos:
    print(api.get_likes_count(video))
#print(api.get_user_videos("maskofshiva"))
#print(api.get_comment_count("https://tikitoks.com/maskofshiva/video/6771378249512635653/"))
#print(api.get_likes_count("https://tikitoks.com/maskofshiva/video/6771378249512635653/"))
#print(api.get_home_page("maskofshiva"))

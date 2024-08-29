import requests
import uuid

while True:
    try:
        UA = {"User-Agent":requests.post("https://www.bejson.com/Bejson/Api/Common/ge_nua?count=1&type=windows").json()["data"][0]}
        Rand = requests.get("https://api.jihujiasuqi.com/apps/captcha/get.php", headers=UA).json()["rand"]
        for i in range(30, 331, 30):
            if requests.get(f"https://api.jihujiasuqi.com/apps/captcha/verify.php?&rand={Rand}&angle={i}", headers=UA).json()["code"] == 0:
                print(requests.get(f"https://api.jihujiasuqi.com/api/user.php?mode=reg&mail={uuid.uuid4()}&captcha_rand="+Rand, headers=UA).json()["msg"])
                break
    except:
        pass

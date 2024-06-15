import requests
import random

while True:
    try:
        UA = {"User-Agent":requests.post("https://www.bejson.com/Bejson/Api/Common/ge_nua?count=1&type=windows").json()["data"][0]}
        Rand = requests.get("https://api.jihujiasuqi.com/apps/captcha/get.php", headers=UA).json()["rand"]
        for i in range(361):
            if requests.get("https://api.jihujiasuqi.com/apps/captcha/verify.php?&rand="+Rand+"&angle="+str(i), headers=UA).json()["code"] == 0:
                Random = ""
                for v in range(101):
                    Random = Random+chr(random.randint(97, 122))
                print(requests.get("https://api.jihujiasuqi.com/api/user.php?mode=reg&mail="+Random+"@163.com&pwd="+Random+"&captcha_rand="+Rand, headers=UA).json()["msg"])
                break
    except:
        pass
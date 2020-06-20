import urllib.request

url = "https://uta.pw/shodou/img/28//214.png"

savename = "test.png"

urllib.request.urlretrieve(url,savename)
print("保存しました")
import urllib.request

url = "https://api.aoikujira.com/ip/ini"
res = urllib.request.urlopen(url)
data = res.read()

text = data.decode("utf-8")
print(text)

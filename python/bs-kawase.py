from bs4 import BeautifulSoup
import urllib.request as req

url = "https://api.aoikujira.com/kawase/xml.usd"
res = req.urlopen(url)
soup = BeautifulSoup(res,"html.parser")

jpy = soup.select_one("jpy").string
print("usd/jpy=",jpy)
from bs4 import BeautifulSoup
import urllib.request as req

url = "https://stocks.finance.yahoo.co.jp/stocks/detail/?code=usdjpy"
res = req.urlopen(url)

soup = BeautifulSoup(res, "html.parser")

price = soup.select_one(".stoksPrice").string
print("usd/jpy=", price)

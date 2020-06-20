from bs4 import BeautifulSoup
from os import makedirs
from urllib.parse import urljoin
from urllib.parse import urlparse
from urllib.request import urlretrieve
import os.path,time,re

proc_files = {}
global startflg 
startflg = 1

def enum_links(html,base):
    soup = BeautifulSoup(html,"html.parser")
    links = soup.select("link[rel='stylesheet']")
    links += soup.select("a[href]")
    h1 = soup.select_one("div:first-child > h1>span.section-number")
    if h1 is not None:
        print("h1 =",h1.string)
    else:print ("h1 is None")
    result = []

    for a in links:
        href = a.attrs['href']
        url = urljoin(base,href)
        print("url=",url)
        result.append(url)
    return result

def download_file(url):
    print("download=",url)
    for i in url.split('/'):
        print(i)
        if i in "dtail":
            o = urlparse(url)
            savepath = "./" + o.netloc + o.path
            if re.search(r"/$",savepath):
                savepath += "index.html"
            savedir = os.path.dirname(savepath)

            if os.path.exists(savepath): return savepath

            if not os.path.exists(savedir):
                print("mkdir=", savedir)
                makedirs(savedir)
    try:
        print("download=",url)
        urlretrieve(url,savepath)
        time.sleep(1)
        return savepath
    except:
        print("ダウンロード失敗:",url)
        return None

def analize_html(url, root_url):
    savepath = download_file(url)
    if savepath is None: return
    if savepath in proc_files: return
    proc_files[savepath] = True
    print("analize_html=",url)

    html = open(savepath,"r", encoding="utf-8").read()
    links = enum_links(html,url)
    for link_url in links:
        if link_url.find(root_url) != 0:
            if not re.search(r".css$",link_url): continue
        if re.search(r".(html|htm)$", link_url):
            analize_html(link_url, root_url)
            continue
        download_file(link_url)
    
if __name__ == "__main__":
    url = "http://www.billboard-japan.com/"
    analize_html(url,url)

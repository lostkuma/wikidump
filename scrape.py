import urllib.request
import wget 
from bs4 import BeautifulSoup

link = "https://dumps.wikimedia.org/enwiki/20191001/"
req = urllib.request.urlopen(link)
soup = BeautifulSoup(req, "html.parser")

url_to_download_dump = list()
url_to_download_idx = list()

for link in soup.find_all('a'):
    link_addr = link.get('href')
    if link_addr.startswith("/enwiki/20191001/enwiki-20191001-pages-articles-multistream"):
        if link_addr.startswith("/enwiki/20191001/enwiki-20191001-pages-articles-multistream.xml."):
            continue 
        if link_addr.startswith("/enwiki/20191001/enwiki-20191001-pages-articles-multistream-index"):
            if link_addr.startswith("/enwiki/20191001/enwiki-20191001-pages-articles-multistream-index.txt"):
                continue 
            url = "https://dumps.wikimedia.org" + link_addr
            url_to_download_idx.append(url)
        else:
            url = "https://dumps.wikimedia.org" + link_addr
            if url not in url_to_download_dump:
                url_to_download_dump.append(url)

for i in range(len(url_to_download_dump)):
    print("downloading {}/57 dump files".format(i))
    wget.download(url_to_download_dump[i])
    print("{}/57 dump files complete".format(i))

for i in range(len(url_to_download_idx)):
    print("downloading {}/57 idx files".format(i))
    wget.download(url_to_download_idx[i])
    print("{}/57 idx files complete".format(i)) 
    
    
import requests
from bs4 import BeautifulSoup

def site_audit(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.title.string
    meta_desc = soup.find("meta", {"name": "description"})
    
    print(f"Site Başlığı: {title}")
    if meta_desc:
        print(f"Meta Açıklaması: {meta_desc['content']}")
    else:
        print("Meta açıklaması bulunamadı.")

site_audit("https://meritking.com")

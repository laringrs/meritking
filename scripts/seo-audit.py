import requests
from bs4 import BeautifulSoup

def site_audit(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    title = soup.title.string if soup.title else "Title Bulunamadı"
    meta_desc = soup.find("meta", {"name": "description"})
    h1_tags = [h1.text for h1 in soup.find_all("h1")]
    
    print(f"\nURL: {url}")
    print(f"Site Başlığı: {title}")
    print(f"Meta Açıklaması: {meta_desc['content'] if meta_desc else 'Bulunamadı'}")
    print(f"H1 Etiketleri: {', '.join(h1_tags)}\n")

# Test için site listesi
site_list = ["https://meritking.com", "https://rakipcasino.com"]

for site in site_list:
    site_audit(site)

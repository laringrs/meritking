import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

def site_audit(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Site Başlığı
    title = soup.title.string if soup.title else "Title Bulunamadı"
    
    # Meta Açıklaması
    meta_desc = soup.find("meta", {"name": "description"})
    meta_desc_content = meta_desc['content'] if meta_desc else "Meta Açıklaması Yok"
    
    # H1 Etiketleri
    h1_tags = [h1.text.strip() for h1 in soup.find_all("h1")]
    h1_combined = ", ".join(h1_tags) if h1_tags else "H1 Etiketi Yok"

    # Raporlama
    print(f"\nURL: {url}")
    print(f"Başlık: {title}")
    print(f"Meta Açıklaması: {meta_desc_content}")
    print(f"H1 Etiketleri: {h1_combined}")
    
    return [url, title, meta_desc_content, h1_combined]

# Sıralı Site Listesi
sites = [
    "https://meritking.com",
    "https://rakipcasino1.com",
    "https://rakipcasino2.com"
]

# Raporu CSV Dosyasına Kaydetme
today = datetime.now().strftime("%Y-%m-%d")
csv_file = f"reports/seo-audit-{today}.csv"

with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["URL", "Başlık", "Meta Açıklaması", "H1 Etiketleri"])
    
    for site in sites:
        data = site_audit(site)
        writer.writerow(data)

print(f"\nSEO raporu oluşturuldu: {csv_file}")

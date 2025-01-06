import requests
from bs4 import BeautifulSoup
import csv

def check_backlinks(site, backlink_list):
    try:
        response = requests.get(site)
        soup = BeautifulSoup(response.text, 'html.parser')
        page_text = soup.get_text().lower()
        
        found_backlinks = []
        for backlink in backlink_list:
            if backlink.lower() in page_text:
                found_backlinks.append(backlink)
        
        return found_backlinks
    except Exception as e:
        print(f"{site} için hata oluştu: {str(e)}")
        return []

# Backlink listesi
backlinks = [
    "https://meritking.com",
    "https://partnercasino.com",
    "https://otelseo.com"
]

# Hedef siteler
sites_to_check = [
    "https://casino-dunyasi.com",
    "https://rakip1.com",
    "https://rakip2.com"
]

# Raporlama
csv_file = "reports/backlink-report.csv"
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Site", "Bulunan Backlink'ler"])
    
    for site in sites_to_check:
        found = check_backlinks(site, backlinks)
        writer.writerow([site, ", ".join(found) if found else "Bulunamadı"])

print(f"Backlink raporu oluşturuldu: {csv_file}")

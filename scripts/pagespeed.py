import requests
import json
import csv
from datetime import datetime

API_KEY = "AIzaSyCcw6pBtx7vNB9EtwouRmMB_VulgZSIMNM"
sites = [
    "https://meritking.com",
    "https://rakip1.com",
    "https://rakip2.com",
    "https://rakip3.com"
]

def check_pagespeed(url):
    endpoint = f"https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={url}&key={API_KEY}"
    response = requests.get(endpoint)
    result = response.json()
    
    if 'error' in result:
        print(f"Hata oluştu: {result['error']['message']} - {url}")
        return None
    
    score = result['lighthouseResult']['categories']['performance']['score'] * 100
    print(f"{url} için PageSpeed Skoru: {score}")
    
    save_report(url, score)
    return score

def save_report(url, score):
    today = datetime.now().strftime("%Y-%m-%d")
    csv_file = f"reports/pagespeed-competitor-report-{today}.csv"
    
    with open(csv_file, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["URL", "Tarih", "Skor"])
        writer.writerow([url, today, score])
    
    print(f"Rapor kaydedildi: {csv_file}")

if __name__ == "__main__":
    for site in sites:
        check_pagespeed(site)

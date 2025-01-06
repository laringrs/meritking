import requests
from bs4 import BeautifulSoup

competitors = [
    "https://rakipcasino1.com",
    "https://rakipcasino2.com"
]

for competitor in competitors:
    response = requests.get(competitor)
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.title.string if soup.title else "Başlık Bulunamadı"
    
    print(f"{competitor} - Başlık: {title}")

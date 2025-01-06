import requests
import json

API_KEY = "YOUR_GOOGLE_PAGESPEED_API_KEY"
site_url = "https://meritking.com"

def check_pagespeed(url):
    endpoint = f"https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={url}&key={API_KEY}"
    response = requests.get(endpoint)
    result = response.json()
    
    score = result['lighthouseResult']['categories']['performance']['score'] * 100
    print(f"{url} için PageSpeed Skoru: {score}")
    return score

check_pagespeed(site_url)
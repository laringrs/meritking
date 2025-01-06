import pandas as pd
import matplotlib.pyplot as plt

def plot_pagespeed_trend(csv_file):
    df = pd.read_csv(csv_file)
    
    plt.figure(figsize=(12, 6))
    for site in df['URL'].unique():
        site_data = df[df['URL'] == site]
        plt.plot(site_data['Tarih'], site_data['Skor'], marker='o', label=site)
    
    plt.title('Rakip Site PageSpeed Skor Karşılaştırması')
    plt.xlabel('Tarih')
    plt.ylabel('Skor')
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    plt.savefig("reports/pagespeed-competitor-trend.png")
    plt.show()

# Raporu analiz et
plot_pagespeed_trend("reports/pagespeed-competitor-report-2025-01-07.csv")

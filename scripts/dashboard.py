import pandas as pd
import matplotlib.pyplot as plt
import os
from datetime import datetime

def plot_pagespeed_trend():
    # Raporun yeri
    today = datetime.now().strftime("%Y-%m-%d")
    csv_file = f"reports/pagespeed-competitor-report-{today}.csv"
    
    # CSV dosyası varsa işlem yap
    if os.path.exists(csv_file):
        # CSV'den veriyi oku
        df = pd.read_csv(csv_file)
        
        plt.figure(figsize=(12, 6))
        
        # Her site için ayrı grafik
        for site in df['URL'].unique():
            site_data = df[df['URL'] == site]
            plt.plot(site_data['Tarih'], site_data['Skor'], marker='o', label=site)
        
        # Grafiği düzenle
        plt.title('Rakip Site PageSpeed Skor Karşılaştırması')
        plt.xlabel('Tarih')
        plt.ylabel('Skor')
        plt.legend()
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.tight_layout()
        
        # Grafiği kaydet
        plt.savefig("reports/pagespeed-competitor-trend.png")
        plt.show()
        print("Dashboard oluşturuldu.")
    else:
        print("Rapor dosyası bulunamadı. Lütfen önce PageSpeed analizini çalıştırın.")

# Dashboard'u çalıştır
if __name__ == "__main__":
    plot_pagespeed_trend()

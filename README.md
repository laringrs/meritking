# MeritKing SEO Projesi
MeritKing için SEO optimizasyonu ve analiz projesi.  
- **Anahtar Kelime Takibi**  
- **Backlink Stratejileri**  
- **Site Hızı ve İçerik Analizi**  
- **Teknik SEO Araçları (Python Script)**

## Klasör Yapısı
meritking-seo │ ├── README.md ├── .gitignore ├── assets/ ├── scripts/ │ ├── seo-audit.py │ └── generate-report.py ├── data/ │ └── keyword-analysis.csv └── reports/ └── audit-report-2025.md

---
### Proje Yapısı
- **scripts/** – SEO analiz araçları (Python script)  
- **data/** – Anahtar kelime ve sıralama verileri  
- **reports/** – SEO analiz raporları (CSV ve MD formatında)  
- **.github/workflows/** – Otomasyon dosyaları  

### Nasıl Çalıştırılır?
1. `scripts/seo-audit.py` script'ini çalıştırarak SEO analizini başlatabilirsiniz.  
2. Raporlar `reports` klasöründe otomatik olarak oluşur.
3. GitHub Actions kullanarak otomatik haftalık analizler yapabilirsiniz.
## **Adım 6: GitHub Actions (Opsiyonel)**
Bu projeyi otomatikleştirmek için GitHub Actions ekleyebiliriz. Bu, her commit yapıldığında SEO script’lerinin çalışmasını sağlar.

**.github/workflows/seo-audit.yml**  
```yaml
name: SEO Audit

on:
  push:
    branches:
      - main

jobs:
  audit:
    runs-on: ubuntu-latest
    steps:
      - name: Depoyu Klonla
        uses: actions/checkout@v3
      - name: Python Kurulumu
        uses: actions/setup-python@v3
        with:
          python-version: '3.x'
      - name: Bağımlılıkları Kur
        run: pip install requests beautifulsoup4
      - name: SEO Audit Çalıştır
        run: python scripts/seo-audit.py

 **SEO Audit Script:** Web sitelerinin meta açıklamalarını ve H1 etiketlerini analiz eder.  
- **Otomatik Raporlama:** Haftalık olarak otomatik SEO raporları oluşturur.  
- **Veri Takibi:** Anahtar kelime sıralamalarını CSV formatında takip eder.  

### Otomasyon Süreci
- GitHub Actions kullanarak her Pazartesi SEO analizi yapılır ve rapor `reports` klasörüne eklenir.  
- Manuel olarak da çalıştırabilirsiniz.  

### Komutlar
```bash
python scripts/seo-audit.py


---

## **Adım 7: Projenin Geliştirilmesi**  
Bu aşamadan sonra şunları ekleyebiliriz:  
- **Backlink Takip Script'i**  
- **PageSpeed Analiz Aracı**  
- **Rakip Analizi Otomasyonu**  

Bu adımlarla MeritKing için SEO projen daha verimli ve otomatik hale gelecek. Takıldığın herhangi bir noktada buradayım!


# MeritKing SEO Projesi
MeritKing için SEO optimizasyonu ve analiz projesi.  
- **Anahtar Kelime Takibi**  
- **Backlink Stratejileri**  
- **Site Hızı ve İçerik Analizi**  
- **Teknik SEO Araçları (Python Script)**

## Klasör Yapısı
meritking-seo │ ├── README.md ├── .gitignore ├── assets/ ├── scripts/ │ ├── seo-audit.py │ └── generate-report.py ├── data/ │ └── keyword-analysis.csv └── reports/ └── audit-report-2025.md

---

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

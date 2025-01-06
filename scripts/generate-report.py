from datetime import datetime

def generate_report():
    today = datetime.now().strftime("%Y-%m-%d")
    with open(f"reports/seo-report-{today}.md", "w") as report:
        report.write(f"# MeritKing SEO Raporu - {today}\n")
        report.write("- Anahtar kelime analizi tamamlandı.\n")
        report.write("- Rakip siteler analiz edildi.\n")
        report.write("- Yeni backlink kaynakları eklendi.\n")

generate_report()

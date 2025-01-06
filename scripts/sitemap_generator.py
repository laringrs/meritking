from datetime import datetime

urls = [
    "https://meritking.com",
    "https://meritking.com/blog",
    "https://meritking.com/contact"
]

sitemap_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
sitemap_content += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'

for url in urls:
    sitemap_content += '  <url>\n'
    sitemap_content += f'    <loc>{url}</loc>\n'
    sitemap_content += f'    <lastmod>{datetime.now().strftime("%Y-%m-%d")}</lastmod>\n'
    sitemap_content += '    <priority>0.8</priority>\n'
    sitemap_content += '  </url>\n'

sitemap_content += '</urlset>'

with open("reports/sitemap.xml", "w", encoding="utf-8") as file:
    file.write(sitemap_content)
    
print("Sitemap oluşturuldu.")

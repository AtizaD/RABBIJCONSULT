import requests
from bs4 import BeautifulSoup

# List of URLs
urls = [
    "https://www.patentisuperiori.com/lista-domande/consumo-degli-pneumatici.html",
    "https://www.patentisuperiori.com/lista-domande/cunei-fermaruota.html",
    "https://www.patentisuperiori.com/lista-domande/efficienza-dello-sterzo.html",
    "https://www.patentisuperiori.com/lista-domande/garantire-la-sicurezza-della-circolazione.html",
    "https://www.patentisuperiori.com/lista-domande/instabilita-di-marcia.html",
    "https://www.patentisuperiori.com/lista-domande/intasamento-del-filtro-del-combustibil.html",
    "https://www.patentisuperiori.com/lista-domande/leggi-sull-autoriparazione-dei-veicoli.html",
    "https://www.patentisuperiori.com/lista-domande/manutenzione-del-motore.html",
    "https://www.patentisuperiori.com/lista-domande/manutenzione-del-veicolo.html",
    "https://www.patentisuperiori.com/lista-domande/manutenzione-del-veicolo-e-incidenti-stradali.html",
    "https://www.patentisuperiori.com/lista-domande/manutenzione-periodica-del-veicolo.html",
    "https://www.patentisuperiori.com/lista-domande/parabrezza-lesionati.html",
    "https://www.patentisuperiori.com/lista-domande/sostituzione-del-volante.html",
    "https://www.patentisuperiori.com/lista-domande/specchi-retrovisori.html",
    "https://www.patentisuperiori.com/lista-domande/verifica-livello-del-liquido-del-serbatoio-del-servosterzo.html",
    "https://www.patentisuperiori.com/lista-domande/verifiche-di-efficienza-del-veicolo-prima-della-partenza.html",
    "https://www.patentisuperiori.com/lista-domande/verifiche-prima-della-partenza.html",
    "https://www.patentisuperiori.com/lista-domande/verifiche-prima-della-partenza-dell-autobus.html"
]
# Initialize the variable to store the combined tbody content
combined_tbody_content = ''

for url in urls:
    # Download the HTML content
    response = requests.get(url)
    html_content = response.text

    # Parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find the table you want to scrape
    original_table = soup.find('table', {'class': 'domande'})

    if original_table:
        # Find the tbody element
        tbody = original_table.find('tbody')

        if tbody:
            # Extract the content inside the tbody
            tbody_content = str(tbody)

            # Append the tbody content to the combined_tbody_content
            combined_tbody_content += tbody_content

        else:
            print(f'No tbody found in the table with class "domande" in {url}.')
    else:
        print(f'No table with class "domande" found in {url}.')

# Write the combined tbody content to a single file
with open('scrapped_table.html', 'w') as combined_file:
    # Write the HTML structure and combined tbody content
    combined_file.write('<html><head></head><body><table class="domande" cellspacing="0"><thead><tr><td>Domanda</td><td>Risposta</td></tr></thead><tbody>')
    combined_file.write(combined_tbody_content)
    combined_file.write('</tbody></table></body></html>')

print('Table content from all URLs successfully extracted and saved in a single HTML file called "scrapped_table.html",.')

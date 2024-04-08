import requests
from bs4 import BeautifulSoup

def extract_links_from_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        links = [a['href'] for a in soup.find_all('a', href=True) if a['href'].startswith('/lista-domande/')]
        return links
    else:
        print(f"Failed to fetch content from {url}. Status code: {response.status_code}")
        return []

# Example usage with the given URLs
urls = [
    "https://www.patentisuperiori.com/quiz-patente-d/lista-domande/disposizioni-guida-riposo.html",
    "https://www.patentisuperiori.com/quiz-patente-d/lista-domande/impiego-cronotachigrafo.html",
    "https://www.patentisuperiori.com/quiz-patente-d/lista-domande/disposizioni-trasporto-cose.html",
    "https://www.patentisuperiori.com/quiz-patente-d/lista-domande/documenti-circolazione-trasporto.html",
    "https://www.patentisuperiori.com/quiz-patente-d/lista-domande/comportamento-in-caso-incidente.html",
    "https://www.patentisuperiori.com/quiz-patente-d/lista-domande/rimozione-sostituzione-ruote.html",
    "https://www.patentisuperiori.com/quiz-patente-d/lista-domande/dimensione-massa-velocita.html",
    "https://www.patentisuperiori.com/quiz-patente-d/lista-domande/limitazione-campo-visivo.html",
    "https://www.patentisuperiori.com/quiz-patente-d/lista-domande/sicurezza-caricamento-veicolo.html",
    "https://www.patentisuperiori.com/quiz-patente-d/lista-domande/rimorchi-semirimorchi.html",
    "https://www.patentisuperiori.com/quiz-patente-d/lista-domande/motori-sistemi-alimentazione.html",
    "https://www.patentisuperiori.com/quiz-patente-d/lista-domande/lubrificazione-protezione-gelo.html",
    "https://www.patentisuperiori.com/quiz-patente-d/lista-domande/pneumatici.html",
    "https://www.patentisuperiori.com/quiz-patente-d/lista-domande/freno-acceleratore.html",
    "https://www.patentisuperiori.com/quiz-patente-d/lista-domande/guasti-sospensioni-ammortizzatori.html",
    "https://www.patentisuperiori.com/quiz-patente-d/lista-domande/manutenzione-riparazioni.html"
]



output_file_path = "extracted_links.txt"

with open(output_file_path, 'w') as output_file:
    for url in urls:
        links_from_url = extract_links_from_url(url)
        output_file.write(f"Links from {url}:\n")
        output_file.write("\n".join(links_from_url) + "\n\n")

print(f"Extracted links have been saved to {output_file_path}")

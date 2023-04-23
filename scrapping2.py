import requests
from bs4 import BeautifulSoup
import csv

# Fonction pour récupérer le contenu de chaque page du formulaire
def get_page_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup

# Liste pour stocker les données filtrées
filtered_data = []

# Scraper les 10 premières pages du formulaire
for i in range(1, 11):
    url = f"https://www.scrapethissite.com/pages/forms/?page={i}"
    page_content = get_page_content(url)
    rows = page_content.find_all('tr')
    for row in rows:
        cells = row.find_all('td')
        if len(cells) >= 2 and cells[-1].text.strip().isdigit() and int(cells[-1].text.strip()) > 0 and cells[-2].text.strip().isdigit() and int(cells[-2].text.strip()) < 300:
            filtered_data.append([cell.text.strip() for cell in cells])

# Écrire les données filtrées dans un fichier CSV
with open('filtered_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Team Name', 'Year', 'Wins', 'Losses', 'Win%', 'Goals For(GF)', 'Goals Against(GA)', '+/-'])
    writer.writerows(filtered_data)

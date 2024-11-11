import requests
from bs4 import BeautifulSoup

def coletar_noticias():
    url = 'https://g1.globo.com/'  
    response = requests.get(url)
    if response.status_code != 200:
        print("Erro ao acessar a página")
        return []
    soup = BeautifulSoup(response.text, 'html.parser')
    noticias = []
    for noticia in soup.select('.feed-post-body'):
        titulo = noticia.select_one('.feed-post-link').get_text()
        link = noticia.select_one('.feed-post-link')['href']
        noticias.append({'titulo': titulo, 'link': link})
    
    return noticias

import requests;
url="https://codeavecjonathan.com/scraping/recette"

response=requests.get(url)

if response.status_code==200 :
    content=response.text
    print("Resultat -------------------")
    print(content)

print("FIN!!!!!!!!!!!")


# https://codeavecjonathan.com/scraping/recette
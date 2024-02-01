from bs4 import BeautifulSoup
import requests;
url="https://codeavecjonathan.com/scraping/recette_js"

def get_element_if_none(e):
    if e:
        return e.text.strip()
    else: return None

HEADERS={'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

response=requests.get(url,headers=HEADERS)
# change encoding to apparent_enscoding
response.encoding=response.apparent_encoding


if response.status_code==200 :
    content=response.text
    print("Resultat -------------------")
    print(content)
    # write file on file
    f=open("recette.html",'w')
    f.write(content)
    f.close()

    # Convert content to HTML format for read
    soup =BeautifulSoup(content,'html5lib')
    print("After coverted------------------------------------------")
    print("++++++++++++++++++++++++++++++++ Result ------------------------------------------")

    print(soup)
    print("++++++++++++++++++++++++++++++++ End Result ------------------------------------------")
    
    # get Description
    print("Gettinng Description------------------------------------------")
    description=get_element_if_none(soup.find("p", class_="description"))
    print("++++++++++++++++++++++++++++++++ Result Description ------------------------------------------")
    print(description)
    print("++++++++++++++++++++++++++++++++ End Description ------------------------------------------")

    # Get igrediemts
    div_ingredients=soup.find("div", class_="ingredients")
    print("++++++++++++++++++++++++++++++++ Result igrediemts ------------------------------------------")
    igredients=div_ingredients.find_all("p")
    for i in igredients:
        print(i.text)
    print("++++++++++++++++++++++++++++++++ End igrediemts ------------------------------------------")

    # Get etapes
    # soup.select(".preparation_etape") aussi possible
    etapes=soup.find_all("td", class_="preparation_etape")
    print("++++++++++++++++++++++++++++++++ Result etapes ------------------------------------------")
    for e in etapes:    
        print(e.text)
    print("++++++++++++++++++++++++++++++++ End etapes ------------------------------------------")

else:
    print("error on get page content "+str(response.status_code))

print("FIN !!!!!!!!!!!")


# https://codeavecjonathan.com/scraping/recette
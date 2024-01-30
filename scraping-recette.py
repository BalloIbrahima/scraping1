from bs4 import BeautifulSoup
import requests;
url="https://codeavecjonathan.com/scraping/recette"

response=requests.get(url)
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


else:
    print("error on get page content "+response.status_code)

print("FIN !!!!!!!!!!!")


# https://codeavecjonathan.com/scraping/recette
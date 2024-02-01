import requests;


# url="https://codeavecjonathan.com/scraping/techsport"
url="https://amazon.fr"

def get_element_if_none(e):
    if e:
        return e.text.strip()
    else: return None

HEADERS={'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
response=requests.get(url,headers=HEADERS)


if response.status_code==200 :
    content=response.text
    print("Resultat -------------------")
    print(content)
    # write file on file
    f=open("test-request.html",'w')
    f.write(content)
    f.close()

else:
    print("error on get page content "+str(response.status_code))

print("FIN !!!!!!!!!!!")


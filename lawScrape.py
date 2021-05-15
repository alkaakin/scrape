from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError


def fetchTitle():
    try:
        html=urlopen('https://data.finlex.fi/eli/sd/2021.html')
    except HTTPError as e:
        print(e)
    except URLError as e:
        print('Could not find the server :(')
    except AttributeError as e:
        print('Tag was not found')
    else:
        lista = []
        bs = BeautifulSoup(html.read(), 'html.parser')
        for link in bs.find_all('a'):
            try:
                actName = link.get_text()
                lista.append(actName)
                #print(link.get('href')) #Testing if it's possible to extract the links from the main site
                #lawHtml=urlopen(kokeilu) #the idea here is to convert the html link into string and then use that string to navigate to a subsite
                #innerSoup = BeautifulSoup(lawHtml.read(), 'html.parser')
                #print(innerSoup.title.string) 
            except ValueError as e:
                continue

    print(lista)
    with open("file.txt", "w") as output:
        output.write(str(lista))    #Saves the extracted data to a separate file

def main():
    fetchTitle()

if __name__ == "__main__":
    main()
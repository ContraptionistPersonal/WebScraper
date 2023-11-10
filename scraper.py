import requests
import re
from hashtable import ScraperHashTable
from hashtablentry import ScraperHashTableEntry


def getLinks(url):

    req = requests.get(f"https://en.wikipedia.org/{url}")
    linkArray = []

    page = req.text
    for i in range(len(page)):
        if(page[i] == "<" and page[i+1] == "a"):
            counter = i+1
            tag = ""
            while page[counter] != "<":
                tag = tag + page[counter]
                counter = counter + 1

            link = re.search('[h][r][e][f][=]["][/][w][i][k][i][/].*["][\s]',tag)
            if link != None:
                link = tag[link.start():link.end()]
                link = link.split()[0]
                link = link[:len(link)-1]
                link = link[6::]

                linkArray.append(link)

    return linkArray


if __name__ == "__main__":
    ht = ScraperHashTable(500000)
    print(ht[1])
    #rootLinks = getLinks('wiki/Wiki')
    #for i in range(len(rootLinks)):
    #    print(rootLinks[i])
    #    subLinks = getLinks(rootLinks[i])
    #    for x in range(len(subLinks)):
    #        print(f"            {subLinks[x]}",ht.addHt(subLinks[x]))

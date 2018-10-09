import requests
from html.parser import HTMLParser

links = []
nextpages = []
startpagename = " "

class HtmlF(HTMLParser):

    def handle_starttag(self, tag, attrs):

        if(tag == "img"):
            for attr in attrs:
                if(attr[0] == "src" and (not(attr[1] in links))):
                    if checklink(attr[1] != "0"):
                        links.append(checklink(attr[1]))
        else:
            for attr in attrs:
                if(attr[0] == "href"):
                    if not attr[1] in nextpages and (attr[1][-4:] == ".php" or attr[1][-5:] == ".html"):
                        if checklink(attr[1]) != "0":
                            nextpages.append(checklink(attr[1]))

def checklink(url):
    if url[:2] == "./":
        return startpagename + url[1:]
    elif url[0] == "/":
        return startpagename + url
    elif url.split("/")[0] == startpagename.split("/")[-1]:
        return startpagename + url[url.index("/")+1:]
    elif url.split("/")[2] == startpagename.split("/")[-1]:
        return url
    else:
        return "0"   

def findimages(url):
    if url.split("/")[0] == "http" or url.split("/")[0] == "https":
        startpagename = url.split("/")[0] + "//" + url.split("/")[2]
    nextpages.append(startpagename)
    i = -1
    a = 0
    r = requests.get(startpagename)
    print("Program is starting checking page/s")
    print("Current Page: " + startpagename)
    while True:
        i = i + 1
        if(i != 0):
            r = requests.get(startpagename + nextpages[i][1:])
            print("Current Page: " + startpagename + nextpages[i][1:])
        parser = HtmlF()
        parser.feed(r.text)
        if(i == len(nextpages) - 1):
            break
        else:
            print("Changing page...")
    print("Checked all pages")
    print("Starting downloading files...")
    for x in links:
        print("Downloading: " + x.split("/")[-1].split(".")[0])
        fulllink = url + x[1:]
        a = a + 1
        f = open("image" + str(a) + x[len(x) - 4:], "wb")
        f.write(requests.get(fulllink).content)
        f.close()

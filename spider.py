import requests
from html.parser import HTMLParser

links = []
nextpages = []


class HtmlF(HTMLParser):

    def handle_starttag(self, tag, attrs):

        if(tag == "img"):
            for attr in attrs:
                if(attr[0] == "src" and attr[1][:2] == './' and (not(attr[1] in links))):
                    links.append(attr[1])
        else:
            for attr in attrs:
                if(attr[0] == "href" and attr[1][:2] == './'):
                    if((not(attr[1] in nextpages)) and (attr[1][-4:] == '.php' or attr[1][-5:] == '.html')):
                        nextpages.append(attr[1])


def filename(lin):
    ftf = 0
    ptf = 0
    x = -1
    for i in lin:
        x = x + 1
        if(i == '/'):
            ftf = x + 1
        elif(i == '.'):
            ptf = x
    return lin[ftf:ptf]


def findimages(url):
    nextpages.append(url)
    i = -1
    a = 0
    r = requests.get(url)
    print("Program is starting checking page/s")
    print("Current Page: " + url)
    while True:
        i = i + 1
        if(i != 0):
            r = requests.get(url + nextpages[i][1:])
            print("Current Page: " + url + nextpages[i][1:])
        parser = HtmlF()
        parser.feed(r.text)
        if(i == len(nextpages) - 1):
            break
        else:
            print("Changing page...")
    print("Checked all pages")
    print("Starting downloading files...")
    for x in links:
        print("Downloading: " + filename(x))
        fulllink = url + x[1:]
        a = a + 1
        f = open('image' + str(a) + x[len(x) - 4:], 'wb')
        f.write(requests.get(fulllink).content)
        f.close()

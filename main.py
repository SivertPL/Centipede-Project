#!/usr/bin/python3
import messages
import spider.spider as spdr 


def main():
    messages.info("spider test")
    spdr.findimages("http://page.art.pl")
    

if __name__ == "__main__":
    main()
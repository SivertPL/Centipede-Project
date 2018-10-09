#!/usr/bin/python3
import messages
import spider.spider

"""
    Plan projektu:

        1. Spider 
        - Pająk który zbiera wszystkie pliki ze strony:
        docx na początek
        2. Analyzer
        - Analizuje zebrane pliki i wyciaga z nich metadane


        Na razie tylko format .docx

"""

def main():
    messages.info("Test info by sebix")
    messages.warning("Test warning by sebix")
    messages.error("TEST error by sebix")
    spider.spider.findimages("http://page.art.pl")
    


if __name__ == "__main__":
    main()
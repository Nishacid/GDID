#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Python Version    : 3.X
# Author            : Nishacid

import requests
import argparse
import re

if __name__ == "__main__":

    # Arguments CLI
    parser = argparse.ArgumentParser(description="Google Dorks for Information Disclosure")
    parser.add_argument("-c", dest="company", help="Company to check", required=True)
    args = parser.parse_args()
    company = args.company

    def search(company):
        
        # define websites
        sites = [
            "github.com",
            "gitlab.com",
            "codepen.io",
            "trello.com", 
            "prezi.com", 
            "codepad.co", 
            "pastebin.com",
            "scribd.com", 
            "npmjs.com", 
            "npm.runkit.com", 
            "libraries.io", 
            "ycombinator.com", 
            "coggle.it", 
            "papaly.com", 
            "jsdelivr.net",
            "codeshare.io",
            "sharecode.io",
            "repl.it",
            "productforums.google.com",
            "google.com",
            "gitter.im",
            "bitbucket.org",
            "*.atlassian.net"
            ]
                        
        for url in sites:
            try:
                
                headers = {
                    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0",
                    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8 ",
                    'DNT' : '1'}
                
                req = requests.get(f"https://www.google.com/search?q=site:http://{url}%20%22{company}%22&hl=en", headers=headers).text
                pattern = re.compile("/span> \- (.*?)\.</p><p")
                
                if pattern.search(req):
                    pass
                else:
                    print(f"[+] Possible result found for {url} : https://google.com/search?q=site:http://{url}%20%22{company}%22")  
            except requests.ConnectionError:
                print("[-] Error, couldn't connect")

            except requests.Timeout:
                print("[-] Error, request time out.")
                
    search(company)

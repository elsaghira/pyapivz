#!/usr/bin/python3


import requests

import pprint

def main():
    r = requests.get("https://anapioficeandfire.com/api")
    pprint.pprint(r.json())

main()


#!/usr/bin/pythin3

import yaml


def main():
    hitchhikers = [{"name": "zaphod beeblebros", "species": "betelgeusian"}, {"name": "author dent", "species": "human"}, {"name": "ford perfict", "species":None}]


    mystr = yaml.dump(hitchhikers)

    print(mystr)
  


main()



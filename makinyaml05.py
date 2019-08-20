#!/usr/bin/pythin3

import yaml


def main():
    hitchhikers = [{"name": "zaphod beeblebros", "species": "betelgeusian"}, {"name": "author dent", "species": "human"}, {"name": "ford perfict", "species":None}]


    with open("zfile.yml", "w") as zfile:
        yaml.dump(hitchhikers, zfile)
  


main()



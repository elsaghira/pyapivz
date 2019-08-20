#!/usr/bin/pythin3

import json


def main():
    hitchhikers = [{"name": "zaphod beeblebros", "species": "betelgeusian"}, {"name": "author dent", "species": "human"}, {"name": "ford perfict", "species":None}]



    with open("galaxyguide.json", "w") as zfile:
        json.dump(hitchhikers, zfile)

    myhitchhikers = json.dumps(hitchhikers)

    print(myhitchhikers)


main()



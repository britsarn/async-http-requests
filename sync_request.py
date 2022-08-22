#!/usr/bin/env python3

import httpx
import time


def main():

    start_time = time.time()
    client = httpx.Client()

    for number in range(1, 151):
        url = f"https://pokeapi.co/api/v2/pokemon/{number}"
        resp = client.get(url)
        pokemon = resp.json()
        print(pokemon["name"])

    print(f"--- {time.time() - start_time} seconds ---")


if __name__ == "__main__":
    main()

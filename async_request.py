#!/usr/bin/env python3

import asyncio
import httpx
import time


start_time = time.time()


async def get_pokemon(client, url):
    resp = await client.get(url)
    pokemon = resp.json()
    return pokemon


async def main():

    async with httpx.AsyncClient() as client:

        tasks: list = []
        for number in range(1, 151):
            url: str = f"https://pokeapi.co/api/v2/pokemon/{number}"
            tasks.append(asyncio.ensure_future(get_pokemon(client, url)))

        original_pokemon = await asyncio.gather(*tasks)
        for pokemon in original_pokemon:
            print(pokemon["name"])


if __name__ == "__main__":
    asyncio.run(main())

print(f"--- {time.time() - start_time} seconds ---")

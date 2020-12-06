import aiohttp
import asyncio
from concurrent.futures import ALL_COMPLETED


async def fetch(client, service):
    async with client.get(service) as resp:
        return await resp.text()


async def asynchronous(n):
    async with aiohttp.ClientSession() as client:
        a = await asyncio.wait({fetch(client, 'http://127.0.0.1:8000') for i in range(n)}, return_when=ALL_COMPLETED)
        for i in a[0]:
            print(i.result())
        print('done')


lol = asyncio.get_event_loop()
lol.run_until_complete(asynchronous(100))
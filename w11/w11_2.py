from collections import namedtuple
import time
import asyncio
from concurrent.futures import FIRST_COMPLETED
import aiohttp

Service = namedtuple('Service', ('name', 'url', 'ip_attr'))

SERVICES = (
    Service('ipify', 'https://api.ipify.org?format=json', 'ip'),
    Service('ip-api', 'http://ip-api.com/json', 'query')
)


async def fetch_ip(client, service):
    # получение ip
    async with client.get(service.url) as resp:
        return await resp.json()


async def asynchronous():
    # создание футур для сервисов
    # используйте FIRST_COMPLETED
    async with aiohttp.ClientSession() as client:
        fut = await asyncio.wait({fetch_ip(client, service) for service in SERVICES}, return_when=FIRST_COMPLETED)
        for i in fut[0]:
            answer = i.result()
            for service in SERVICES:
                try:
                    print(answer[service.ip_attr])
                except:
                    pass


ioloop = asyncio.get_event_loop()
ioloop.run_until_complete(asynchronous())


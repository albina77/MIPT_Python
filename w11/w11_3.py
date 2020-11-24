import aiofile
import aiohttp
import asyncio
import re


async def fetch(client, service):
    async with client.get(service) as resp:
        a = resp.text()
        a = re.split(r'[\r\n]', a)  # делим текст на строки
        for line in a:
            if line.startswith('<a >'):  # если строка соответствует данному в задаче шаблону -
                async with aiofile.async_open('found.txt', 'w') as found:  # записываем её в файл
                    found.write('Next special line has sent from {}. Look at this: {} \n'.format(service, line))


async def asynchronous(name_file):
    async with aiofile.async_open(name_file, 'r') as ai_as_o:  # открываем файл urls.txt
        async for line in aiofile.LineReader(ai_as_o):  # считываем веб-ссылки построчно
            async with aiohttp.ClientSession() as client:
                asyncio.ensure_future(fetch(client, line))
        print('done')


lol = asyncio.get_event_loop()
lol.run_until_complete(asynchronous('urls.txt'))

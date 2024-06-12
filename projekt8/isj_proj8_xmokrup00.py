#!/usr/bin/env python3
import asyncio
import aiohttp

async def fetch_url(url):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                await response.text()
                return response.status
    except Exception as error:
        return error.__class__.__name__

async def get_urls(urls):
    tasks = [fetch_url(url) for url in urls]
    responses = await asyncio.gather(*tasks)
    return list(tuple(zip(responses, urls)))


# if __name__ == '__main__':

#     urls = ['https://www.fit.vutbr.cz','https://www.szn.cz',  'https://www.alza.cz', 'https://office.com', 'https://aukro.cz']

#     # asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
#     res = asyncio.run(get_urls(urls))

#     print(res)
import asyncio
import logging

from base import consts
from instance import KufarApi
from utils.requester import Requester
from utils.state import State

logging.basicConfig(level=logging.DEBUG)


async def main():
    state = State('state.conf')

    async with Requester(consts.BASE_HEADERS) as client:
        api = KufarApi(client, state)
        await api.init()
        # await api.authenticate("email", "password")
        ads_count = await api.user_ads.get_my_ads_count()
        print(ads_count)


if __name__ == "__main__":
    asyncio.run(main())

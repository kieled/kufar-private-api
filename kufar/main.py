import asyncio

from _instance import KufarApi
from utils.requester import Requester
from utils.state import State



async def main():
    state = State('state.conf')

    async with Requester() as client:
        api = KufarApi(client, state)
        await api.init()
        await api.authenticate("email", "password")
        ads_count = await api.user_ads.get_my_ads_count()

        # Get Current Account Info
        current_account = await api.account.get_current_account()

        # Get Saved Searches
        saved_searches = await api.saved.get_searches(current_account.account.account_id)

        # Get unread messages count
        messages_unread_count = await api.messaging.unread_count()
        
        # Get all categories
        categories = await api.categories.get_categories()
        


if __name__ == "__main__":
    asyncio.run(main())

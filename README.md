# Kufar Private API

This library is result of researching around Kufar Mobile App. Project is still development. But you can use it now.

### Installing:
You can install this library using command:
```bash
pip install kufar 
```

### Example:
```python
from kufar import KufarAPI, State, Requster
import asyncio

async def main():
    state = State('state.conf')

    async with Requester() as client:
        api = KufarApi(client, state)
        await api.init()
        await api.authenticate("email", "password")

        # Get current account ads count
        ads_count = await api.user_ads.get_my_ads_count()
        print(ads_count)

        # Get Current Account Info
        current_account = await api.account.get_current_account()

        # Get Saved Searches
        saved_searches = await api.saved.get_searches(current_account.account.account_id)

        # Get unread messages count
        messages_unread_count = await api.messaging.unread_count()
        
        # Get all categories
        categories = await api.categories.get_categories()
 


asyncio.run(main())
```
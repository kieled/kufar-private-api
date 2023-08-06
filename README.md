# Kufar Private API

This library is result of researching around Kufar Mobile App. Project is still development. But you can use it now.

### :recycle: Requirements

- Python 3.10+

### :pill: Usage

1. Install library using pip (or another package manager):

```bash
pip install kufar
```

2. Import nessesary classes:

```python
from kufar import KufarAPI, State, Requster
```

3. Create state, and open Request context manager:

```python
async def test():
    state = State('here you should specify path to the file that will store your state')

    async with Requster() as client:
        api = KufarAPI(client, state)

        # !!! Required step !!!
        await api.init()

        # Here you can call any methods what you want
        api.authenticate("kufar_email@gmail.com", "kufar_password")
        print(await api.user_ads.get_my_ads_count())

```

### What you make with this library

```python
# Authenticate and save tokens in the your state and file that you specified
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
```

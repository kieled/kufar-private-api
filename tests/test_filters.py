from kufar import State, KufarApi, Requester
import pytest

from kufar.schemas import MetadataResponse


@pytest.mark.asyncio
async def test_filters():
    state = State("state.conf")

    async with Requester() as req:
        api = KufarApi(req, state)

        await api.init()

        base_filters = await api.filters.get_base_filters()
        assert isinstance(base_filters, MetadataResponse)

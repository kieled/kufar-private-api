from base import consts
from packages import (
    AccountService,
    AdsService,
    AuthService,
    CategoryService,
    LogInPayload,
    MessagingService,
    SavedService,
    UserAdsService,
)
from utils.requester import Requester
from utils.state import State


class KufarApi:
    __inited: bool = False

    _client: Requester

    account: AccountService
    ads: AdsService
    auth: AuthService
    categories: CategoryService
    saved: SavedService
    user_ads: UserAdsService
    messaging: MessagingService

    state: State

    def __init__(self, client: Requester, state: State):
        self._client = client

        self.state = state

        self.ads = AdsService(self._client, consts.API_URL)
        self.auth = AuthService(self._client, consts.CRE_API_URL)
        self.categories = CategoryService(self._client, consts.API_URL)
        self.saved = SavedService(self._client, consts.API_URL)
        self.user_ads = UserAdsService(self._client, consts.BAPI_URL)
        self.account = AccountService(self._client, consts.API_URL)
        self.messaging = MessagingService(self._client, consts.API_URL)

    def _load_tokens_from_state(self):
        if self.state.access_token is not None:
            self._client.patch_headers({
                "authorization": f"Bearer {self.state.access_token}",
                "session-id": str(self.state.session_id),
            })

    async def init(self):
        if self.__inited:
            return
        await self.state.load()
        self._load_tokens_from_state()
        self.__inited = True

    async def authenticate(self, email: str, password: str):
        if (await self.auth.is_login_captcha_required()).is_required:
            raise Exception("Captcha required")
        tokens = await self.auth.login(LogInPayload(login=email, password=password))
        if tokens:
            self.state.access_token = tokens.jwt
            self.state.session_id = tokens.session_id
            await self.state.save()
            self._load_tokens_from_state()

from kufar.base import BaseService
from kufar.utils.auth import auth_required

from . import consts
from .schemas import (
    ChangePasswordPayload,
    HistoryResponse,
    IsCaptchaRequiredResponse,
    LogInPayload,
    LogInResponse,
    RequestSmsCodeResponse,
    ResetPasswordPayload,
    ResetPasswordRequestPayload,
    SignUpPayload,
    VerifySmsCodePayload,
)


class AuthService(BaseService):
    async def login(self, payload: LogInPayload) -> LogInResponse:
        return await self.client.post(
            consts.LOG_IN,
            {
                **payload.model_dump(exclude_none=True),
                "captcha_platform": "android",
                "captcha_type": "recaptcha",
                "captcha_secret_version": "v1",
            },
            params={"token_type": "user"},
        )

    async def login_apple(self, token: str, full_name: str) -> LogInResponse:
        return await self.client.post(
            consts.LOG_IN_APPLE, {"token": token, "full_name": full_name}
        )

    async def login_google(self, token: str) -> LogInResponse:
        return await self.client.post(consts.LOG_IN_GOOGLE, {"token": token})

    async def login_mail_ru(self, token: str) -> LogInResponse:
        return await self.client.post(consts.LOG_IN_MAIL_RU, {"token": token})

    async def login_yandex(self, token: str) -> LogInResponse:
        return await self.client.post(consts.LOG_IN_YANDEX, {"token": token})

    @auth_required
    async def logout(self) -> None:
        return await self.client.get(consts.LOG_OUT)

    @auth_required
    async def logout_all(self) -> None:
        return await self.client.get(consts.LOG_OUT_ALL)

    async def change_password(self, payload: ChangePasswordPayload) -> any:
        return await self.client.post(consts.CHANGE_PASSWORD, payload.model_dump())

    async def create_account(self, payload: SignUpPayload) -> any:
        return await self.client.post(consts.CREATE_ACCOUNT, payload.model_dump())

    async def is_login_captcha_required(self) -> IsCaptchaRequiredResponse:
        return await self.client.get(consts.IS_LOGIN_CAPTCHA_REQUIRED)

    @auth_required
    async def login_history(self, cursor: str | None = None) -> HistoryResponse:
        return await self.client.get(consts.LOGIN_HISTORY, params={"cursor": cursor})

    async def reset_password(self, payload: ResetPasswordPayload) -> any:
        return await self.client.post(consts.RESET_PASSWORD, payload.model_dump())

    async def reset_password_request(self, payload: ResetPasswordRequestPayload) -> any:
        return await self.client.post(
            consts.RESET_PASSWORD_REQUEST, payload.model_dump()
        )

    async def request_sms_code(self, phone: str) -> RequestSmsCodeResponse:
        return await self.client.get(consts.REQUEST_SMS_CODE, params={"phone": phone})

    async def verify_sms_code(self, payload: VerifySmsCodePayload) -> LogInResponse:
        return await self.client.post(consts.VERIFY_SMS_CODE, payload.model_dump())

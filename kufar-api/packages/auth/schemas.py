from pydantic import BaseModel, Field
from typing import Literal

__all__ = [
    'Session',
    'LogInResponse',
    'LogInPayload',
    'ChangePasswordPayload',
    'HistoryResponse',
    'IsCaptchaRequiredResponse',
    'RequestSmsCodeResponse',
    'ResetPasswordPayload',
    'ResetPasswordRequestPayload',
    'SignUpPayload',
    'VerifySmsCodePayload'
]


class LogInPayload(BaseModel):
    login: str
    password: str
    captcha_user_response: str | None = None


class LogInResponse(BaseModel):
    session_id: str = Field(validation_alias='session-id')
    jwt: str


class ChangePasswordPayload(BaseModel):
    email: str
    current_password: str
    password: str


class SignUpPayload(BaseModel):
    email: str
    password: str
    password_confirm: str
    company_ad: bool
    captcha_user_response: str
    captcha_platform: Literal['android']
    gdpr_confirm: bool


class IsCaptchaRequiredResponse(BaseModel):
    is_required: bool


class Session(BaseModel):
    is_active: bool
    created_at: str
    city_name: str
    country_name: str
    country_code: str
    client_ip: str
    user_agent: str
    device_type: str


class HistoryResponse(BaseModel):
    history: list[Session]


class ResetPasswordPayload(BaseModel):
    password: str
    password_confirm: str
    activation_code: str


class ResetPasswordRequestPayload(BaseModel):
    email: str


class RequestSmsCodeResponse(BaseModel):
    code_token: str


class VerifySmsCodePayload(BaseModel):
    code_token: str
    code: str

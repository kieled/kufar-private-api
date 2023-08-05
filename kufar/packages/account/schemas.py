from datetime import datetime

from pydantic import BaseModel

__all__ = [
    'Account',
    'GetCurrentAccountResponse',
    'Profile'
]


class Account(BaseModel):
    account_id: int
    email: str
    created_at: datetime
    phone: str
    verified_phone: bool


class ProfileParams(BaseModel):
    company_ad: int
    date_of_birth: datetime | None = None
    gdpr_confirm: int
    gdpr_confirm_date: datetime
    gdpr_confirm_version: int
    gender: str | None = None
    name: str
    origin: str
    phone_hidden: int
    profile_image: str


class ProfileReputationFeedback(BaseModel):
    overallScore: int
    receivedCount: int


class ProfileReputation(BaseModel):
    feedback: ProfileReputationFeedback


class ProfileBase(BaseModel):
    reputation: ProfileReputation


class ProfileFollowings(BaseModel):
    followers: int
    followings: int


class Profile(BaseModel):
    params: ProfileParams
    profile: ProfileBase
    followings: ProfileFollowings


class GetCurrentAccountResponse(BaseModel):
    account: Account
    profile: Profile

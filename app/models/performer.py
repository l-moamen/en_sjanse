from pydantic import BaseModel
from typing import Optional, List


class Equipment(BaseModel):
    instruments: Optional[List[str]] = None
    soundSystem: Optional[str] = None
    lightSystem: Optional[str] = None


class ContactInfo(BaseModel):
    email: str
    main_phone: str
    extra_phone: Optional[str] = None


class Socials(BaseModel):
    last_fm: Optional[str] = None
    spotify: Optional[str] = None
    snap_chat: Optional[str] = None
    instagram: Optional[str] = None
    tiktok: Optional[str] = None
    others: Optional[List[str]] = None


class Performer(BaseModel):
    id: Optional[int] = -1
    display_name: str
    name: Optional[str] = None
    city: Optional[str] = None
    country: Optional[str] = None
    description: Optional[str] = None
    address: Optional[str] = None
    pictures: Optional[List[str]] = None
    equipment: Optional[Equipment] = None
    covered_genres: Optional[List[str]] = None
    contact_info: Optional[ContactInfo] = None
    socials: Optional[Socials] = None  # This is Optional


class PerformerUpdate(BaseModel):
    display_name: Optional[str] = None
    name: Optional[str] = None
    city: Optional[str] = None
    country: Optional[str] = None
    description: Optional[str] = None
    address: Optional[str] = None
    pictures: Optional[List[str]] = None
    equipment: Optional[Equipment] = None
    covered_genres: Optional[List[str]] = None
    contact_info: Optional[ContactInfo] = None
    socials: Optional[Socials] = None  # This is Optional

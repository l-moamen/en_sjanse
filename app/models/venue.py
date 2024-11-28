from pydantic import BaseModel
from typing import Optional, List


class Specs(BaseModel):
    soundSystem: Optional[str] = None
    lightSystem: Optional[str] = None
    capacity: Optional[int] = None


class Preferences(BaseModel):
    genre: Optional[str] = None
    theme: Optional[str] = None


class Venue(BaseModel):
    id: Optional[int] = -1
    name: str
    city: str
    country: str
    description: Optional[str] = None
    address: Optional[str] = None
    pictures: Optional[List[str]] = None
    specs: Optional[Specs] = None
    preferences: Optional[List[Preferences]] = None


# For update to save on payload
class VenueUpdate(BaseModel):
    name: Optional[str] = None
    city: Optional[str] = None
    country: Optional[str] = None
    description: Optional[str] = None
    address: Optional[str] = None
    pictures: Optional[List[str]] = None
    specs: Optional[Specs] = None
    preferences: Optional[List[Preferences]] = None

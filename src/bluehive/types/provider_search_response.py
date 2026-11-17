# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "ProviderSearchResponse",
    "ProviderAddress",
    "ProviderPhoneNumber",
    "ProviderLoc",
    "ProviderService",
    "Provider",
]


class ProviderAddress(BaseModel):
    city: Optional[str] = None

    country: Optional[str] = None

    county: Optional[str] = None

    postal_code: Optional[str] = FieldInfo(alias="postalCode", default=None)

    state: Optional[str] = None

    street1: Optional[str] = None

    street2: Optional[str] = None


class ProviderPhoneNumber(BaseModel):
    number: Optional[str] = None

    type: Optional[str] = None


class ProviderLoc(BaseModel):
    coordinates: Optional[List[float]] = None

    type: Optional[str] = None


class ProviderService(BaseModel):
    name: Optional[str] = None

    price: Optional[float] = None

    service_id: Optional[str] = FieldInfo(alias="serviceId", default=None)

    slug: Optional[str] = None


class Provider(BaseModel):
    id: Optional[str] = FieldInfo(alias="_id", default=None)

    address: Optional[ProviderAddress] = None

    distance: Optional[float] = None
    """Distance from zipcode in miles"""

    email: Optional[str] = None

    loc: Optional[ProviderLoc] = None

    logo_url: Optional[str] = FieldInfo(alias="logoURL", default=None)

    name: Optional[str] = None

    phone_numbers: Optional[List[ProviderPhoneNumber]] = None

    services: Optional[List[ProviderService]] = None

    slug: Optional[str] = None

    url: Optional[str] = None


class ProviderSearchResponse(BaseModel):
    count: float

    providers: List[Provider]

    radius: float

    status: str

    zipcode: str

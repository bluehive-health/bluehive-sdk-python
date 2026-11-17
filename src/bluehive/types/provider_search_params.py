# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ProviderSearchParams"]


class ProviderSearchParams(TypedDict, total=False):
    zipcode: Required[str]
    """US postal code to search near (5-digit or ZIP+4 format)"""

    brand_id: Annotated[str, PropertyInfo(alias="brandId")]
    """Brand ID to filter services by brand (optional)"""

    employer_id: Annotated[str, PropertyInfo(alias="employerId")]
    """Employer ID for employer-specific pricing (optional)"""

    limit: str
    """Maximum number of providers to return (default: 50, max: 200)"""

    provider_id: Annotated[str, PropertyInfo(alias="providerId")]
    """Comma-separated provider IDs to restrict results to (optional)"""

    radius: str
    """Search radius in miles (default: 25, max: 100)"""

    services: str
    """Comma-separated service IDs to filter by (optional)"""

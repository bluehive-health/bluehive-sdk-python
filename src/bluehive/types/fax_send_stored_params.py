# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["FaxSendStoredParams"]


class FaxSendStoredParams(TypedDict, total=False):
    to: Required[str]
    """Recipient fax number (E.164 format preferred)"""

    from_: Annotated[str, PropertyInfo(alias="from")]
    """Sender fax number (optional, uses default if not provided)"""

    subject: str
    """Subject line for the fax"""

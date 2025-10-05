# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["Hl7ProcessParams"]


class Hl7ProcessParams(TypedDict, total=False):
    f: str
    """Form field (legacy support)"""

    interface: str
    """Interface identifier (legacy support)"""

    login_passwd: str
    """Login password (legacy support)"""

    login_user: str
    """Login user (legacy support)"""

    message: str
    """HL7 message content - the primary way to send HL7 data"""

    message_b64: str
    """Base64 encoded HL7 message (legacy support)"""

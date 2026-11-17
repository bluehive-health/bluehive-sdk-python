# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["Hl7ReplayParams"]


class Hl7ReplayParams(TypedDict, total=False):
    destination: Dict[str, object]
    """
    Destination configuration for sending the message. If not provided, uses the original destination from the log.
    """

    interface_name: Annotated[str, PropertyInfo(alias="interfaceName")]
    """Interface name to use in the request (default: bluehiveadt)"""

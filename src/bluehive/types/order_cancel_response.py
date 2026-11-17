# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["OrderCancelResponse"]


class OrderCancelResponse(BaseModel):
    message: Optional[str] = None

    success: Literal[True]

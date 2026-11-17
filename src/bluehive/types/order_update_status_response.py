# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["OrderUpdateStatusResponse"]


class OrderUpdateStatusResponse(BaseModel):
    message: Optional[str] = None

    success: Optional[bool] = None

# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["FaxSendStoredResponse"]


class FaxSendStoredResponse(BaseModel):
    created_at: str = FieldInfo(alias="createdAt")
    """ISO timestamp when fax was created"""

    estimated_delivery: Optional[str] = FieldInfo(alias="estimatedDelivery", default=None)
    """Estimated delivery time (ISO timestamp)"""

    from_: str = FieldInfo(alias="from")
    """Sender fax number"""

    id: str
    """Unique fax identifier"""

    provider: str
    """Provider used to send the fax"""

    status: Literal["queued", "dialing", "sending", "delivered", "failed", "cancelled", "retrying"]
    """Current fax status"""

    to: str
    """Recipient fax number"""

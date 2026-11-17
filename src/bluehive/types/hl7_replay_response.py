# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Hl7ReplayResponse"]


class Hl7ReplayResponse(BaseModel):
    """Result of the replayed HL7 message send"""

    acknowledgment: Optional[str] = None

    duration: Optional[float] = None

    message_id: Optional[str] = FieldInfo(alias="messageId", default=None)

    new_log_timestamp: Optional[str] = FieldInfo(alias="newLogTimestamp", default=None)

    original_log_id: Optional[str] = FieldInfo(alias="originalLogId", default=None)

    retry_count: Optional[float] = FieldInfo(alias="retryCount", default=None)

    success: Optional[bool] = None

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["OrderUploadResultsResponse"]


class OrderUploadResultsResponse(BaseModel):
    file_ids: Optional[List[str]] = FieldInfo(alias="fileIds", default=None)

    message: Optional[str] = None

    success: Optional[bool] = None

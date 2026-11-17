# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["OrderSearchItemsParams"]


class OrderSearchItemsParams(TypedDict, total=False):
    employee_id: Annotated[str, PropertyInfo(alias="employeeId")]
    """Filter by exact employee ID"""

    employee_id_contains: Annotated[str, PropertyInfo(alias="employeeIdContains")]
    """Filter by employee ID containing this value (case-insensitive)"""

    employer_id: Annotated[str, PropertyInfo(alias="employerId")]
    """Filter by exact employer ID"""

    id: str
    """Filter by exact document ID (_id)"""

    id_contains: Annotated[str, PropertyInfo(alias="idContains")]
    """Filter by document ID containing this value (case-insensitive)"""

    order_access_code: Annotated[str, PropertyInfo(alias="orderAccessCode")]
    """Filter by exact order access code"""

    order_access_code_contains: Annotated[str, PropertyInfo(alias="orderAccessCodeContains")]
    """Filter by order access code containing this value (case-insensitive)"""

    order_id: Annotated[str, PropertyInfo(alias="orderId")]
    """Filter by exact order ID"""

    order_id_contains: Annotated[str, PropertyInfo(alias="orderIdContains")]
    """Filter by order ID containing this value (case-insensitive)"""

    order_number: Annotated[str, PropertyInfo(alias="orderNumber")]
    """Filter by exact order number"""

    order_number_contains: Annotated[str, PropertyInfo(alias="orderNumberContains")]
    """Filter by order number containing this value (case-insensitive)"""

    page: int

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]

    provider_id: Annotated[str, PropertyInfo(alias="providerId")]
    """Filter by exact provider ID"""

    service_id: Annotated[str, PropertyInfo(alias="serviceId")]
    """Filter by exact service ID within services array"""

    since: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Filter orderItems created after this time"""

    status: str
    """Filter by service status within orderItems"""

    until: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Filter orderItems created before this time"""

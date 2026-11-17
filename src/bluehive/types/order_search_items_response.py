# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["OrderSearchItemsResponse", "Meta", "OrderItemService", "OrderItem"]


class Meta(BaseModel):
    page: int

    page_size: int = FieldInfo(alias="pageSize")

    returned: int

    total: int


class OrderItemService(BaseModel):
    due_date: Optional[datetime] = FieldInfo(alias="dueDate", default=None)

    last_edit: Optional[datetime] = FieldInfo(alias="lastEdit", default=None)

    price: Optional[float] = None

    quantity: Optional[int] = None

    results: Optional[Dict[str, object]] = None

    self_report: Optional[bool] = FieldInfo(alias="selfReport", default=None)

    service_id: Optional[str] = FieldInfo(alias="serviceId", default=None)

    status: Optional[str] = None


class OrderItem(BaseModel):
    id: Optional[str] = FieldInfo(alias="_id", default=None)

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    created_by: Optional[str] = FieldInfo(alias="createdBy", default=None)

    demo: Optional[bool] = None

    employee_id: Optional[str] = FieldInfo(alias="employeeId", default=None)

    employer_id: Optional[str] = FieldInfo(alias="employerId", default=None)

    order_access_code: Optional[str] = FieldInfo(alias="orderAccessCode", default=None)

    order_id: Optional[str] = FieldInfo(alias="orderId", default=None)

    order_number: Optional[str] = FieldInfo(alias="orderNumber", default=None)

    priority: Optional[str] = None

    provider_id: Optional[str] = FieldInfo(alias="providerId", default=None)

    services: Optional[List[OrderItemService]] = None


class OrderSearchItemsResponse(BaseModel):
    meta: Meta

    order_items: List[OrderItem] = FieldInfo(alias="orderItems")

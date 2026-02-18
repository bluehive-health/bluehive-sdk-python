# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ServiceBundleRetrieveResponse", "IntegrationData", "IntegrationDataEnterpriseHealth"]


class IntegrationDataEnterpriseHealth(BaseModel):
    add_on_services: Optional[bool] = FieldInfo(alias="addOnServices", default=None)


class IntegrationData(BaseModel):
    enterprise_health: Optional[IntegrationDataEnterpriseHealth] = FieldInfo(alias="enterprise-health", default=None)


class ServiceBundleRetrieveResponse(BaseModel):
    api_id: str = FieldInfo(alias="_id")

    bundle_name: str = FieldInfo(alias="bundleName")

    employer_id: str = FieldInfo(alias="employerId")

    service_ids: List[str] = FieldInfo(alias="serviceIds")

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    created_by: Optional[str] = FieldInfo(alias="createdBy", default=None)

    externally_managed: Optional[bool] = FieldInfo(alias="externallyManaged", default=None)
    """Indicates if this bundle originated from a third-party integration.

    Externally managed bundles cannot be edited or deleted in BlueHive.
    """

    integration: Optional[str] = None
    """
    Name of the third-party integration that manages this bundle (e.g., "Enterprise
    Health"). Null if bundle was created in BlueHive.
    """

    integration_data: Optional[IntegrationData] = FieldInfo(alias="integrationData", default=None)

    limit: Optional[float] = None

    occurrence: Optional[str] = None

    recurring: Optional[bool] = None

    roles: Optional[List[str]] = None

    start_date: Optional[str] = FieldInfo(alias="startDate", default=None)

    updated_at: Optional[str] = FieldInfo(alias="updatedAt", default=None)

    updated_by: Optional[str] = FieldInfo(alias="updatedBy", default=None)

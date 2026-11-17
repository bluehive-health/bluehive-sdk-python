# Checks each call added from the live API description against a stubbed transport (respx).
# For every call: one request with the description's method and path, every argument sent where the description
# puts it, and the documented response parsed into the method's return type with strict validation on.

from __future__ import annotations

import json
from typing import Any, Dict, cast

import httpx
import respx
import pytest

from bluehive import BlueHive, AsyncBlueHive, types
from bluehive._models import BaseModel

base_url = "http://stub.test"

CASES: list[Dict[str, Any]] = json.loads(
    '[{"id": "orders.cancel", "resource": "orders", "method": "cancel", "http": "POST", "path": "/v1/orders/orderId-value/cancel", "args": ["orderId-value"], "kwargs": {}, "body": {}, "query": {}, "headers": {}, "response": {"success": true, "message": "message-value"}, "response_type": "OrderCancelResponse"}, {"id": "orders.update_status", "resource": "orders", "method": "update_status", "http": "PUT", "path": "/v1/orders/orderId-value/status", "args": ["orderId-value"], "kwargs": {"status": "order_sent", "message": "message-value"}, "body": {"status": "order_sent", "message": "message-value"}, "query": {}, "headers": {}, "response": {"success": true, "message": "message-value"}, "response_type": "OrderUpdateStatusResponse"}, {"id": "orders.search_items", "resource": "orders", "method": "search_items", "http": "GET", "path": "/v1/orderItems", "args": [], "kwargs": {"page": 1, "page_size": 1, "id": "id-value", "order_number": "orderNumber-value", "order_id": "orderId-value", "employee_id": "employeeId-value", "employer_id": "employerId-value", "provider_id": "providerId-value", "order_access_code": "orderAccessCode-value", "service_id": "serviceId-value", "status": "status-value", "id_contains": "idContains-value", "order_number_contains": "orderNumberContains-value", "order_id_contains": "orderIdContains-value", "employee_id_contains": "employeeIdContains-value", "order_access_code_contains": "orderAccessCodeContains-value", "since": "2026-01-15T10:00:00+00:00", "until": "2026-01-15T10:00:00+00:00"}, "body": {}, "query": {"page": "1", "pageSize": "1", "id": "id-value", "orderNumber": "orderNumber-value", "orderId": "orderId-value", "employeeId": "employeeId-value", "employerId": "employerId-value", "providerId": "providerId-value", "orderAccessCode": "orderAccessCode-value", "serviceId": "serviceId-value", "status": "status-value", "idContains": "idContains-value", "orderNumberContains": "orderNumberContains-value", "orderIdContains": "orderIdContains-value", "employeeIdContains": "employeeIdContains-value", "orderAccessCodeContains": "orderAccessCodeContains-value", "since": "2026-01-15T10:00:00+00:00", "until": "2026-01-15T10:00:00+00:00"}, "headers": {}, "response": {"meta": {"page": 1, "pageSize": 1, "total": 1, "returned": 1}, "orderItems": [{"_id": "_id-value", "orderId": "orderId-value", "orderNumber": "orderNumber-value", "employerId": "employerId-value", "employeeId": "employeeId-value", "providerId": "providerId-value", "orderAccessCode": "orderAccessCode-value", "priority": "priority-value", "createdAt": "2026-01-15T10:00:00+00:00", "createdBy": "createdBy-value", "services": [{"serviceId": "serviceId-value", "price": 1.5, "quantity": 1, "lastEdit": "2026-01-15T10:00:00+00:00", "status": "status-value", "dueDate": "2026-01-15T10:00:00+00:00", "selfReport": true, "results": {}}], "demo": true}]}, "response_type": "OrderSearchItemsResponse"}, {"id": "fax.send_stored", "resource": "fax", "method": "send_stored", "http": "POST", "path": "/v1/fax/faxId-value/send", "args": ["faxId-value"], "kwargs": {"to": "to-value", "from_": "from-value", "subject": "subject-value"}, "body": {"to": "to-value", "from": "from-value", "subject": "subject-value"}, "query": {}, "headers": {}, "response": {"id": "id-value", "status": "queued", "provider": "provider-value", "to": "to-value", "from": "from-value", "createdAt": "createdAt-value", "estimatedDelivery": "estimatedDelivery-value"}, "response_type": "FaxSendStoredResponse"}, {"id": "fax.retrieve_subscription_health", "resource": "fax", "method": "retrieve_subscription_health", "http": "GET", "path": "/v1/fax/subscriptions/health", "args": [], "kwargs": {}, "body": {}, "query": {}, "headers": {}, "response": [{}], "response_type": "FaxRetrieveSubscriptionHealthResponse"}, {"id": "hl7.process", "resource": "hl7", "method": "process", "http": "POST", "path": "/v1/hl7", "args": [], "kwargs": {"message": "message-value", "f": "f-value", "interface": "interface-value", "login_user": "login_user-value", "login_passwd": "login_passwd-value", "message_b64": "message_b64-value"}, "body": {"message": "message-value", "f": "f-value", "interface": "interface-value", "login_user": "login_user-value", "login_passwd": "login_passwd-value", "message_b64": "message_b64-value"}, "query": {}, "headers": {}, "response": "x-value", "response_type": "Hl7ProcessResponse"}, {"id": "hl7.replay", "resource": "hl7", "method": "replay", "http": "POST", "path": "/v1/hl7/replay/logId-value", "args": ["logId-value"], "kwargs": {"destination": {"url": "aaaa", "protocol": "http", "port": 1.5, "username": "username-value", "password": "password-value", "timeout": 1.5, "retryAttempts": 1.5, "retryDelay": 1.5}, "interface_name": "interfaceName-value"}, "body": {"destination": {"url": "aaaa", "protocol": "http", "port": 1.5, "username": "username-value", "password": "password-value", "timeout": 1.5, "retryAttempts": 1.5, "retryDelay": 1.5}, "interfaceName": "interfaceName-value"}, "query": {}, "headers": {}, "response": {"success": true, "messageId": "messageId-value", "acknowledgment": "acknowledgment-value", "retryCount": 1.5, "duration": 1.5, "originalLogId": "originalLogId-value", "newLogTimestamp": "newLogTimestamp-value"}, "response_type": "Hl7ReplayResponse"}, {"id": "providers.search", "resource": "providers", "method": "search", "http": "GET", "path": "/v1/providers/search", "args": [], "kwargs": {"zipcode": "aaaaa", "radius": "radius-value", "services": "services-value", "provider_id": "providerId-value", "employer_id": "employerId-value", "brand_id": "brandId-value", "limit": "limit-value"}, "body": {}, "query": {"zipcode": "aaaaa", "radius": "radius-value", "services": "services-value", "providerId": "providerId-value", "employerId": "employerId-value", "brandId": "brandId-value", "limit": "limit-value"}, "headers": {}, "response": {"status": "status-value", "count": 1.5, "zipcode": "zipcode-value", "radius": 1.5, "providers": [{"_id": "_id-value", "name": "name-value", "slug": "slug-value", "address": {"street1": "street1-value", "street2": "street2-value", "city": "city-value", "state": "state-value", "postalCode": "postalCode-value", "county": "county-value", "country": "country-value"}, "email": "email-value", "logoURL": "logoURL-value", "phone_numbers": [{"type": "type-value", "number": "number-value"}], "loc": {"type": "type-value", "coordinates": [1.5]}, "distance": 1.5, "url": "url-value", "services": [{"serviceId": "serviceId-value", "name": "name-value", "slug": "slug-value", "price": 1.5}]}]}, "response_type": "ProviderSearchResponse"}]'
)


def _check_request(route: respx.Route, case: Dict[str, Any]) -> None:
    assert route.call_count == 1
    request = cast(httpx.Request, route.calls[0].request)  # pyright: ignore[reportUnknownMemberType]
    assert request.method == case["http"]
    assert request.url.path == case["path"]
    if case["body"]:
        sent = json.loads(request.content or b"{}")
        for key, expected in case["body"].items():
            assert sent.get(key) == expected, key
    for key, expected in case["query"].items():
        assert str(request.url.params.get(key)).lower() == expected.lower(), key
    for key, expected in case["headers"].items():
        assert request.headers.get(key) == expected, key


def _check_response(result: Any, case: Dict[str, Any]) -> None:
    expected = case["response"]
    if isinstance(result, BaseModel):
        # every field of the documented response came back, under its wire name
        assert set(result.to_dict(use_api_names=True).keys()) == set(expected.keys())
    elif isinstance(expected, str):
        # a string response comes back as the response body's text, as the existing string methods do
        assert result == json.dumps(expected)
    else:
        # a list or map response is returned as parsed
        assert result == expected
    expected_type = getattr(types, case["response_type"])
    if isinstance(expected_type, type):
        assert isinstance(result, expected_type)


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
@respx.mock
def test_added_call_sync(case: Dict[str, Any]) -> None:
    route = respx.route(method=case["http"], url__startswith=base_url + case["path"]).mock(
        return_value=httpx.Response(200, json=case["response"])
    )
    client = BlueHive(base_url=base_url, api_key="My API Key", _strict_response_validation=True)
    method = getattr(getattr(client, case["resource"]), case["method"])
    result = method(*case["args"], **case["kwargs"])
    _check_request(route, case)
    _check_response(result, case)


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
@respx.mock
async def test_added_call_async(case: Dict[str, Any]) -> None:
    route = respx.route(method=case["http"], url__startswith=base_url + case["path"]).mock(
        return_value=httpx.Response(200, json=case["response"])
    )
    client = AsyncBlueHive(base_url=base_url, api_key="My API Key", _strict_response_validation=True)
    method = getattr(getattr(client, case["resource"]), case["method"])
    result = await method(*case["args"], **case["kwargs"])
    _check_request(route, case)
    _check_response(result, case)

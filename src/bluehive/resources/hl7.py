# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict

import httpx

from ..types import hl7_replay_params, hl7_process_params, hl7_send_results_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.hl7_replay_response import Hl7ReplayResponse
from ..types.hl7_process_response import Hl7ProcessResponse

__all__ = ["Hl7Resource", "AsyncHl7Resource"]


class Hl7Resource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> Hl7ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/bluehive-health/bluehive-sdk-python#accessing-raw-response-data-eg-headers
        """
        return Hl7ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> Hl7ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/bluehive-health/bluehive-sdk-python#with_streaming_response
        """
        return Hl7ResourceWithStreamingResponse(self)

    def send_results(
        self,
        *,
        employee_id: str,
        file: hl7_send_results_params.File,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """
        Send lab results or documents via HL7

        Args:
          employee_id: Employee ID to send results for

          file: File containing the results

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/hl7/results",
            body=maybe_transform(
                {
                    "employee_id": employee_id,
                    "file": file,
                },
                hl7_send_results_params.Hl7SendResultsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    def process(
        self,
        *,
        message: object | Omit = omit,
        f: str | Omit = omit,
        interface: str | Omit = omit,
        login_user: str | Omit = omit,
        login_passwd: str | Omit = omit,
        message_b64: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Hl7ProcessResponse:
        """
        Process incoming HL7 messages from EHR systems. Accepts JSON with "message" field, raw text/plain HL7 content, or form-encoded data.

        Args:
          message: HL7 message content - the primary way to send HL7 data

          f: Form field (legacy support)

          interface: Interface identifier (legacy support)

          login_user: Login user (legacy support)

          login_passwd: Login password (legacy support)

          message_b64: Base64 encoded HL7 message (legacy support)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/hl7",
            body=maybe_transform(
                {
                    "message": message,
                    "f": f,
                    "interface": interface,
                    "login_user": login_user,
                    "login_passwd": login_passwd,
                    "message_b64": message_b64,
                },
                hl7_process_params.Hl7ProcessParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    def replay(
        self,
        log_id: str,
        *,
        destination: Dict[str, object] | Omit = omit,
        interface_name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Hl7ReplayResponse:
        """
        Replay a previously sent outbound HL7 message by its log ID. The exact same message will be re-sent to the specified destination. If no destination is provided, the original destination will be used (credentials required).

        Args:
          destination: Destination configuration for sending the message. If not provided, uses the original destination from the log.

          interface_name: Interface name to use in the request (default: bluehiveadt)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not log_id:
            raise ValueError(f"Expected a non-empty value for `log_id` but received {log_id!r}")
        return self._post(
            path_template("/v1/hl7/replay/{log_id}", log_id=log_id),
            body=maybe_transform(
                {
                    "destination": destination,
                    "interface_name": interface_name,
                },
                hl7_replay_params.Hl7ReplayParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Hl7ReplayResponse,
        )


class AsyncHl7Resource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncHl7ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/bluehive-health/bluehive-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncHl7ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHl7ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/bluehive-health/bluehive-sdk-python#with_streaming_response
        """
        return AsyncHl7ResourceWithStreamingResponse(self)

    async def send_results(
        self,
        *,
        employee_id: str,
        file: hl7_send_results_params.File,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """
        Send lab results or documents via HL7

        Args:
          employee_id: Employee ID to send results for

          file: File containing the results

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/hl7/results",
            body=await async_maybe_transform(
                {
                    "employee_id": employee_id,
                    "file": file,
                },
                hl7_send_results_params.Hl7SendResultsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    async def process(
        self,
        *,
        message: object | Omit = omit,
        f: str | Omit = omit,
        interface: str | Omit = omit,
        login_user: str | Omit = omit,
        login_passwd: str | Omit = omit,
        message_b64: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Hl7ProcessResponse:
        """
        Process incoming HL7 messages from EHR systems. Accepts JSON with "message" field, raw text/plain HL7 content, or form-encoded data.

        Args:
          message: HL7 message content - the primary way to send HL7 data

          f: Form field (legacy support)

          interface: Interface identifier (legacy support)

          login_user: Login user (legacy support)

          login_passwd: Login password (legacy support)

          message_b64: Base64 encoded HL7 message (legacy support)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/hl7",
            body=await async_maybe_transform(
                {
                    "message": message,
                    "f": f,
                    "interface": interface,
                    "login_user": login_user,
                    "login_passwd": login_passwd,
                    "message_b64": message_b64,
                },
                hl7_process_params.Hl7ProcessParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    async def replay(
        self,
        log_id: str,
        *,
        destination: Dict[str, object] | Omit = omit,
        interface_name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Hl7ReplayResponse:
        """
        Replay a previously sent outbound HL7 message by its log ID. The exact same message will be re-sent to the specified destination. If no destination is provided, the original destination will be used (credentials required).

        Args:
          destination: Destination configuration for sending the message. If not provided, uses the original destination from the log.

          interface_name: Interface name to use in the request (default: bluehiveadt)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not log_id:
            raise ValueError(f"Expected a non-empty value for `log_id` but received {log_id!r}")
        return await self._post(
            path_template("/v1/hl7/replay/{log_id}", log_id=log_id),
            body=await async_maybe_transform(
                {
                    "destination": destination,
                    "interface_name": interface_name,
                },
                hl7_replay_params.Hl7ReplayParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Hl7ReplayResponse,
        )


class Hl7ResourceWithRawResponse:
    def __init__(self, hl7: Hl7Resource) -> None:
        self._hl7 = hl7

        self.send_results = to_raw_response_wrapper(
            hl7.send_results,
        )
        self.process = to_raw_response_wrapper(
            hl7.process,
        )
        self.replay = to_raw_response_wrapper(
            hl7.replay,
        )


class AsyncHl7ResourceWithRawResponse:
    def __init__(self, hl7: AsyncHl7Resource) -> None:
        self._hl7 = hl7

        self.send_results = async_to_raw_response_wrapper(
            hl7.send_results,
        )
        self.process = async_to_raw_response_wrapper(
            hl7.process,
        )
        self.replay = async_to_raw_response_wrapper(
            hl7.replay,
        )


class Hl7ResourceWithStreamingResponse:
    def __init__(self, hl7: Hl7Resource) -> None:
        self._hl7 = hl7

        self.send_results = to_streamed_response_wrapper(
            hl7.send_results,
        )
        self.process = to_streamed_response_wrapper(
            hl7.process,
        )
        self.replay = to_streamed_response_wrapper(
            hl7.replay,
        )


class AsyncHl7ResourceWithStreamingResponse:
    def __init__(self, hl7: AsyncHl7Resource) -> None:
        self._hl7 = hl7

        self.send_results = async_to_streamed_response_wrapper(
            hl7.send_results,
        )
        self.process = async_to_streamed_response_wrapper(
            hl7.process,
        )
        self.replay = async_to_streamed_response_wrapper(
            hl7.replay,
        )

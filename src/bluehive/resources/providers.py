# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import provider_lookup_params, provider_search_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.provider_lookup_response import ProviderLookupResponse
from ..types.provider_search_response import ProviderSearchResponse

__all__ = ["ProvidersResource", "AsyncProvidersResource"]


class ProvidersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ProvidersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/bluehive-health/bluehive-sdk-python#accessing-raw-response-data-eg-headers
        """
        return ProvidersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProvidersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/bluehive-health/bluehive-sdk-python#with_streaming_response
        """
        return ProvidersResourceWithStreamingResponse(self)

    def lookup(
        self,
        *,
        firstname: str | Omit = omit,
        lastname: str | Omit = omit,
        npi: str | Omit = omit,
        zipcode: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProviderLookupResponse:
        """
        Search for healthcare providers by NPI number, name, or location proximity.

        Args:
          firstname: Provider first name

          lastname: Provider last name

          npi: Provider NPI number

          zipcode: ZIP code to filter results by proximity

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/providers/lookup",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "firstname": firstname,
                        "lastname": lastname,
                        "npi": npi,
                        "zipcode": zipcode,
                    },
                    provider_lookup_params.ProviderLookupParams,
                ),
            ),
            cast_to=ProviderLookupResponse,
        )

    def search(
        self,
        *,
        zipcode: str,
        radius: str | Omit = omit,
        services: str | Omit = omit,
        provider_id: str | Omit = omit,
        employer_id: str | Omit = omit,
        brand_id: str | Omit = omit,
        limit: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProviderSearchResponse:
        """
        Search for healthcare providers near a given zipcode. Optionally filter by services and customize the search radius. When services are provided, only providers offering those services are returned with pricing info.

        Args:
          zipcode: US postal code to search near (5-digit or ZIP+4 format)

          radius: Search radius in miles (default: 25, max: 100)

          services: Comma-separated service IDs to filter by (optional)

          provider_id: Comma-separated provider IDs to restrict results to (optional)

          employer_id: Employer ID for employer-specific pricing (optional)

          brand_id: Brand ID to filter services by brand (optional)

          limit: Maximum number of providers to return (default: 50, max: 200)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/providers/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "zipcode": zipcode,
                        "radius": radius,
                        "services": services,
                        "provider_id": provider_id,
                        "employer_id": employer_id,
                        "brand_id": brand_id,
                        "limit": limit,
                    },
                    provider_search_params.ProviderSearchParams,
                ),
            ),
            cast_to=ProviderSearchResponse,
        )


class AsyncProvidersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncProvidersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/bluehive-health/bluehive-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncProvidersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProvidersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/bluehive-health/bluehive-sdk-python#with_streaming_response
        """
        return AsyncProvidersResourceWithStreamingResponse(self)

    async def lookup(
        self,
        *,
        firstname: str | Omit = omit,
        lastname: str | Omit = omit,
        npi: str | Omit = omit,
        zipcode: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProviderLookupResponse:
        """
        Search for healthcare providers by NPI number, name, or location proximity.

        Args:
          firstname: Provider first name

          lastname: Provider last name

          npi: Provider NPI number

          zipcode: ZIP code to filter results by proximity

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/providers/lookup",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "firstname": firstname,
                        "lastname": lastname,
                        "npi": npi,
                        "zipcode": zipcode,
                    },
                    provider_lookup_params.ProviderLookupParams,
                ),
            ),
            cast_to=ProviderLookupResponse,
        )

    async def search(
        self,
        *,
        zipcode: str,
        radius: str | Omit = omit,
        services: str | Omit = omit,
        provider_id: str | Omit = omit,
        employer_id: str | Omit = omit,
        brand_id: str | Omit = omit,
        limit: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProviderSearchResponse:
        """
        Search for healthcare providers near a given zipcode. Optionally filter by services and customize the search radius. When services are provided, only providers offering those services are returned with pricing info.

        Args:
          zipcode: US postal code to search near (5-digit or ZIP+4 format)

          radius: Search radius in miles (default: 25, max: 100)

          services: Comma-separated service IDs to filter by (optional)

          provider_id: Comma-separated provider IDs to restrict results to (optional)

          employer_id: Employer ID for employer-specific pricing (optional)

          brand_id: Brand ID to filter services by brand (optional)

          limit: Maximum number of providers to return (default: 50, max: 200)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/providers/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "zipcode": zipcode,
                        "radius": radius,
                        "services": services,
                        "provider_id": provider_id,
                        "employer_id": employer_id,
                        "brand_id": brand_id,
                        "limit": limit,
                    },
                    provider_search_params.ProviderSearchParams,
                ),
            ),
            cast_to=ProviderSearchResponse,
        )


class ProvidersResourceWithRawResponse:
    def __init__(self, providers: ProvidersResource) -> None:
        self._providers = providers

        self.lookup = to_raw_response_wrapper(
            providers.lookup,
        )
        self.search = to_raw_response_wrapper(
            providers.search,
        )


class AsyncProvidersResourceWithRawResponse:
    def __init__(self, providers: AsyncProvidersResource) -> None:
        self._providers = providers

        self.lookup = async_to_raw_response_wrapper(
            providers.lookup,
        )
        self.search = async_to_raw_response_wrapper(
            providers.search,
        )


class ProvidersResourceWithStreamingResponse:
    def __init__(self, providers: ProvidersResource) -> None:
        self._providers = providers

        self.lookup = to_streamed_response_wrapper(
            providers.lookup,
        )
        self.search = to_streamed_response_wrapper(
            providers.search,
        )


class AsyncProvidersResourceWithStreamingResponse:
    def __init__(self, providers: AsyncProvidersResource) -> None:
        self._providers = providers

        self.lookup = async_to_streamed_response_wrapper(
            providers.lookup,
        )
        self.search = async_to_streamed_response_wrapper(
            providers.search,
        )

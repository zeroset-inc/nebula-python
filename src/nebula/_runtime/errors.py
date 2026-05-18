from __future__ import annotations

from typing import Any, Optional


class NebulaError(Exception):
    pass


class NebulaConnectionError(NebulaError):
    pass


class NebulaTimeoutError(NebulaError):
    pass


class NebulaAPIError(NebulaError):
    def __init__(
        self,
        status: int,
        body: Any,
        request_id: Optional[str] = None,
        message: Optional[str] = None,
    ) -> None:
        super().__init__(message or f"Nebula API error (status {status})")
        self.status = status
        self.body = body
        self.request_id = request_id


class NebulaBadRequestError(NebulaAPIError):
    pass


class NebulaUnauthorizedError(NebulaAPIError):
    pass


class NebulaForbiddenError(NebulaAPIError):
    pass


class NebulaNotFoundError(NebulaAPIError):
    pass


class NebulaConflictError(NebulaAPIError):
    pass


class NebulaValidationError(NebulaAPIError):
    pass


class NebulaRateLimitError(NebulaAPIError):
    def __init__(
        self,
        status: int,
        body: Any,
        request_id: Optional[str] = None,
        retry_after: Optional[float] = None,
    ) -> None:
        super().__init__(status=status, body=body, request_id=request_id)
        self.retry_after = retry_after


class NebulaServerError(NebulaAPIError):
    pass


_STATUS_TO_CLASS: dict[int, type[NebulaAPIError]] = {
    400: NebulaBadRequestError,
    401: NebulaUnauthorizedError,
    403: NebulaForbiddenError,
    404: NebulaNotFoundError,
    409: NebulaConflictError,
    422: NebulaValidationError,
}


def error_from_response(
    *,
    status: int,
    body: Any,
    request_id: Optional[str] = None,
    retry_after: Optional[float] = None,
) -> NebulaAPIError:
    if status == 429:
        return NebulaRateLimitError(
            status=status, body=body, request_id=request_id, retry_after=retry_after
        )
    cls = _STATUS_TO_CLASS.get(status)
    if cls is not None:
        return cls(status=status, body=body, request_id=request_id)
    if status >= 500:
        return NebulaServerError(status=status, body=body, request_id=request_id)
    return NebulaAPIError(status=status, body=body, request_id=request_id)

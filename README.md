# nebula-sdk

Official Nebula API SDK for Python. Provides typed async access to the public
Nebula REST API: collections, memories, connectors, snapshots, and system
health.

## Install

```bash
pip install nebula-sdk
# or
uv add nebula-sdk
```

## Quick start

```python
import asyncio
from nebula import Nebula, ClientOptions

async def main() -> None:
    async with Nebula(ClientOptions(api_key="...")) as client:
        memory_id = await client.store_memory(
            collection_id="01234567-...",
            raw_text="hello, world",
        )
        results = await client.search("hello")
        print(results)

asyncio.run(main())
```

This SDK is **async-first**. If you need to call it from a sync context, wrap
each call with `asyncio.run(...)`. A dedicated sync client is not currently
provided.

## Auth

The constructor accepts `api_key` / `access_token` plus their camelCase
aliases `apiKey` / `accessToken` / `bearerToken`. If you pass an API key
that doesn't look like a Nebula key (not prefixed with `key_` or `neb_`),
the DX layer automatically routes it through the bearer-token header instead.

## Errors

All HTTP errors map to a typed exception hierarchy:

- `NebulaBadRequestError` (400)
- `NebulaUnauthorizedError` (401)
- `NebulaForbiddenError` (403)
- `NebulaNotFoundError` (404)
- `NebulaConflictError` (409)
- `NebulaValidationError` (422)
- `NebulaRateLimitError` (429) — carries `retry_after` when the server returns `Retry-After`
- `NebulaServerError` (5xx)
- `NebulaConnectionError` / `NebulaTimeoutError` — transport-level

## Docs

- API reference: https://docs.zeroset.com
- Migration notes: see `MIGRATION.md` in the source repo

## License

MIT

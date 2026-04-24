# Nebula

Types:

```python
from nebula.types import HealthResponse
```

Methods:

- <code title="get /v1/health">client.<a href="./src/nebula/_client.py">health</a>() -> <a href="./src/nebula/types/health_response.py">HealthResponse</a></code>

# Collections

Types:

```python
from nebula.types import (
    CollectionCreateResponse,
    CollectionRetrieveResponse,
    CollectionUpdateResponse,
    CollectionListResponse,
    CollectionDeleteResponse,
    CollectionRetrieveByNameResponse,
)
```

Methods:

- <code title="post /v1/collections">client.collections.<a href="./src/nebula/resources/collections.py">create</a>(\*\*<a href="src/nebula/types/collection_create_params.py">params</a>) -> <a href="./src/nebula/types/collection_create_response.py">CollectionCreateResponse</a></code>
- <code title="get /v1/collections/{id}">client.collections.<a href="./src/nebula/resources/collections.py">retrieve</a>(id) -> <a href="./src/nebula/types/collection_retrieve_response.py">CollectionRetrieveResponse</a></code>
- <code title="post /v1/collections/{id}">client.collections.<a href="./src/nebula/resources/collections.py">update</a>(id, \*\*<a href="src/nebula/types/collection_update_params.py">params</a>) -> <a href="./src/nebula/types/collection_update_response.py">CollectionUpdateResponse</a></code>
- <code title="get /v1/collections">client.collections.<a href="./src/nebula/resources/collections.py">list</a>(\*\*<a href="src/nebula/types/collection_list_params.py">params</a>) -> <a href="./src/nebula/types/collection_list_response.py">CollectionListResponse</a></code>
- <code title="delete /v1/collections/{id}">client.collections.<a href="./src/nebula/resources/collections.py">delete</a>(id) -> <a href="./src/nebula/types/collection_delete_response.py">CollectionDeleteResponse</a></code>
- <code title="get /v1/collections/name/{collection_name}">client.collections.<a href="./src/nebula/resources/collections.py">retrieve_by_name</a>(collection_name, \*\*<a href="src/nebula/types/collection_retrieve_by_name_params.py">params</a>) -> <a href="./src/nebula/types/collection_retrieve_by_name_response.py">CollectionRetrieveByNameResponse</a></code>

# Memories

Types:

```python
from nebula.types import (
    MemoryCreateResponse,
    MemoryRetrieveResponse,
    MemoryUpdateResponse,
    MemoryListResponse,
    MemoryDeleteResponse,
    MemoryAppendResponse,
    MemoryCreateUploadResponse,
    MemoryDeleteManyResponse,
    MemoryDeleteUploadResponse,
    MemorySearchResponse,
)
```

Methods:

- <code title="post /v1/memories">client.memories.<a href="./src/nebula/resources/memories.py">create</a>(\*\*<a href="src/nebula/types/memory_create_params.py">params</a>) -> <a href="./src/nebula/types/memory_create_response.py">MemoryCreateResponse</a></code>
- <code title="get /v1/memories/{id}">client.memories.<a href="./src/nebula/resources/memories.py">retrieve</a>(id) -> <a href="./src/nebula/types/memory_retrieve_response.py">MemoryRetrieveResponse</a></code>
- <code title="patch /v1/memories/{id}">client.memories.<a href="./src/nebula/resources/memories.py">update</a>(id, \*\*<a href="src/nebula/types/memory_update_params.py">params</a>) -> <a href="./src/nebula/types/memory_update_response.py">MemoryUpdateResponse</a></code>
- <code title="get /v1/memories">client.memories.<a href="./src/nebula/resources/memories.py">list</a>(\*\*<a href="src/nebula/types/memory_list_params.py">params</a>) -> <a href="./src/nebula/types/memory_list_response.py">MemoryListResponse</a></code>
- <code title="delete /v1/memories/{id}">client.memories.<a href="./src/nebula/resources/memories.py">delete</a>(id) -> <a href="./src/nebula/types/memory_delete_response.py">MemoryDeleteResponse</a></code>
- <code title="post /v1/memories/{id}/append">client.memories.<a href="./src/nebula/resources/memories.py">append</a>(id, \*\*<a href="src/nebula/types/memory_append_params.py">params</a>) -> <a href="./src/nebula/types/memory_append_response.py">MemoryAppendResponse</a></code>
- <code title="post /v1/memories/upload">client.memories.<a href="./src/nebula/resources/memories.py">create_upload</a>(\*\*<a href="src/nebula/types/memory_create_upload_params.py">params</a>) -> <a href="./src/nebula/types/memory_create_upload_response.py">MemoryCreateUploadResponse</a></code>
- <code title="post /v1/memories/delete">client.memories.<a href="./src/nebula/resources/memories.py">delete_many</a>(\*\*<a href="src/nebula/types/memory_delete_many_params.py">params</a>) -> <a href="./src/nebula/types/memory_delete_many_response.py">MemoryDeleteManyResponse</a></code>
- <code title="delete /v1/memories/upload">client.memories.<a href="./src/nebula/resources/memories.py">delete_upload</a>(\*\*<a href="src/nebula/types/memory_delete_upload_params.py">params</a>) -> <a href="./src/nebula/types/memory_delete_upload_response.py">MemoryDeleteUploadResponse</a></code>
- <code title="post /v1/memories/search">client.memories.<a href="./src/nebula/resources/memories.py">search</a>(\*\*<a href="src/nebula/types/memory_search_params.py">params</a>) -> <a href="./src/nebula/types/memory_search_response.py">MemorySearchResponse</a></code>

# Connectors

Types:

```python
from nebula.types import (
    ConnectorRetrieveResponse,
    ConnectorListResponse,
    ConnectorConnectResponse,
    ConnectorDisconnectResponse,
    ConnectorListProvidersResponse,
    ConnectorSyncResponse,
)
```

Methods:

- <code title="get /v1/connectors/{connection_id}">client.connectors.<a href="./src/nebula/resources/connectors.py">retrieve</a>(connection_id) -> <a href="./src/nebula/types/connector_retrieve_response.py">ConnectorRetrieveResponse</a></code>
- <code title="get /v1/connectors">client.connectors.<a href="./src/nebula/resources/connectors.py">list</a>(\*\*<a href="src/nebula/types/connector_list_params.py">params</a>) -> <a href="./src/nebula/types/connector_list_response.py">ConnectorListResponse</a></code>
- <code title="post /v1/connectors/{provider}/connect">client.connectors.<a href="./src/nebula/resources/connectors.py">connect</a>(provider, \*\*<a href="src/nebula/types/connector_connect_params.py">params</a>) -> <a href="./src/nebula/types/connector_connect_response.py">ConnectorConnectResponse</a></code>
- <code title="delete /v1/connectors/{connection_id}">client.connectors.<a href="./src/nebula/resources/connectors.py">disconnect</a>(connection_id, \*\*<a href="src/nebula/types/connector_disconnect_params.py">params</a>) -> <a href="./src/nebula/types/connector_disconnect_response.py">ConnectorDisconnectResponse</a></code>
- <code title="get /v1/connectors/providers">client.connectors.<a href="./src/nebula/resources/connectors.py">list_providers</a>() -> <a href="./src/nebula/types/connector_list_providers_response.py">ConnectorListProvidersResponse</a></code>
- <code title="post /v1/connectors/{connection_id}/sync">client.connectors.<a href="./src/nebula/resources/connectors.py">sync</a>(connection_id) -> <a href="./src/nebula/types/connector_sync_response.py">ConnectorSyncResponse</a></code>

# Snapshots

Types:

```python
from nebula.types import SnapshotExportResponse, SnapshotImportResponse
```

Methods:

- <code title="post /v1/device-memory/snapshot/export">client.snapshots.<a href="./src/nebula/resources/snapshots.py">export</a>(\*\*<a href="src/nebula/types/snapshot_export_params.py">params</a>) -> <a href="./src/nebula/types/snapshot_export_response.py">SnapshotExportResponse</a></code>
- <code title="post /v1/device-memory/snapshot/import">client.snapshots.<a href="./src/nebula/resources/snapshots.py">import\_</a>(\*\*<a href="src/nebula/types/snapshot_import_params.py">params</a>) -> <a href="./src/nebula/types/snapshot_import_response.py">SnapshotImportResponse</a></code>

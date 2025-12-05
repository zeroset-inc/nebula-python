# Nebula

Methods:

- <code title="get /">client.<a href="./src/nebula/_client.py">get_status</a>() -> object</code>

# Chunks

Types:

```python
from nebula.types import (
    ChunkResponse,
    ChunkSearchResult,
    NebulaResultsChunkResponse,
    NebulaResultsGenericBooleanResponse,
    PaginatedNebulaResultListChunkResponse,
    SearchSettings,
    ChunkSearchResponse,
)
```

Methods:

- <code title="get /v1/chunks/{id}">client.chunks.<a href="./src/nebula/resources/chunks.py">retrieve</a>(id) -> <a href="./src/nebula/types/nebula_results_chunk_response.py">NebulaResultsChunkResponse</a></code>
- <code title="post /v1/chunks/{id}">client.chunks.<a href="./src/nebula/resources/chunks.py">update</a>(path_id, \*\*<a href="src/nebula/types/chunk_update_params.py">params</a>) -> <a href="./src/nebula/types/nebula_results_chunk_response.py">NebulaResultsChunkResponse</a></code>
- <code title="get /v1/chunks">client.chunks.<a href="./src/nebula/resources/chunks.py">list</a>(\*\*<a href="src/nebula/types/chunk_list_params.py">params</a>) -> <a href="./src/nebula/types/paginated_nebula_result_list_chunk_response.py">PaginatedNebulaResultListChunkResponse</a></code>
- <code title="delete /v1/chunks/{id}">client.chunks.<a href="./src/nebula/resources/chunks.py">delete</a>(id) -> <a href="./src/nebula/types/nebula_results_generic_boolean_response.py">NebulaResultsGenericBooleanResponse</a></code>
- <code title="post /v1/chunks/search">client.chunks.<a href="./src/nebula/resources/chunks.py">search</a>(\*\*<a href="src/nebula/types/chunk_search_params.py">params</a>) -> <a href="./src/nebula/types/chunk_search_response.py">ChunkSearchResponse</a></code>

# Collections

Types:

```python
from nebula.types import (
    CollectionResponse,
    GraphCreationSettings,
    NebulaResultsCollectionResponse,
    PaginatedNebulaResultListCollectionResponse,
)
```

Methods:

- <code title="post /v1/collections">client.collections.<a href="./src/nebula/resources/collections/collections.py">create</a>(\*\*<a href="src/nebula/types/collection_create_params.py">params</a>) -> <a href="./src/nebula/types/nebula_results_collection_response.py">NebulaResultsCollectionResponse</a></code>
- <code title="get /v1/collections/{id}">client.collections.<a href="./src/nebula/resources/collections/collections.py">retrieve</a>(id) -> <a href="./src/nebula/types/nebula_results_collection_response.py">NebulaResultsCollectionResponse</a></code>
- <code title="post /v1/collections/{id}">client.collections.<a href="./src/nebula/resources/collections/collections.py">update</a>(id, \*\*<a href="src/nebula/types/collection_update_params.py">params</a>) -> <a href="./src/nebula/types/nebula_results_collection_response.py">NebulaResultsCollectionResponse</a></code>
- <code title="get /v1/collections">client.collections.<a href="./src/nebula/resources/collections/collections.py">list</a>(\*\*<a href="src/nebula/types/collection_list_params.py">params</a>) -> <a href="./src/nebula/types/paginated_nebula_result_list_collection_response.py">PaginatedNebulaResultListCollectionResponse</a></code>
- <code title="delete /v1/collections/{id}">client.collections.<a href="./src/nebula/resources/collections/collections.py">delete</a>(id) -> <a href="./src/nebula/types/nebula_results_generic_boolean_response.py">NebulaResultsGenericBooleanResponse</a></code>
- <code title="post /v1/collections/export">client.collections.<a href="./src/nebula/resources/collections/collections.py">export</a>(\*\*<a href="src/nebula/types/collection_export_params.py">params</a>) -> object</code>
- <code title="post /v1/collections/{id}/extract">client.collections.<a href="./src/nebula/resources/collections/collections.py">extract</a>(id, \*\*<a href="src/nebula/types/collection_extract_params.py">params</a>) -> <a href="./src/nebula/types/collections/nebula_results_generic_message_response.py">NebulaResultsGenericMessageResponse</a></code>
- <code title="get /v1/collections/{id}/documents-with-memories">client.collections.<a href="./src/nebula/resources/collections/collections.py">get_documents_with_memories</a>(id, \*\*<a href="src/nebula/types/collection_get_documents_with_memories_params.py">params</a>) -> object</code>
- <code title="get /v1/collections/{collection_id}/metrics">client.collections.<a href="./src/nebula/resources/collections/collections.py">get_metrics</a>(collection_id, \*\*<a href="src/nebula/types/collection_get_metrics_params.py">params</a>) -> object</code>
- <code title="get /v1/collections/name/{collection_name}">client.collections.<a href="./src/nebula/resources/collections/collections.py">retrieve_by_name</a>(collection_name, \*\*<a href="src/nebula/types/collection_retrieve_by_name_params.py">params</a>) -> <a href="./src/nebula/types/nebula_results_collection_response.py">NebulaResultsCollectionResponse</a></code>
- <code title="post /v1/collections/{id}/validate-status">client.collections.<a href="./src/nebula/resources/collections/collections.py">validate_status</a>(id, \*\*<a href="src/nebula/types/collection_validate_status_params.py">params</a>) -> object</code>

## Engrams

Types:

```python
from nebula.types.collections import (
    NebulaResultsGenericMessageResponse,
    PaginatedNebulaResultListEngramResponse,
)
```

Methods:

- <code title="get /v1/collections/{id}/engrams">client.collections.engrams.<a href="./src/nebula/resources/collections/engrams.py">list</a>(id, \*\*<a href="src/nebula/types/collections/engram_list_params.py">params</a>) -> <a href="./src/nebula/types/collections/paginated_nebula_result_list_engram_response.py">PaginatedNebulaResultListEngramResponse</a></code>
- <code title="post /v1/collections/{id}/engrams/{engram_id}">client.collections.engrams.<a href="./src/nebula/resources/collections/engrams.py">add</a>(engram_id, \*, id) -> <a href="./src/nebula/types/collections/nebula_results_generic_message_response.py">NebulaResultsGenericMessageResponse</a></code>
- <code title="delete /v1/collections/{id}/engrams/{engram_id}">client.collections.engrams.<a href="./src/nebula/resources/collections/engrams.py">remove</a>(engram_id, \*, id) -> <a href="./src/nebula/types/nebula_results_generic_boolean_response.py">NebulaResultsGenericBooleanResponse</a></code>

## Users

Types:

```python
from nebula.types.collections import PaginatedNebulaResultListUser
```

Methods:

- <code title="get /v1/collections/{id}/users">client.collections.users.<a href="./src/nebula/resources/collections/users.py">list</a>(id, \*\*<a href="src/nebula/types/collections/user_list_params.py">params</a>) -> <a href="./src/nebula/types/collections/paginated_nebula_result_list_user.py">PaginatedNebulaResultListUser</a></code>
- <code title="post /v1/collections/{id}/users/{user_id}">client.collections.users.<a href="./src/nebula/resources/collections/users.py">add</a>(user_id, \*, id) -> <a href="./src/nebula/types/nebula_results_generic_boolean_response.py">NebulaResultsGenericBooleanResponse</a></code>
- <code title="delete /v1/collections/{id}/users/{user_id}">client.collections.users.<a href="./src/nebula/resources/collections/users.py">remove</a>(user_id, \*, id) -> <a href="./src/nebula/types/nebula_results_generic_boolean_response.py">NebulaResultsGenericBooleanResponse</a></code>

# Memories

Types:

```python
from nebula.types import (
    IngestionConfig,
    IngestionMode,
    SearchMode,
    MemoryAppendResponse,
    MemoryDeleteMultipleResponse,
    MemorySearchResponse,
)
```

Methods:

- <code title="post /v1/memories">client.memories.<a href="./src/nebula/resources/memories/memories.py">create</a>(\*\*<a href="src/nebula/types/memory_create_params.py">params</a>) -> object</code>
- <code title="get /v1/memories/{id}">client.memories.<a href="./src/nebula/resources/memories/memories.py">retrieve</a>(id) -> <a href="./src/nebula/types/memories/nebula_results_engram_response.py">NebulaResultsEngramResponse</a></code>
- <code title="patch /v1/memories/{id}">client.memories.<a href="./src/nebula/resources/memories/memories.py">update</a>(id, \*\*<a href="src/nebula/types/memory_update_params.py">params</a>) -> <a href="./src/nebula/types/memories/nebula_results_engram_response.py">NebulaResultsEngramResponse</a></code>
- <code title="get /v1/memories">client.memories.<a href="./src/nebula/resources/memories/memories.py">list</a>(\*\*<a href="src/nebula/types/memory_list_params.py">params</a>) -> <a href="./src/nebula/types/collections/paginated_nebula_result_list_engram_response.py">PaginatedNebulaResultListEngramResponse</a></code>
- <code title="delete /v1/memories/{id}">client.memories.<a href="./src/nebula/resources/memories/memories.py">delete</a>(id) -> <a href="./src/nebula/types/nebula_results_generic_boolean_response.py">NebulaResultsGenericBooleanResponse</a></code>
- <code title="post /v1/memories/{id}/append">client.memories.<a href="./src/nebula/resources/memories/memories.py">append</a>(id, \*\*<a href="src/nebula/types/memory_append_params.py">params</a>) -> <a href="./src/nebula/types/memory_append_response.py">MemoryAppendResponse</a></code>
- <code title="post /v1/memories/{id}/deduplicate">client.memories.<a href="./src/nebula/resources/memories/memories.py">deduplicate_entities</a>(id, \*\*<a href="src/nebula/types/memory_deduplicate_entities_params.py">params</a>) -> <a href="./src/nebula/types/collections/nebula_results_generic_message_response.py">NebulaResultsGenericMessageResponse</a></code>
- <code title="delete /v1/memories/by-filter">client.memories.<a href="./src/nebula/resources/memories/memories.py">delete_by_filter</a>(\*\*<a href="src/nebula/types/memory_delete_by_filter_params.py">params</a>) -> <a href="./src/nebula/types/nebula_results_generic_boolean_response.py">NebulaResultsGenericBooleanResponse</a></code>
- <code title="post /v1/memories/delete">client.memories.<a href="./src/nebula/resources/memories/memories.py">delete_multiple</a>(\*\*<a href="src/nebula/types/memory_delete_multiple_params.py">params</a>) -> <a href="./src/nebula/types/memory_delete_multiple_response.py">MemoryDeleteMultipleResponse</a></code>
- <code title="get /v1/memories/{id}/download">client.memories.<a href="./src/nebula/resources/memories/memories.py">download_content</a>(id) -> None</code>
- <code title="get /v1/memories/download_zip">client.memories.<a href="./src/nebula/resources/memories/memories.py">download_zip</a>(\*\*<a href="src/nebula/types/memory_download_zip_params.py">params</a>) -> None</code>
- <code title="post /v1/memories/export">client.memories.<a href="./src/nebula/resources/memories/memories.py">export</a>(\*\*<a href="src/nebula/types/memory_export_params.py">params</a>) -> object</code>
- <code title="post /v1/memories/{id}/extract">client.memories.<a href="./src/nebula/resources/memories/memories.py">extract_entities</a>(id, \*\*<a href="src/nebula/types/memory_extract_entities_params.py">params</a>) -> <a href="./src/nebula/types/collections/nebula_results_generic_message_response.py">NebulaResultsGenericMessageResponse</a></code>
- <code title="get /v1/memories/{id}/chunks">client.memories.<a href="./src/nebula/resources/memories/memories.py">list_chunks</a>(id, \*\*<a href="src/nebula/types/memory_list_chunks_params.py">params</a>) -> <a href="./src/nebula/types/paginated_nebula_result_list_chunk_response.py">PaginatedNebulaResultListChunkResponse</a></code>
- <code title="get /v1/memories/{id}/collections">client.memories.<a href="./src/nebula/resources/memories/memories.py">list_collections</a>(id, \*\*<a href="src/nebula/types/memory_list_collections_params.py">params</a>) -> <a href="./src/nebula/types/paginated_nebula_result_list_collection_response.py">PaginatedNebulaResultListCollectionResponse</a></code>
- <code title="post /v1/memories/search">client.memories.<a href="./src/nebula/resources/memories/memories.py">search</a>(\*\*<a href="src/nebula/types/memory_search_params.py">params</a>) -> <a href="./src/nebula/types/memory_search_response.py">MemorySearchResponse</a></code>

## Metadata

Types:

```python
from nebula.types.memories import EngramResponse, NebulaResultsEngramResponse
```

Methods:

- <code title="patch /v1/memories/{id}/metadata">client.memories.metadata.<a href="./src/nebula/resources/memories/metadata.py">append</a>(id, \*\*<a href="src/nebula/types/memories/metadata_append_params.py">params</a>) -> <a href="./src/nebula/types/memories/nebula_results_engram_response.py">NebulaResultsEngramResponse</a></code>
- <code title="put /v1/memories/{id}/metadata">client.memories.metadata.<a href="./src/nebula/resources/memories/metadata.py">replace</a>(id, \*\*<a href="src/nebula/types/memories/metadata_replace_params.py">params</a>) -> <a href="./src/nebula/types/memories/nebula_results_engram_response.py">NebulaResultsEngramResponse</a></code>

## Entities

Types:

```python
from nebula.types.memories import PaginatedNebulaResultEntity
```

Methods:

- <code title="get /v1/memories/{id}/entities">client.memories.entities.<a href="./src/nebula/resources/memories/entities.py">list</a>(id, \*\*<a href="src/nebula/types/memories/entity_list_params.py">params</a>) -> <a href="./src/nebula/types/memories/paginated_nebula_result_entity.py">PaginatedNebulaResultEntity</a></code>
- <code title="post /v1/memories/{id}/entities/export">client.memories.entities.<a href="./src/nebula/resources/memories/entities.py">export</a>(id, \*\*<a href="src/nebula/types/memories/entity_export_params.py">params</a>) -> object</code>

## Relationships

Types:

```python
from nebula.types.memories import PaginatedNebulaResultRelationship
```

Methods:

- <code title="get /v1/memories/{id}/relationships">client.memories.relationships.<a href="./src/nebula/resources/memories/relationships.py">list</a>(id, \*\*<a href="src/nebula/types/memories/relationship_list_params.py">params</a>) -> <a href="./src/nebula/types/memories/paginated_nebula_result_relationship.py">PaginatedNebulaResultRelationship</a></code>
- <code title="post /v1/memories/{id}/relationships/export">client.memories.relationships.<a href="./src/nebula/resources/memories/relationships.py">export</a>(id, \*\*<a href="src/nebula/types/memories/relationship_export_params.py">params</a>) -> object</code>

# Graphs

Types:

```python
from nebula.types import GraphResponse, NebulaResultsGraphResponse, GraphListResponse
```

Methods:

- <code title="get /v1/graphs/{collection_id}">client.graphs.<a href="./src/nebula/resources/graphs/graphs.py">retrieve</a>(collection_id) -> <a href="./src/nebula/types/nebula_results_graph_response.py">NebulaResultsGraphResponse</a></code>
- <code title="post /v1/graphs/{collection_id}">client.graphs.<a href="./src/nebula/resources/graphs/graphs.py">update</a>(collection_id, \*\*<a href="src/nebula/types/graph_update_params.py">params</a>) -> <a href="./src/nebula/types/nebula_results_graph_response.py">NebulaResultsGraphResponse</a></code>
- <code title="get /v1/graphs">client.graphs.<a href="./src/nebula/resources/graphs/graphs.py">list</a>(\*\*<a href="src/nebula/types/graph_list_params.py">params</a>) -> <a href="./src/nebula/types/graph_list_response.py">GraphListResponse</a></code>
- <code title="post /v1/graphs/{collection_id}/reset">client.graphs.<a href="./src/nebula/resources/graphs/graphs.py">reset</a>(collection_id) -> <a href="./src/nebula/types/nebula_results_generic_boolean_response.py">NebulaResultsGenericBooleanResponse</a></code>

## Communities

Types:

```python
from nebula.types.graphs import Community, NebulaResultsCommunity, CommunityListResponse
```

Methods:

- <code title="post /v1/graphs/{collection_id}/communities">client.graphs.communities.<a href="./src/nebula/resources/graphs/communities.py">create</a>(collection_id, \*\*<a href="src/nebula/types/graphs/community_create_params.py">params</a>) -> <a href="./src/nebula/types/graphs/nebula_results_community.py">NebulaResultsCommunity</a></code>
- <code title="get /v1/graphs/{collection_id}/communities/{community_id}">client.graphs.communities.<a href="./src/nebula/resources/graphs/communities.py">retrieve</a>(community_id, \*, collection_id) -> <a href="./src/nebula/types/graphs/nebula_results_community.py">NebulaResultsCommunity</a></code>
- <code title="post /v1/graphs/{collection_id}/communities/{community_id}">client.graphs.communities.<a href="./src/nebula/resources/graphs/communities.py">update</a>(community_id, \*, collection_id, \*\*<a href="src/nebula/types/graphs/community_update_params.py">params</a>) -> <a href="./src/nebula/types/graphs/nebula_results_community.py">NebulaResultsCommunity</a></code>
- <code title="get /v1/graphs/{collection_id}/communities">client.graphs.communities.<a href="./src/nebula/resources/graphs/communities.py">list</a>(collection_id, \*\*<a href="src/nebula/types/graphs/community_list_params.py">params</a>) -> <a href="./src/nebula/types/graphs/community_list_response.py">CommunityListResponse</a></code>
- <code title="delete /v1/graphs/{collection_id}/communities/{community_id}">client.graphs.communities.<a href="./src/nebula/resources/graphs/communities.py">delete</a>(community_id, \*, collection_id) -> <a href="./src/nebula/types/nebula_results_generic_boolean_response.py">NebulaResultsGenericBooleanResponse</a></code>
- <code title="post /v1/graphs/{collection_id}/communities/build">client.graphs.communities.<a href="./src/nebula/resources/graphs/communities.py">build</a>(collection_id, \*\*<a href="src/nebula/types/graphs/community_build_params.py">params</a>) -> <a href="./src/nebula/types/collections/nebula_results_generic_message_response.py">NebulaResultsGenericMessageResponse</a></code>
- <code title="post /v1/graphs/{collection_id}/communities/export">client.graphs.communities.<a href="./src/nebula/resources/graphs/communities.py">export</a>(collection_id, \*\*<a href="src/nebula/types/graphs/community_export_params.py">params</a>) -> object</code>

## Entities

Types:

```python
from nebula.types.graphs import Entity, NebulaResultsEntity
```

Methods:

- <code title="post /v1/graphs/{collection_id}/entities">client.graphs.entities.<a href="./src/nebula/resources/graphs/entities.py">create</a>(collection_id, \*\*<a href="src/nebula/types/graphs/entity_create_params.py">params</a>) -> <a href="./src/nebula/types/graphs/nebula_results_entity.py">NebulaResultsEntity</a></code>
- <code title="get /v1/graphs/{collection_id}/entities/{entity_id}">client.graphs.entities.<a href="./src/nebula/resources/graphs/entities.py">retrieve</a>(entity_id, \*, collection_id) -> <a href="./src/nebula/types/graphs/nebula_results_entity.py">NebulaResultsEntity</a></code>
- <code title="post /v1/graphs/{collection_id}/entities/{entity_id}">client.graphs.entities.<a href="./src/nebula/resources/graphs/entities.py">update</a>(entity_id, \*, collection_id, \*\*<a href="src/nebula/types/graphs/entity_update_params.py">params</a>) -> <a href="./src/nebula/types/graphs/nebula_results_entity.py">NebulaResultsEntity</a></code>
- <code title="get /v1/graphs/{collection_id}/entities">client.graphs.entities.<a href="./src/nebula/resources/graphs/entities.py">list</a>(collection_id, \*\*<a href="src/nebula/types/graphs/entity_list_params.py">params</a>) -> <a href="./src/nebula/types/memories/paginated_nebula_result_entity.py">PaginatedNebulaResultEntity</a></code>
- <code title="delete /v1/graphs/{collection_id}/entities/{entity_id}">client.graphs.entities.<a href="./src/nebula/resources/graphs/entities.py">delete</a>(entity_id, \*, collection_id) -> <a href="./src/nebula/types/nebula_results_generic_boolean_response.py">NebulaResultsGenericBooleanResponse</a></code>
- <code title="post /v1/graphs/{collection_id}/entities/export">client.graphs.entities.<a href="./src/nebula/resources/graphs/entities.py">export</a>(collection_id, \*\*<a href="src/nebula/types/graphs/entity_export_params.py">params</a>) -> object</code>

## Relationships

Types:

```python
from nebula.types.graphs import NebulaResultsRelationship, Relationship
```

Methods:

- <code title="post /v1/graphs/{collection_id}/relationships">client.graphs.relationships.<a href="./src/nebula/resources/graphs/relationships.py">create</a>(collection_id, \*\*<a href="src/nebula/types/graphs/relationship_create_params.py">params</a>) -> <a href="./src/nebula/types/graphs/nebula_results_relationship.py">NebulaResultsRelationship</a></code>
- <code title="get /v1/graphs/{collection_id}/relationships/{relationship_id}">client.graphs.relationships.<a href="./src/nebula/resources/graphs/relationships.py">retrieve</a>(relationship_id, \*, collection_id) -> <a href="./src/nebula/types/graphs/nebula_results_relationship.py">NebulaResultsRelationship</a></code>
- <code title="post /v1/graphs/{collection_id}/relationships/{relationship_id}">client.graphs.relationships.<a href="./src/nebula/resources/graphs/relationships.py">update</a>(relationship_id, \*, collection_id, \*\*<a href="src/nebula/types/graphs/relationship_update_params.py">params</a>) -> <a href="./src/nebula/types/graphs/nebula_results_relationship.py">NebulaResultsRelationship</a></code>
- <code title="get /v1/graphs/{collection_id}/relationships">client.graphs.relationships.<a href="./src/nebula/resources/graphs/relationships.py">list</a>(collection_id, \*\*<a href="src/nebula/types/graphs/relationship_list_params.py">params</a>) -> <a href="./src/nebula/types/memories/paginated_nebula_result_relationship.py">PaginatedNebulaResultRelationship</a></code>
- <code title="delete /v1/graphs/{collection_id}/relationships/{relationship_id}">client.graphs.relationships.<a href="./src/nebula/resources/graphs/relationships.py">delete</a>(relationship_id, \*, collection_id) -> <a href="./src/nebula/types/nebula_results_generic_boolean_response.py">NebulaResultsGenericBooleanResponse</a></code>
- <code title="post /v1/graphs/{collection_id}/relationships/export">client.graphs.relationships.<a href="./src/nebula/resources/graphs/relationships.py">export</a>(collection_id, \*\*<a href="src/nebula/types/graphs/relationship_export_params.py">params</a>) -> object</code>

# Entities

Methods:

- <code title="post /v1/entities/{entity_id}/resolve-duplicate">client.entities.<a href="./src/nebula/resources/entities.py">resolve_duplicate</a>(entity_id, \*\*<a href="src/nebula/types/entity_resolve_duplicate_params.py">params</a>) -> object</code>
- <code title="get /v1/entities/{entity_id}/duplicates">client.entities.<a href="./src/nebula/resources/entities.py">retrieve_duplicates</a>(entity_id, \*\*<a href="src/nebula/types/entity_retrieve_duplicates_params.py">params</a>) -> object</code>

# Engrams

Methods:

- <code title="get /v1/engrams/{engram_id}/duplicate-stats">client.engrams.<a href="./src/nebula/resources/engrams.py">retrieve_duplicate_stats</a>(engram_id, \*\*<a href="src/nebula/types/engram_retrieve_duplicate_stats_params.py">params</a>) -> object</code>

# Prompts

Types:

```python
from nebula.types import PromptResponse, PromptRetrieveResponse, PromptListResponse
```

Methods:

- <code title="post /v1/prompts">client.prompts.<a href="./src/nebula/resources/prompts.py">create</a>(\*\*<a href="src/nebula/types/prompt_create_params.py">params</a>) -> <a href="./src/nebula/types/collections/nebula_results_generic_message_response.py">NebulaResultsGenericMessageResponse</a></code>
- <code title="post /v1/prompts/{name}">client.prompts.<a href="./src/nebula/resources/prompts.py">retrieve</a>(name, \*\*<a href="src/nebula/types/prompt_retrieve_params.py">params</a>) -> <a href="./src/nebula/types/prompt_retrieve_response.py">PromptRetrieveResponse</a></code>
- <code title="put /v1/prompts/{name}">client.prompts.<a href="./src/nebula/resources/prompts.py">update</a>(name, \*\*<a href="src/nebula/types/prompt_update_params.py">params</a>) -> <a href="./src/nebula/types/collections/nebula_results_generic_message_response.py">NebulaResultsGenericMessageResponse</a></code>
- <code title="get /v1/prompts">client.prompts.<a href="./src/nebula/resources/prompts.py">list</a>() -> <a href="./src/nebula/types/prompt_list_response.py">PromptListResponse</a></code>
- <code title="delete /v1/prompts/{name}">client.prompts.<a href="./src/nebula/resources/prompts.py">delete</a>(name) -> <a href="./src/nebula/types/nebula_results_generic_boolean_response.py">NebulaResultsGenericBooleanResponse</a></code>

# Retrieval

Types:

```python
from nebula.types import (
    GenerationConfig,
    Message,
    WebPageSearchResult,
    RetrievalEngageAgentResponse,
    RetrievalGenerateCompletionsResponse,
    RetrievalGenerateEmbeddingsResponse,
    RetrievalSearchResponse,
)
```

Methods:

- <code title="post /v1/retrieval/agent">client.retrieval.<a href="./src/nebula/resources/retrieval.py">engage_agent</a>(\*\*<a href="src/nebula/types/retrieval_engage_agent_params.py">params</a>) -> <a href="./src/nebula/types/retrieval_engage_agent_response.py">RetrievalEngageAgentResponse</a></code>
- <code title="post /v1/retrieval/rag">client.retrieval.<a href="./src/nebula/resources/retrieval.py">execute_rag_query</a>(\*\*<a href="src/nebula/types/retrieval_execute_rag_query_params.py">params</a>) -> object</code>
- <code title="post /v1/retrieval/completion">client.retrieval.<a href="./src/nebula/resources/retrieval.py">generate_completions</a>(\*\*<a href="src/nebula/types/retrieval_generate_completions_params.py">params</a>) -> <a href="./src/nebula/types/retrieval_generate_completions_response.py">RetrievalGenerateCompletionsResponse</a></code>
- <code title="post /v1/retrieval/embedding">client.retrieval.<a href="./src/nebula/resources/retrieval.py">generate_embeddings</a>(\*\*<a href="src/nebula/types/retrieval_generate_embeddings_params.py">params</a>) -> <a href="./src/nebula/types/retrieval_generate_embeddings_response.py">RetrievalGenerateEmbeddingsResponse</a></code>
- <code title="post /v1/retrieval/search">client.retrieval.<a href="./src/nebula/resources/retrieval.py">search</a>(\*\*<a href="src/nebula/types/retrieval_search_params.py">params</a>) -> <a href="./src/nebula/types/retrieval_search_response.py">RetrievalSearchResponse</a></code>

# Marketplace

## Collections

Types:

```python
from nebula.types.marketplace import CollectionAddResponse
```

Methods:

- <code title="get /v1/marketplace/collections/{collection_id}">client.marketplace.collections.<a href="./src/nebula/resources/marketplace/collections.py">retrieve</a>(collection_id) -> <a href="./src/nebula/types/nebula_results_collection_response.py">NebulaResultsCollectionResponse</a></code>
- <code title="get /v1/marketplace/collections">client.marketplace.collections.<a href="./src/nebula/resources/marketplace/collections.py">list</a>(\*\*<a href="src/nebula/types/marketplace/collection_list_params.py">params</a>) -> <a href="./src/nebula/types/paginated_nebula_result_list_collection_response.py">PaginatedNebulaResultListCollectionResponse</a></code>
- <code title="post /v1/marketplace/collections/{collection_id}/add">client.marketplace.collections.<a href="./src/nebula/resources/marketplace/collections.py">add</a>(collection_id) -> <a href="./src/nebula/types/marketplace/collection_add_response.py">CollectionAddResponse</a></code>

# Analytics

## Collections

### Centrality

Types:

```python
from nebula.types.analytics.collections import CentralityComputeResponse, CentralityStatusResponse
```

Methods:

- <code title="post /v1/analytics/collections/{collection_id}/centrality/compute">client.analytics.collections.centrality.<a href="./src/nebula/resources/analytics/collections/centrality.py">compute</a>(collection_id, \*\*<a href="src/nebula/types/analytics/collections/centrality_compute_params.py">params</a>) -> <a href="./src/nebula/types/analytics/collections/centrality_compute_response.py">CentralityComputeResponse</a></code>
- <code title="get /v1/analytics/collections/{collection_id}/centrality/status">client.analytics.collections.centrality.<a href="./src/nebula/resources/analytics/collections/centrality.py">status</a>(collection_id) -> <a href="./src/nebula/types/analytics/collections/centrality_status_response.py">CentralityStatusResponse</a></code>

# Health

Methods:

- <code title="get /v1/health">client.health.<a href="./src/nebula/resources/health.py">check</a>() -> <a href="./src/nebula/types/collections/nebula_results_generic_message_response.py">NebulaResultsGenericMessageResponse</a></code>

# Version

Methods:

- <code title="get /v1/version">client.version.<a href="./src/nebula/resources/version.py">retrieve</a>() -> object</code>

# Management

Methods:

- <code title="post /v1/management/sync-subscription">client.management.<a href="./src/nebula/resources/management.py">sync_subscription</a>() -> object</code>

# Plans

Methods:

- <code title="get /v1/plans">client.plans.<a href="./src/nebula/resources/plans.py">list</a>() -> object</code>

# Usage

Methods:

- <code title="get /v1/usage">client.usage.<a href="./src/nebula/resources/usage/usage.py">retrieve</a>() -> object</code>

## Tokens

Methods:

- <code title="get /v1/usage/tokens">client.usage.tokens.<a href="./src/nebula/resources/usage/tokens.py">retrieve_current_month</a>() -> object</code>
- <code title="get /v1/usage/tokens/history">client.usage.tokens.<a href="./src/nebula/resources/usage/tokens.py">retrieve_history</a>(\*\*<a href="src/nebula/types/usage/token_retrieve_history_params.py">params</a>) -> object</code>

# System

Types:

```python
from nebula.types import SystemRetrieveSettingsResponse, SystemRetrieveStatusResponse
```

Methods:

- <code title="get /v1/system/settings">client.system.<a href="./src/nebula/resources/system.py">retrieve_settings</a>() -> <a href="./src/nebula/types/system_retrieve_settings_response.py">SystemRetrieveSettingsResponse</a></code>
- <code title="get /v1/system/status">client.system.<a href="./src/nebula/resources/system.py">retrieve_status</a>() -> <a href="./src/nebula/types/system_retrieve_status_response.py">SystemRetrieveStatusResponse</a></code>

# Secrets

Types:

```python
from nebula.types import (
    SecretInitializeResponse,
    SecretRetrieveHistoryResponse,
    SecretRetrieveStatusResponse,
    SecretRotateResponse,
    SecretUpdateConfigResponse,
)
```

Methods:

- <code title="post /v1/secrets/initialize">client.secrets.<a href="./src/nebula/resources/secrets/secrets.py">initialize</a>(\*\*<a href="src/nebula/types/secret_initialize_params.py">params</a>) -> <a href="./src/nebula/types/secret_initialize_response.py">SecretInitializeResponse</a></code>
- <code title="get /v1/secrets/history">client.secrets.<a href="./src/nebula/resources/secrets/secrets.py">retrieve_history</a>(\*\*<a href="src/nebula/types/secret_retrieve_history_params.py">params</a>) -> <a href="./src/nebula/types/secret_retrieve_history_response.py">SecretRetrieveHistoryResponse</a></code>
- <code title="get /v1/secrets/status">client.secrets.<a href="./src/nebula/resources/secrets/secrets.py">retrieve_status</a>(\*\*<a href="src/nebula/types/secret_retrieve_status_params.py">params</a>) -> <a href="./src/nebula/types/secret_retrieve_status_response.py">SecretRetrieveStatusResponse</a></code>
- <code title="post /v1/secrets/rotate">client.secrets.<a href="./src/nebula/resources/secrets/secrets.py">rotate</a>(\*\*<a href="src/nebula/types/secret_rotate_params.py">params</a>) -> <a href="./src/nebula/types/secret_rotate_response.py">SecretRotateResponse</a></code>
- <code title="put /v1/secrets/config">client.secrets.<a href="./src/nebula/resources/secrets/secrets.py">update_config</a>(\*\*<a href="src/nebula/types/secret_update_config_params.py">params</a>) -> <a href="./src/nebula/types/secret_update_config_response.py">SecretUpdateConfigResponse</a></code>

## Scheduler

Types:

```python
from nebula.types.secrets import SchedulerStartResponse, SchedulerStopResponse
```

Methods:

- <code title="post /v1/secrets/scheduler/start">client.secrets.scheduler.<a href="./src/nebula/resources/secrets/scheduler.py">start</a>() -> <a href="./src/nebula/types/secrets/scheduler_start_response.py">SchedulerStartResponse</a></code>
- <code title="post /v1/secrets/scheduler/stop">client.secrets.scheduler.<a href="./src/nebula/resources/secrets/scheduler.py">stop</a>() -> <a href="./src/nebula/types/secrets/scheduler_stop_response.py">SchedulerStopResponse</a></code>

# Webhooks

Types:

```python
from nebula.types import (
    WebhookGetStatsResponse,
    WebhookListEventsResponse,
    WebhookScheduleCleanupResponse,
    WebhookTriggerCleanupResponse,
)
```

Methods:

- <code title="get /v1/webhooks/stats">client.webhooks.<a href="./src/nebula/resources/webhooks.py">get_stats</a>() -> <a href="./src/nebula/types/webhook_get_stats_response.py">WebhookGetStatsResponse</a></code>
- <code title="get /v1/webhooks/events">client.webhooks.<a href="./src/nebula/resources/webhooks.py">list_events</a>(\*\*<a href="src/nebula/types/webhook_list_events_params.py">params</a>) -> <a href="./src/nebula/types/webhook_list_events_response.py">WebhookListEventsResponse</a></code>
- <code title="post /v1/webhooks/schedule-cleanup">client.webhooks.<a href="./src/nebula/resources/webhooks.py">schedule_cleanup</a>(\*\*<a href="src/nebula/types/webhook_schedule_cleanup_params.py">params</a>) -> <a href="./src/nebula/types/webhook_schedule_cleanup_response.py">WebhookScheduleCleanupResponse</a></code>
- <code title="post /v1/webhooks/cleanup">client.webhooks.<a href="./src/nebula/resources/webhooks.py">trigger_cleanup</a>(\*\*<a href="src/nebula/types/webhook_trigger_cleanup_params.py">params</a>) -> <a href="./src/nebula/types/webhook_trigger_cleanup_response.py">WebhookTriggerCleanupResponse</a></code>

# Billing

Methods:

- <code title="post /v1/billing/portal">client.billing.<a href="./src/nebula/resources/billing.py">create_billing_portal_session</a>(\*\*<a href="src/nebula/types/billing_create_billing_portal_session_params.py">params</a>) -> object</code>
- <code title="post /v1/billing/checkout">client.billing.<a href="./src/nebula/resources/billing.py">create_checkout_session</a>(\*\*<a href="src/nebula/types/billing_create_checkout_session_params.py">params</a>) -> object</code>
- <code title="post /v1/billing/webhook">client.billing.<a href="./src/nebula/resources/billing.py">handle_webhook</a>() -> object</code>

# Contradictions

Methods:

- <code title="post /v1/contradictions/{relationship_id}/cascade">client.contradictions.<a href="./src/nebula/resources/contradictions.py">cascade_invalidation</a>(relationship_id, \*\*<a href="src/nebula/types/contradiction_cascade_invalidation_params.py">params</a>) -> object</code>

# TemporalEvents

Methods:

- <code title="get /v1/temporal-events/{event_id}">client.temporal_events.<a href="./src/nebula/resources/temporal_events.py">retrieve</a>(event_id) -> object</code>
- <code title="get /v1/temporal-events/">client.temporal_events.<a href="./src/nebula/resources/temporal_events.py">list</a>(\*\*<a href="src/nebula/types/temporal_event_list_params.py">params</a>) -> object</code>

# Users

Types:

```python
from nebula.types import (
    NebulaResultsUser,
    StandardUser,
    StorageTypeLimit,
    SystemDefaults,
    Token,
    TokenResponse,
    UsageLimit,
    UserFetchLimitsResponse,
)
```

Methods:

- <code title="get /v1/users/{id}">client.users.<a href="./src/nebula/resources/users/users.py">retrieve</a>(id) -> <a href="./src/nebula/types/nebula_results_user.py">NebulaResultsUser</a></code>
- <code title="post /v1/users/{id}">client.users.<a href="./src/nebula/resources/users/users.py">update</a>(id, \*\*<a href="src/nebula/types/user_update_params.py">params</a>) -> <a href="./src/nebula/types/nebula_results_user.py">NebulaResultsUser</a></code>
- <code title="get /v1/users">client.users.<a href="./src/nebula/resources/users/users.py">list</a>(\*\*<a href="src/nebula/types/user_list_params.py">params</a>) -> <a href="./src/nebula/types/collections/paginated_nebula_result_list_user.py">PaginatedNebulaResultListUser</a></code>
- <code title="delete /v1/users/{id}">client.users.<a href="./src/nebula/resources/users/users.py">delete</a>(id, \*\*<a href="src/nebula/types/user_delete_params.py">params</a>) -> <a href="./src/nebula/types/nebula_results_generic_boolean_response.py">NebulaResultsGenericBooleanResponse</a></code>
- <code title="post /v1/users/change-password">client.users.<a href="./src/nebula/resources/users/users.py">change_password</a>(\*\*<a href="src/nebula/types/user_change_password_params.py">params</a>) -> <a href="./src/nebula/types/collections/nebula_results_generic_message_response.py">NebulaResultsGenericMessageResponse</a></code>
- <code title="post /v1/users/export">client.users.<a href="./src/nebula/resources/users/users.py">export</a>(\*\*<a href="src/nebula/types/user_export_params.py">params</a>) -> object</code>
- <code title="get /v1/users/{id}/limits">client.users.<a href="./src/nebula/resources/users/users.py">fetch_limits</a>(id) -> <a href="./src/nebula/types/user_fetch_limits_response.py">UserFetchLimitsResponse</a></code>
- <code title="get /v1/users/me">client.users.<a href="./src/nebula/resources/users/users.py">get_current_user</a>() -> <a href="./src/nebula/types/nebula_results_user.py">NebulaResultsUser</a></code>
- <code title="post /v1/users/login">client.users.<a href="./src/nebula/resources/users/users.py">login</a>(\*\*<a href="src/nebula/types/user_login_params.py">params</a>) -> <a href="./src/nebula/types/token_response.py">TokenResponse</a></code>
- <code title="post /v1/users/logout">client.users.<a href="./src/nebula/resources/users/users.py">logout</a>() -> <a href="./src/nebula/types/collections/nebula_results_generic_message_response.py">NebulaResultsGenericMessageResponse</a></code>
- <code title="post /v1/users/refresh-token">client.users.<a href="./src/nebula/resources/users/users.py">refresh_token</a>(\*\*<a href="src/nebula/types/user_refresh_token_params.py">params</a>) -> <a href="./src/nebula/types/token_response.py">TokenResponse</a></code>
- <code title="post /v1/users">client.users.<a href="./src/nebula/resources/users/users.py">register</a>(\*\*<a href="src/nebula/types/user_register_params.py">params</a>) -> <a href="./src/nebula/types/nebula_results_user.py">NebulaResultsUser</a></code>
- <code title="post /v1/users/request-password-reset">client.users.<a href="./src/nebula/resources/users/users.py">request_password_reset</a>(\*\*<a href="src/nebula/types/user_request_password_reset_params.py">params</a>) -> <a href="./src/nebula/types/collections/nebula_results_generic_message_response.py">NebulaResultsGenericMessageResponse</a></code>
- <code title="post /v1/users/reset-password">client.users.<a href="./src/nebula/resources/users/users.py">reset_password</a>(\*\*<a href="src/nebula/types/user_reset_password_params.py">params</a>) -> <a href="./src/nebula/types/collections/nebula_results_generic_message_response.py">NebulaResultsGenericMessageResponse</a></code>
- <code title="get /v1/user/metrics">client.users.<a href="./src/nebula/resources/users/users.py">retrieve_metrics</a>(\*\*<a href="src/nebula/types/user_retrieve_metrics_params.py">params</a>) -> object</code>
- <code title="post /v1/users/send-verification-email">client.users.<a href="./src/nebula/resources/users/users.py">send_verification_email</a>(\*\*<a href="src/nebula/types/user_send_verification_email_params.py">params</a>) -> <a href="./src/nebula/types/collections/nebula_results_generic_message_response.py">NebulaResultsGenericMessageResponse</a></code>
- <code title="post /v1/users/verify-email">client.users.<a href="./src/nebula/resources/users/users.py">verify_email</a>(\*\*<a href="src/nebula/types/user_verify_email_params.py">params</a>) -> <a href="./src/nebula/types/collections/nebula_results_generic_message_response.py">NebulaResultsGenericMessageResponse</a></code>

## Collections

Methods:

- <code title="post /v1/users/{id}/collections/{collection_id}">client.users.collections.<a href="./src/nebula/resources/users/collections.py">add</a>(collection_id, \*, id) -> <a href="./src/nebula/types/nebula_results_generic_boolean_response.py">NebulaResultsGenericBooleanResponse</a></code>
- <code title="get /v1/users/{id}/collections">client.users.collections.<a href="./src/nebula/resources/users/collections.py">get_all</a>(id, \*\*<a href="src/nebula/types/users/collection_get_all_params.py">params</a>) -> <a href="./src/nebula/types/paginated_nebula_result_list_collection_response.py">PaginatedNebulaResultListCollectionResponse</a></code>
- <code title="delete /v1/users/{id}/collections/{collection_id}">client.users.collections.<a href="./src/nebula/resources/users/collections.py">remove</a>(collection_id, \*, id) -> <a href="./src/nebula/types/nebula_results_generic_boolean_response.py">NebulaResultsGenericBooleanResponse</a></code>

## APIKeys

Types:

```python
from nebula.types.users import APIKeyCreateResponse, APIKeyListResponse
```

Methods:

- <code title="post /v1/users/{id}/api-keys">client.users.api_keys.<a href="./src/nebula/resources/users/api_keys.py">create</a>(id, \*\*<a href="src/nebula/types/users/api_key_create_params.py">params</a>) -> <a href="./src/nebula/types/users/api_key_create_response.py">APIKeyCreateResponse</a></code>
- <code title="get /v1/users/{id}/api-keys">client.users.api_keys.<a href="./src/nebula/resources/users/api_keys.py">list</a>(id) -> <a href="./src/nebula/types/users/api_key_list_response.py">APIKeyListResponse</a></code>
- <code title="delete /v1/users/{id}/api-keys/{key_id}">client.users.api_keys.<a href="./src/nebula/resources/users/api_keys.py">delete</a>(key_id, \*, id) -> <a href="./src/nebula/types/nebula_results_generic_boolean_response.py">NebulaResultsGenericBooleanResponse</a></code>

## OAuth

### Google

Types:

```python
from nebula.types.users.oauth import LoginResponse
```

Methods:

- <code title="get /v1/users/oauth/google/authorize">client.users.oauth.google.<a href="./src/nebula/resources/users/oauth/google.py">authorize</a>() -> <a href="./src/nebula/types/collections/nebula_results_generic_message_response.py">NebulaResultsGenericMessageResponse</a></code>
- <code title="get /v1/users/oauth/google/callback">client.users.oauth.google.<a href="./src/nebula/resources/users/oauth/google.py">callback</a>(\*\*<a href="src/nebula/types/users/oauth/google_callback_params.py">params</a>) -> <a href="./src/nebula/types/users/oauth/login_response.py">LoginResponse</a></code>

### GitHub

Methods:

- <code title="get /v1/users/oauth/github/authorize">client.users.oauth.github.<a href="./src/nebula/resources/users/oauth/github.py">authorize</a>() -> <a href="./src/nebula/types/collections/nebula_results_generic_message_response.py">NebulaResultsGenericMessageResponse</a></code>
- <code title="get /v1/users/oauth/github/callback">client.users.oauth.github.<a href="./src/nebula/resources/users/oauth/github.py">callback</a>(\*\*<a href="src/nebula/types/users/oauth/github_callback_params.py">params</a>) -> <a href="./src/nebula/types/users/oauth/login_response.py">LoginResponse</a></code>

# Changelog

## 1.4.0 (2026-05-13)

Full Changelog: [v1.3.0...v1.4.0](https://github.com/nebula-agi/nebula-python/compare/v1.3.0...v1.4.0)

### Features

* Add workflow synthesis pipeline ([3114b85](https://github.com/nebula-agi/nebula-python/commit/3114b855bf5332f1b50abe3afc3bf5df5fc039ad))
* graph: unify TASK→EPISODIC + decouple Step 3.5+ from ingest ack ([e97e85b](https://github.com/nebula-agi/nebula-python/commit/e97e85b867bf48a4afd3b3dde1813cd48d200607))
* **internal/types:** support eagerly validating pydantic iterators ([2f24095](https://github.com/nebula-agi/nebula-python/commit/2f2409504df61e2fb2cfe67b42070c550b013d9b))
* **overview:** Shape A++ — additive scaffolding for Memories upload→list RYW ([4b05433](https://github.com/nebula-agi/nebula-python/commit/4b05433d7a5c5534b33ca11204fbbca9bb69989e))
* Rationale grounding + backfill outbox for v4 trace pipeline ([ed3b85f](https://github.com/nebula-agi/nebula-python/commit/ed3b85f0e1df0fdcbbfc991b27886aa36dec66ac))
* support setting headers via env ([04e9b84](https://github.com/nebula-agi/nebula-python/commit/04e9b8471757c020e86140bcfff73a3270ce8855))


### Bug Fixes

* **client:** add missing f-string prefix in file type error message ([f8aec65](https://github.com/nebula-agi/nebula-python/commit/f8aec65e6795d0832ec3ca916a9ed787ea053a9a))
* use correct field name format for multipart file arrays ([a94c864](https://github.com/nebula-agi/nebula-python/commit/a94c864b605eaa99941458dc897c2319396eeac3))


### Chores

* configure new SDK language ([16d124a](https://github.com/nebula-agi/nebula-python/commit/16d124a98eee3764259efc262d4c4c1d790a5d61))
* **internal:** reformat pyproject.toml ([6247618](https://github.com/nebula-agi/nebula-python/commit/6247618832b915cd5fd68c6c96d958ab7ecbeb9d))


### Documentation

* align SDK examples with nebula-sdk v1.3.0; fix stale router descriptions ([9d5d69a](https://github.com/nebula-agi/nebula-python/commit/9d5d69a56dd540f61c501e7dbb9f4dc9840c7a97))


### Refactors

* **engrams:** typed EngramKind + ConversationFields/DocumentFields substructure ([4e00a23](https://github.com/nebula-agi/nebula-python/commit/4e00a234ea52c0cd1b1a5b2d063dfe8687736dee))

## 1.3.0 (2026-04-27)

Full Changelog: [v1.2.2...v1.3.0](https://github.com/nebula-agi/nebula-python/compare/v1.2.2...v1.3.0)

### Features

* [codex] Clean up replayed playground memories ([0dfc69d](https://github.com/nebula-agi/nebula-python/commit/0dfc69df82f36929e528241e9a3ab2a2d593daa4))
* [codex] Fix EngramResponse OpenAPI example ([e30c479](https://github.com/nebula-agi/nebula-python/commit/e30c4791c3b84853e87c88ed7ce19809540ebc2c))
* [codex] Harden memory write validation contracts ([d55ce58](https://github.com/nebula-agi/nebula-python/commit/d55ce58c5b61eee2f468b5c054645e151fe8ec64))
* add nebula devex facade ([327f061](https://github.com/nebula-agi/nebula-python/commit/327f0610830c345b4899ecc4255ba6d6c4e78b55))
* api: honor chunks_limit on memory listing ([659d3c3](https://github.com/nebula-agi/nebula-python/commit/659d3c331dd4812b534172d1b8984b85a0723be9))
* engram: replace generated summaries with deterministic engram_context ([11e00ee](https://github.com/nebula-agi/nebula-python/commit/11e00ee6197de3b4c93f5c5d59a89f15b6a3d9ec))
* NQL overhaul v2 - clean cherry-pick baseline from [#526](https://github.com/nebula-agi/nebula-python/issues/526) ([c8d1366](https://github.com/nebula-agi/nebula-python/commit/c8d1366109d2726246a960707e5c9debb0ee2b2c))
* Remove legacy append chunk IDs from public contract ([ec543ad](https://github.com/nebula-agi/nebula-python/commit/ec543ad4d7f04996656a7ab8f6d362d47cf43b1e))
* Rename MemoryRecall response fields to adjective-uniform shape ([d3fda51](https://github.com/nebula-agi/nebula-python/commit/d3fda5130620ff961b5956a8ab8957e5a3375cd8))
* sdks/python: SnapshotEnvelope dataclass + typed export/import/search/add ([d4850d3](https://github.com/nebula-agi/nebula-python/commit/d4850d31ad4ae0c0a3234b3ea01db2d352ff74bd))
* Stabilize memory create SDK response schema ([54223f7](https://github.com/nebula-agi/nebula-python/commit/54223f7d3b3c24c23850e4b4bc4f9d0a625232ba))


### Bug Fixes

* harden dx facade compatibility ([#5](https://github.com/nebula-agi/nebula-python/issues/5)) ([219492f](https://github.com/nebula-agi/nebula-python/commit/219492ff070d2d39ccc0de609a11574669fdb6c4))
* **types:** allow pyright to infer TypedDict types within SequenceNotStr ([426e1c2](https://github.com/nebula-agi/nebula-python/commit/426e1c2d4c530a2524bc5b2d5790f8afd365e457))
* use async_to_httpx_files in patch method ([db8be2a](https://github.com/nebula-agi/nebula-python/commit/db8be2a29c33dc0d71d457ccecb5c3c96c6f9845))


### Chores

* add missing docstrings ([0393792](https://github.com/nebula-agi/nebula-python/commit/0393792d11323c21520ccd5693ef9c8e43c7a47e))
* **internal:** add `--fix` argument to lint script ([afa73fd](https://github.com/nebula-agi/nebula-python/commit/afa73fdf311affde54f5b0437adff64a77838c30))
* **internal:** add missing files argument to base client ([e79b5f7](https://github.com/nebula-agi/nebula-python/commit/e79b5f73aff54fb3ee2b5c54755ef054ce26e6f9))
* **internal:** more robust bootstrap script ([6da9e21](https://github.com/nebula-agi/nebula-python/commit/6da9e21c7c0c101c193d0b62e21ec68f6fc63c23))
* seed release baseline ([#4](https://github.com/nebula-agi/nebula-python/issues/4)) ([1561427](https://github.com/nebula-agi/nebula-python/commit/15614278e6459e97d6c0bc29b635fd4773a43ceb))
* speedup initial import ([01adfc0](https://github.com/nebula-agi/nebula-python/commit/01adfc08053fa2371c6264ed30b4978b38160b27))
* update SDK settings ([41a4a78](https://github.com/nebula-agi/nebula-python/commit/41a4a78c5944d902e5687fe9ace59d4ae818c37a))
* update SDK settings ([936b50a](https://github.com/nebula-agi/nebula-python/commit/936b50a4ba506394068cf52b2c5d470f43eadf23))
* update SDK settings ([cd61be2](https://github.com/nebula-agi/nebula-python/commit/cd61be2877083366a050c5a8b5413e21dea49519))
* update SDK settings ([b5d5785](https://github.com/nebula-agi/nebula-python/commit/b5d5785a1b33d55e78f5b68ab10d6377342f5d3d))
* update SDK settings ([54d2013](https://github.com/nebula-agi/nebula-python/commit/54d20131ca419a57c75f6779506e3937a1cca0e5))
* update SDK settings ([576c1f0](https://github.com/nebula-agi/nebula-python/commit/576c1f07cb7f7f8dd771092eb1ad85578cb060e6))
* update SDK settings ([631893f](https://github.com/nebula-agi/nebula-python/commit/631893f6398b13445e1e0ccaf21f5ea6c3aae50a))


### Refactors

* **internal:** switch from rye to uv ([cb98a73](https://github.com/nebula-agi/nebula-python/commit/cb98a7357bb6fdbb0e6609780f914fcc3bb8f692))

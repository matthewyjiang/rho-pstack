---
name: principle-migrate-callers-then-delete-legacy-apis
description: "Apply when introducing a new internal API while old callers still exist. Migrate callers and delete the old API in the same wave instead of preserving compatibility layers."
disable-model-invocation: false
---

# Migrate Callers Then Delete Legacy APIs

Read [the workflow contract](../../references/workflow-contract.md).

Identify every consumer before replacing an internal API. Migrate callers and
remove the obsolete route together when coordinated change is safe. External
compatibility, published versioning and repository migration policy take priority;
do not treat unknown consumers as nonexistent. Validate the supported path before
removing the old one. This does not authorize deleting unrelated APIs.

- Update tests to assert the new contract, and delete tests that only protect pre-refactor implementation details

**When this applies:**
- No external users depend on backward compatibility
- The project can absorb coordinated breaking changes
- The new API is part of a simplification or refactor initiative

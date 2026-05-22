# Package Policy

Mode: `offline_existing_binaries_only`.

This example assumes an offline server may have a machine-wide package inventory, but no such inventory is included in the public repository.

Codex must not assume that a package missing from a project `renv` subset is unavailable on the server. The complete machine/server inventory should be attached in a real private project when available.

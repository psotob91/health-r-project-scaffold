# Package policy

Mode: `<online_installs_allowed | package_requests_only | offline_existing_binaries_only | offline_locked_verify_only | offline_global_cache_renv | offline_local_repo_renv>`

Codex must follow this policy before proposing or installing R packages.

- `online_installs_allowed`: online installs may be used, but every package must be recorded in `metadata/package_inventory_or_request.csv`.
- `package_requests_only`: do not install; document requested packages.
- `offline_existing_binaries_only`: assume the offline server has preinstalled binaries, but each project renv library still needs restore or reinstall from those local binaries.
- `offline_locked_verify_only`: do not install or hydrate packages; only verify an already prepared project library.
- `offline_global_cache_renv`: a separate setup/bootstrap may hydrate or locally install project packages from approved global/site libraries and local renv cache.
- `offline_local_repo_renv`: a separate setup/bootstrap may hydrate or locally install from an approved local repository or package cellar.

Package inventory scope matters:

- `machine_universal_inventory`: complete package inventory for the server or PC.
- `project_renv_subset`: only the packages currently included in this project's renv.
- `scope_unknown`: do not infer availability; ask for clarification.

Do not assume that a package missing from a project renv subset is unavailable on the offline server. The server may have a larger universal binary inventory.

For mirror/server workflows, server-bound package notes belong in `server_payload/docs/offline_package_policy.md`.

Analytic scripts must never contain package installs, downloads, GitHub/remotes or internet repositories. Bootstrap-capable offline modes require an explicit package registry, install log, `renv::snapshot()` evidence and `renv::status()` evidence.

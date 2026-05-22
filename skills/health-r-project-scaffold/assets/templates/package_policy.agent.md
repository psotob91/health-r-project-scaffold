# Package policy

Mode: `<online_installs_allowed | package_requests_only | offline_existing_binaries_only>`

Codex must follow this policy before proposing or installing R packages.

- `online_installs_allowed`: online installs may be used, but every package must be recorded in `metadata/package_inventory_or_request.csv`.
- `package_requests_only`: do not install; document requested packages.
- `offline_existing_binaries_only`: assume the offline server has preinstalled binaries, but each project renv library still needs restore or reinstall from those local binaries.

Package inventory scope matters:

- `machine_universal_inventory`: complete package inventory for the server or PC.
- `project_renv_subset`: only the packages currently included in this project's renv.
- `scope_unknown`: do not infer availability; ask for clarification.

Do not assume that a package missing from a project renv subset is unavailable on the offline server. The server may have a larger universal binary inventory.

For mirror/server workflows, server-bound package notes belong in `server_payload/docs/offline_package_policy.md`.

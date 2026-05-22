# Offline package policy

The offline server must not download packages from the internet.

If packages already exist as server binaries, the project still needs a project-local renv restore or reinstall from those binaries. Record package availability and restore status in `metadata-public/package_inventory_or_request.csv` or `metadata-private/package_inventory_or_request.csv`.

Package lists must state their scope:

- complete server/PC package inventory;
- project-specific renv subset;
- unknown scope.

If only the project renv subset is available, attach the complete server/PC package inventory later or explicitly waive that requirement. Do not assume that packages absent from this project's renv are absent from the server.

Do not add new packages silently. If a package is missing, document the request and validation need.

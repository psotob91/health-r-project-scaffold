# renv restore notes

This folder documents project-local renv restoration for offline server use.

Offline servers may already have many package binaries installed, but a new renv project still needs its own project library restored or populated from approved local binaries.

The server package inventory and a project renv lockfile are different artifacts. The server inventory may be much larger. A project renv should use only the subset needed for that project.

If the complete server/PC inventory is not available, record it as pending in `metadata/open_questions.csv` or `metadata-public/open_questions.csv`.

Do not download from the internet on the offline server.

For `offline_global_cache_renv` projects, run a separate setup/bootstrap script
before any analytic pipeline step. The bootstrap should read an explicit package
registry, hydrate the project library from approved global/site libraries and
local `renv` cache, log every package action, run `renv::snapshot()` and
`renv::status()`, and write review evidence.

For server-first offline projects, do not rely on a laptop-created `renv.lock`
for the first server bootstrap. Create the lockfile on the server after the
project library has been populated from approved offline sources.

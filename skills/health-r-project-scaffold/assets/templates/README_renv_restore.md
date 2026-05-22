# renv restore notes

This folder documents project-local renv restoration for offline server use.

Offline servers may already have many package binaries installed, but a new renv project still needs its own project library restored or populated from approved local binaries.

The server package inventory and a project renv lockfile are different artifacts. The server inventory may be much larger. A project renv should use only the subset needed for that project.

If the complete server/PC inventory is not available, record it as pending in `metadata/open_questions.csv` or `metadata-public/open_questions.csv`.

Do not download from the internet on the offline server.

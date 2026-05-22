# renv Restore Notes

This public example does not include a lockfile.

For offline server workflows, attach the complete machine/server package inventory in the private project, then choose a project-specific `renv` subset. A package missing from one project `renv` subset should not be treated as unavailable on the server.

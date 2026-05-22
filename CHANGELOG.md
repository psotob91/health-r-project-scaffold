# Changelog

## v0.1.0 - 2026-05-22

First public pilot release.

### Added

- `health-r-project-scaffold` skill.
- Independent input-axis classification for project content, package status, data status, and environment.
- Reduced and extended scaffold guidance.
- Offline, online-agent, and offline-with-online-mirror workflow support.
- `server_payload/` transfer contract for offline server workflows.
- Package inventory scope policy for machine-wide inventories versus project `renv` subsets.
- Encoding decision guidance for Japanese and other encoding-sensitive text inputs.
- Warning-resolution form contract.
- Safe Plan Request Inbox contract for submitted warning answers and uploaded planning evidence.
- Sanitized minimal examples.

### Boundaries

- No R analysis code generation.
- No package installation.
- No dependency downloads.
- No real raw data or private metadata included.

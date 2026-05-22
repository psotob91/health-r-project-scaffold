# AGENTS.md

This is an agent-enabled online mirror for a simulated health research scaffold.

## Rules

- Use `health-r-project-scaffold` only for project architecture, metadata, package policy, transfer guidance, and scaffold validation.
- Use a separate coding-standards skill for future R analysis code generation or review.
- Keep future production scripts only under `server_payload/scripts/`.
- Keep agent notes outside `server_payload/`.
- Do not install packages unless the project package policy explicitly allows it.

## Transfer Boundary

Only `server_payload/` is copied to the offline code server.

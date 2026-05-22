# MEMORY.md

## Project Context

- Project name: `<project_name>`
- Decision path: `<decision_path>`
- Structure: `<reduced_or_extended>`
- Storage layout: `<single_root_or_split_root>`
- Data status: `<simulated_real_unknown>`

## Package Policy

`<package_policy>`

## Data Rules

- Raw real data belong only in protected locations.
- Simulated mirror data must be labelled simulated.
- IDs, linkage keys, dates and postal-code-like fields are sensitive by design.

## Agent Boundary

Agent files stay in agent-enabled roots and must not be copied to clean offline server roots unless explicitly approved.

## Server Payload

When this project uses an online mirror, `server_payload/` is the only folder copied to the offline code server. Keep exploratory agent notes outside it. Put future production scripts in `server_payload/scripts/`.

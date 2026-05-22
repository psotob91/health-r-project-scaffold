# AGENTS.md

## Project Rule

This project is a health research R project. Prioritize auditability, reproducibility, privacy and simple human-readable structure.

## Package Policy

Follow `docs/agent_context/package_policy.md`. Do not install packages unless the policy explicitly allows it.

## Coding Standards

For any R code generation, code review, refactor or style decision, use the future health R coding-standards skill. This scaffold skill is only for project architecture and metadata organization.

## Data Safety

Treat all IDs, linkage keys, dates, postal-code-like fields and private metadata as sensitive by design. Do not copy real data into agent or online roots unless explicitly approved.

## Transfer Safety

Do not transfer `.codex/`, `.agents/`, `AGENTS.md`, `MEMORY.md` or `docs/agent_context/` to offline server roots unless the transfer guide explicitly allows it.

In mirror/server workflows, production scripts and server-bound documentation must be created under `server_payload/`. Future R production scripts belong in `server_payload/scripts/` so the server transfer remains a single curated copy operation.

---
name: health-r-project-scaffold
description: Set up or reorganize folder architecture, metadata, README/docs, agent context, offline/online package policy, renv guidance, transfer instructions, and validation reports for R health research projects. Use when creating a new project from an empty folder, organizing existing raw data/metadata/ERD/package lists, preparing online mirrors for offline servers, or splitting code/docs from protected data roots. This skill does not create R analysis code, ingest scripts, modeling code, or coding-standard enforcement.
---

# Health R Project Scaffold

## Mission

Create simple, auditable, human-readable R health research project scaffolds. The skill only creates or reorganizes project architecture, metadata and documentation. It must not write analysis code.

## Boundary

Do:

- create folders, README/docs, `.gitignore`, `.Rprofile`, config templates and metadata templates;
- inventory available data, metadata, ERD, package lists and notes;
- infer minimal metadata only as `inferred_low`;
- create architecture, validation and transfer HTML reports;
- isolate agent-only files from offline server roots.
- create small scaffold utilities for warning close-out or encoding audit when they remain clearly separate from analysis scripts.
- create a safe Plan Request Inbox for warning-form submissions that Codex can review in the current conversation.

Do not:

- create R analysis, ingest, derive, modeling or reporting scripts;
- install packages or download dependencies;
- silently move raw or sensitive files;
- mark inferred metadata as verified.

Scaffold utilities must not be placed in production analysis script folders unless they are meant to run on the server as part of the project workflow. In mirror/server workflows, production analysis scripts still belong only in `server_payload/scripts/`.

## Required References

Read only as needed:

- `references/decision_algorithm.md`: decision tree, required questions and validation rules.
- `references/project_structures.md`: reduced, extended, online mirror, offline server and code/data split layouts.
- `references/output_contract.md`: exact required artifacts and HTML report requirements.

Use `../health-r-data-steward/references/standards_research.md` only for standards rationale when needed. Keep implementation simpler than the reference whenever possible.

## Initial Workflow

1. Inspect the target folder before asking questions.
2. Classify available inputs on independent axes, not as mutually exclusive branches:
   - content axis: empty folder, data present, metadata/dictionary present, ERD/schema present, notes/protocol present, codelists/mappings present;
   - package axis: no package information, machine/server universal inventory present, project `renv` subset present, package scope unknown, complete inventory pending, package policy unknown;
   - data status axis: simulated, real or unknown;
   - environment axis: online with agent, offline no mirror, offline with online mirror.
3. Ask only blocking interactive questions that cannot be answered from files.
4. Select and record the decision-tree path in `config/project.yml`.
5. Generate the scaffold for the selected path.
6. Validate the scaffold.
7. Repair safe structural issues and rerun validation.
8. Stop only at `OK_SO_FAR`, `WARNING_PENDING_HUMAN_DECISION`, or `BLOCKED`.

## Mandatory Question Style

Ask short direct questions with quick choices. Each question must map to a decision-tree branch or unresolved safety item.

Examples:

- "Use reduced or extended structure?"
- "Environment: online with agent, offline no mirror, or offline with online mirror?"
- "Storage: single protected root or code/data split?"
- "Are available data simulated, real, or unknown?"
- "Can the online mirror download new R packages?"
- "Does the offline server restore renv only from existing local binaries?"
- "Is this package list the complete server/PC package inventory, or only this project's renv subset?"

Do not ask questions that can be answered from the folder contents.

## Input Completeness Rules

Minimum to create structure:

- project name or folder name;
- online/offline/mirror path;
- single-root or split-root storage;
- reduced or extended structure;
- simulated, real or unknown data status.

Minimum to make raw data understandable:

- source inventory;
- sensitivity classification;
- table/file role;
- suspected IDs and key fields;
- encoding decision for text/Japanese files;
- open questions for grain, keys, date meanings, code systems and ERD contradictions.

Minimum to configure R safely:

- package policy: online installs allowed, package requests only, or offline existing binaries only;
- renv strategy;
- package inventory scope: complete machine/server inventory, project `renv` subset, or unknown;
- package list if present, otherwise a package inventory/request template;
- `.Rprofile` guardrails;
- agent instructions when agent support exists.

If a package list is provided but scope is unclear, record `scope_unknown`, warn, and ask the user to classify it. If only a project `renv` subset exists, warn that the complete server/PC package inventory should be attached or explicitly waived, because packages absent from the project `renv` may still be available as server binaries.

## Server Payload Rule

When an online mirror will feed an offline server, create a single curated transfer root:

```text
server_payload/
```

Only `server_payload/` may be copied to the offline code server. Agent context, drafts, prompts and exploratory notes must stay outside it.

In mirror/server workflows:

- place all server-bound README/docs/config/metadata templates under `server_payload/`;
- place future production scripts only under `server_payload/scripts/`;
- place agent context under `.codex/`, `.agents/`, `AGENTS.md`, `MEMORY.md`, `docs/agent_context/` and `workspace_notes/`, outside `server_payload/`;
- fail validation if server-bound scripts/docs/config are scattered outside `server_payload/`;
- fail validation if `.codex/`, `.agents/`, `AGENTS.md`, `MEMORY.md` or `docs/agent_context/` appear inside `server_payload/`.

## Online/Offline Mirror Policy

For online laptop plus offline server projects, scaffold the laptop as a
rehearsal of the server rather than a separate architecture:

- `server_payload/` is the only code/docs/config root copied to the offline
  server;
- laptop paths should emulate server roots through explicit environment
  variables, for example code on the project payload root and protected data
  roots equivalent to server `D:` and `Z:`;
- real raw data, harmonized outputs, derived data and QC outputs must stay in
  protected data roots, not inside the code payload;
- `AGENTS.md`, `MEMORY.md`, `.codex/`, `.agents/` and agent notes stay outside
  the payload unless the user explicitly requests a server-side agent context;
- generate both laptop-online and server-offline execution manuals with exact
  folder setup, environment variables, bootstrap order, script order and review
  artifacts;
- record package policy, package inventory scope, `renv` strategy, internet
  policy, D/Z-style root mapping and open/closed human decisions in config and
  metadata.

Recognized offline package policies:

- `offline_locked_verify_only`: project code may verify an already prepared
  project library, but must not hydrate or install packages.
- `offline_global_cache_renv`: setup/bootstrap may populate a project `renv`
  from approved global/site libraries and local `renv` cache, with no internet.
- `offline_local_repo_renv`: setup/bootstrap may populate a project `renv` from
  an approved local repository/cellar, with no internet.

When `renv` is server-first, do not require a laptop `renv.lock` as an initial
server input. Treat `renv.lock` as a bootstrap output created from the server's
actual package versions, and document that `00_check_environment.R` or the
analytic pipeline runs only after bootstrap evidence exists.

## Agent Context Rules

Only create agent files in agent-enabled roots:

- `AGENTS.md`;
- `MEMORY.md` or `docs/agent_context/project_memory.md`;
- `.codex/`;
- `.agents/`;
- `docs/agent_context/`.

`AGENTS.md` must instruct Codex to use the future health R coding-standards skill for code generation, code review or coding-style decisions.

Server-only offline roots must not contain agent traces unless the user explicitly requests them.

## Validation Requirement

Always create these in the active metadata root (`metadata/`, `metadata-public/` or `metadata-private/` according to the selected path):

- `scaffold_validation_checklist.csv`;
- `open_questions.csv`;
- `warning_resolution_form.csv` when validation status is `WARNING_PENDING_HUMAN_DECISION`;
- `docs/scaffold_validation_report.html`;
- `docs/project_architecture.html`;
- `docs/warning_resolution_form.html` when validation status is `WARNING_PENDING_HUMAN_DECISION`;
- `docs/server_transfer_guide.html` when any server/offline path exists.

Validation must check:

- correct decision-tree path;
- required artifacts for that path;
- input axes recorded separately in `config/project.yml`;
- agent artifacts isolated correctly;
- server roots clean of agent traces;
- mirror/server metadata and project IDs match;
- all server-bound artifacts live under `server_payload/` in online mirror projects;
- future script location is documented as `server_payload/scripts/`;
- package policy embedded in README, `.Rprofile`, agent docs when relevant;
- package inventory scope is known or recorded as an open question;
- project `renv` subset is not treated as the complete server/PC package inventory;
- no dangerous inference marked verified.
- every `WARNING_PENDING_HUMAN_DECISION` item has a close-out row with closed choices and free text in `warning_resolution_form.csv`.

Report status:

- `OK_SO_FAR`;
- `WARNING_PENDING_HUMAN_DECISION`;
- `BLOCKED`.

When status is `WARNING_PENDING_HUMAN_DECISION`, create a human-fillable close-out form in both CSV and HTML. The form must include closed-choice options, a free-text clarification field, evidence path, decision owner and date. The validation report must link directly to the form.

If the environment can run a local helper without installing packages, the warning form should support interactive submission to that helper and a no-helper fallback export. The helper may update only scaffold metadata and validation files; it must not touch raw data or create analysis outputs.

When the form accepts uploaded evidence, uploads must be staged as planning inputs only. The helper must write a plan-intake package under the active metadata root, including a manifest, a machine-readable JSON payload and a Codex Plan Mode prompt. Uploaded files must never be copied automatically into raw data, private metadata, production scripts or protected server roots.

Prefer the safe Plan Request Inbox pattern for interactive warning forms:

- write each submitted request under `plan_requests/<timestamp>/` in the active metadata root;
- include `request.json`, `request_manifest.csv`, `codex_plan_prompt.md` and `REQUEST_STATUS.md`;
- set `request_status` to `pending_codex_plan_review`;
- instruct the analyst to tell Codex: `review latest scaffold plan request`;
- do not launch Codex, install packages, run analysis, move files, or close risky warnings automatically.

Validation must compare current status across `config/project.yml`, `scaffold_validation_checklist.csv`, README/MEMORY files, HTML reports and current request/intake files. Historical intake artifacts may remain for audit only if they are explicitly marked `superseded_by_iteration`; otherwise status mismatches must become `WARNING_PENDING_HUMAN_DECISION` or `BLOCKED`.

For Japanese or other encoding-sensitive text inputs, test candidate encodings on headers or small previews only. Record tested encodings, scores, recommended encoding, evidence and rationale separately from semantic readability status. Encoding detection alone is not proof that labels are meaningful.

## Completion Response

When scaffolding is performed, report:

- selected decision path;
- validation status;
- files/folders created or reorganized;
- unresolved questions;
- links to architecture, validation and transfer HTML reports.

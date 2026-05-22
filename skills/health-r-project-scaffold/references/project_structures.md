# Project Structures

## Reduced Online Agent Project

```text
project-online/
|- AGENTS.md
|- MEMORY.md
|- README.md
|- .Rprofile
|- .gitignore
|- config/
|- metadata/
|- docs/
|  |- agent_context/
|  |- project_architecture.html
|  |- scaffold_validation_report.html
|  `- server_transfer_guide.html
|- data_simulated/
`- .codex/
```

## Offline Server, No Mirror

```text
project-server/
|- README.md
|- .Rprofile
|- .gitignore
|- config/
|- metadata-private/
|- raw/
|- external/
|- derived/
|- analytic/
|- outputs-private/
|- logs-private/
`- docs/
   |- project_architecture.html
   `- scaffold_validation_report.html
```

## Offline With Online Mirror And Code/Data Split

```text
project-mirror/
|- AGENTS.md
|- MEMORY.md
|- .codex/
|- docs/
|  |- agent_context/
|  `- agent_notes.md
|- workspace_notes/
|- server_payload/
|  |- README.md
|  |- .Rprofile
|  |- .gitignore
|  |- config/
|  |- metadata-public/
|  |- docs/
|  |  |- server_transfer_guide.html
|  |  |- scaffold_validation_report.html
|  |  |- project_architecture.html
|  |  `- offline_package_policy.md
|  |- scripts/
|  |  `- README_scripts.md
|  `- renv/
|     `- README_renv_restore.md
|- data_simulated/
`- README.md

project-server-code/
`- <contents copied from project-mirror/server_payload/>

project-server-protected/
|- raw/
|- external/
|- metadata-private/
|- derived/
|- analytic/
|- outputs-private/
`- logs-private/
```

## Offline With Online Mirror And Single Protected Root

```text
project-mirror/
|- AGENTS.md
|- MEMORY.md
|- .codex/
|- docs/agent_context/
|- workspace_notes/
|- server_payload/
|  |- README.md
|  |- .Rprofile
|  |- .gitignore
|  |- config/
|  |- metadata-public/
|  |- docs/
|  |- scripts/
|  `- renv/
`- data_simulated/

project-server/
|- <contents copied from project-mirror/server_payload/>
|- raw/
|- external/
|- metadata-private/
|- derived/
|- analytic/
|- outputs-private/
`- logs-private/
```

## Server Payload Rules

- Only `server_payload/` is copied to the offline code server.
- Agent files stay outside `server_payload/`.
- Future production scripts go in `server_payload/scripts/`.
- Agent exploratory notes, prompts and drafts stay in `workspace_notes/` or `docs/agent_context/`.
- Validation fails if server-bound scripts, docs or config are scattered outside `server_payload/`.
- Validation fails if agent artifacts appear inside `server_payload/`.

## Extended Additions

Add only when justified by multiple sources, real sensitive server workflows, ERD/dictionaries, repeated audits, multiple analysts, package transfer complexity, codelists or mappings.

```text
metadata/
|- source_inventory.csv
|- data_dictionary_inferred.csv
|- relocation_plan.csv
|- open_questions.csv
|- scaffold_validation_checklist.csv
|- package_inventory_or_request.csv
|- encoding_decisions.csv
|- codelists/
|- mappings/
`- decisions/

docs/
|- project_architecture.html
|- scaffold_validation_report.html
|- server_transfer_guide.html
|- offline_package_policy.md
`- agent_context/
```

## Agent Isolation

Agent-only artifacts:

- `.codex/`
- `.agents/`
- `AGENTS.md`
- `MEMORY.md`
- `docs/agent_context/`

These belong only in online or mirror roots unless the user explicitly requests an exception. They must not be placed in `server_payload/`.

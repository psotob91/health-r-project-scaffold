# Decision Algorithm

Use this as both human-readable flowchart and implementation checklist.

```mermaid
flowchart TD
    A["Start: empty or existing project folder"] --> B["Inventory available inputs"]
    B --> C["Classify independent input axes"]
    C --> C1["Content axis"]
    C --> C2["Package axis"]
    C --> C3["Data status axis"]
    C --> C4["Environment axis"]

    C1 -->|Empty folder| D["Ask setup questions"]
    C1 -->|Data present, metadata missing| E["Infer metadata as inferred_low + ask data meaning questions"]
    C1 -->|Metadata/ERD present, data missing| F["Create metadata-first scaffold + ask raw data location questions"]
    C1 -->|Data + metadata/ERD| G["Reconcile inputs + ask contradictions only"]
    C2 -->|Package info missing| H["Ask package policy questions"]
    C2 -->|Package info present| H2["Record package/renv facts"]

    D --> I{"Environment path?"}
    E --> I
    F --> I
    G --> I
    H --> I
    H2 --> I

    I -->|Online / agent available| J["Online agent project"]
    I -->|Offline no mirror| K["Server-only offline project"]
    I -->|Offline with online mirror| L["Online mirror + offline server projects with server_payload"]

    J --> M{"Storage layout?"}
    K --> M
    L --> M

    M -->|Single protected root| N["One-root layout"]
    M -->|Code/data split| O["Two-root layout"]

    N --> P{"Reduced or extended?"}
    O --> P

    P -->|Reduced| Q["Reduced scaffold"]
    P -->|Extended| R["Extended scaffold"]

    Q --> S["Generate docs, metadata, package policy, server_payload as needed, validation, HTML"]
    R --> S

    S --> T["Validate decision path, input axes, agent isolation, server_payload, mirror fidelity, transfer rules"]
    T --> T2["Validate global status consistency across config, checklist, docs, memory and request/intake files"]
    T2 --> U{"Validation status"}
    U -->|OK_SO_FAR| V["Final reports + links"]
    U -->|WARNING_PENDING_HUMAN_DECISION| W["Interactive questions + open_questions.csv + warning_resolution_form.csv/html"]
    U -->|BLOCKED| X["Stop, explain blocker, ask required question"]

    W --> T
    X --> T
```

## Input Axes

Record these axes separately in `config/project.yml`. They are compatible with each other, not mutually exclusive.

| axis | possible values |
|---|---|
| content | empty_folder; data_present; metadata_dictionary_present; erd_schema_present; notes_protocol_present; codelists_mappings_initial_present; codelists_mappings_derived_present |
| package | no_package_information; machine_universal_inventory_present; project_renv_subset_present; scope_unknown; complete_inventory_pending; renv_lock_present; package_policy_unknown |
| data_status | simulated; real; unknown |
| environment | online_with_agent; offline_no_mirror; offline_with_online_mirror |

Example: `data_present + package_list_missing + simulated + offline_with_online_mirror` is valid.

## Blocking Questions

Use these only when not discoverable from files.

| decision | question | choices |
|---|---|---|
| structure | Should this project use reduced or extended structure? | reduced; extended |
| environment | What environment path applies? | online with agent; offline no mirror; offline with online mirror |
| storage | Where will sensitive raw data and private metadata live? | single protected root; code/data split |
| data status | Are available data simulated, real or unknown? | simulated; real; unknown |
| package policy | Can the project download new R packages? | yes online; no package requests only; offline existing binaries only |
| package scope | Is this package list the complete server/PC package inventory, or only this project's renv subset? | complete machine/server inventory; project renv subset; unknown |
| renv | How should renv be handled offline? | restore from existing local binaries; document package requests only |
| server transfer | Should agent files be excluded from server transfer? | yes; no explicit exception |

## Server Payload Validation

In online mirror workflows:

- all server-bound artifacts must live under `server_payload/`;
- no `.codex/`, `.agents/`, `AGENTS.md`, `MEMORY.md` or `docs/agent_context/` may exist inside `server_payload/`;
- no production server-bound scripts, docs or config may be scattered outside `server_payload/`;
- `server_payload/` must be copyable as one unit to the offline server code root;
- future production scripts must be documented as belonging in `server_payload/scripts/`.
- scaffold-only utilities may live under `server_payload/tools/` if they are documented as non-analysis utilities and do not touch raw/protected data.

## Validation Checks

Validation must confirm:

- `config/project.yml` records selected environment, storage layout, structure level and data status.
- `config/project.yml` records content, package, data status and environment axes separately.
- Required artifacts exist for the selected path.
- Agent files exist only in agent-enabled roots.
- Server roots contain no `.codex/`, `.agents/`, `AGENTS.md`, `MEMORY.md`, or agent orchestrator docs unless explicitly allowed.
- Mirror and server scaffolds share project ID, metadata schema, source inventory, package plan and transfer contract.
- Simulated mirror data are labelled simulated.
- Real-data destinations are labelled protected.
- Package policy is embedded in README, `.Rprofile`, `AGENTS.md`/`MEMORY.md` when relevant, and package docs.
- Package inventory scope is explicit: complete machine/server inventory, project renv subset, or unknown.
- If package scope is unknown, `open_questions.csv` includes a required scope question.
- If status is `WARNING_PENDING_HUMAN_DECISION`, `warning_resolution_form.csv` and `docs/warning_resolution_form.html` exist and link each warning to closed choices plus a free-text field.
- If encoding-sensitive text inputs are present, tested encodings, preview evidence and a recommended setup are recorded separately from human semantic readability status.
- If only a project renv subset exists, validation warns that the complete server/PC package inventory is pending unless explicitly waived.
- Packages missing from a project renv subset are not assumed unavailable on the server.
- No `inferred_low` or `inferred_medium` value is marked verified.
- Open questions remain visible until answered.
- Current status is consistent across `config/project.yml`, `scaffold_validation_checklist.csv`, README/MEMORY files, HTML reports and current plan request files.
- Historical intake/request artifacts with older statuses are marked `superseded_by_iteration` or they trigger a warning.

## Plan Request Inbox

When an interactive warning form submits answers or uploads, prefer a safe Plan Request Inbox under the active metadata root:

- `plan_requests/<timestamp>/request.json`
- `plan_requests/<timestamp>/request_manifest.csv`
- `plan_requests/<timestamp>/codex_plan_prompt.md`
- `plan_requests/<timestamp>/REQUEST_STATUS.md`
- `plan_requests/<timestamp>/uploads/`

The request status starts as `pending_codex_plan_review`. The user-facing instruction is the short chat command: `review latest scaffold plan request`. The helper must not launch Codex Desktop or a separate Codex CLI session.

## Status Rules

- `OK_SO_FAR`: all checks pass for answered decisions.
- `WARNING_PENDING_HUMAN_DECISION`: scaffold is usable but questions remain.
- `BLOCKED`: unsafe to transfer or use.

# Output Contract

## Required Metadata

Create these in the active metadata root. Depending on the selected path, the active metadata root may be `metadata/`, `metadata-public/` or `metadata-private/`.

- `source_inventory.csv`
- `relocation_plan.csv`
- `open_questions.csv`
- `scaffold_validation_checklist.csv`
- `package_inventory_or_request.csv`
- `encoding_decisions.csv`
- `warning_resolution_form.csv` when validation status is `WARNING_PENDING_HUMAN_DECISION`

Use `data_dictionary_inferred.csv` when raw data or metadata are available but no verified dictionary exists.

## Required Docs

- `README.md`
- `docs/project_architecture.html`
- `docs/scaffold_validation_report.html`
- `docs/warning_resolution_form.html` when validation status is `WARNING_PENDING_HUMAN_DECISION`
- `docs/server_transfer_guide.html` when server or offline paths exist
- `docs/offline_package_policy.md` for offline paths
- `docs/agent_context/package_policy.md` for agent-enabled paths
- `server_payload/docs/offline_package_policy.md` for online mirror workflows
- `server_payload/scripts/README_scripts.md` for online mirror workflows
- `server_payload/renv/README_renv_restore.md` for online mirror workflows

## Required Config

- `config/project.yml`
- `config/paths.example.yml`
- optional `config/paths.local.template.yml`
- `.gitignore`
- `.Rprofile`

In online mirror workflows, server-bound config, docs, metadata templates, `.Rprofile`, `.gitignore`, and future scripts must live under `server_payload/`.

## Architecture HTML Must Include

- selected decision-tree path;
- independent input classification axes;
- project tree or trees;
- `server_payload/` tree when relevant;
- every created, modified or reorganized artifact;
- purpose of each artifact;
- sensitivity class;
- transfer status;
- whether artifact is agent-only;
- whether artifact is copied to server;
- links to related metadata and reports.

## Validation HTML Must Include

- validation status;
- checklist summary;
- direct links for face validity:
  - architecture report;
  - source inventory;
  - relocation plan;
  - open questions;
  - package/renv plan;
  - encoding decisions;
  - transfer guide;
  - validation checklist.
  - warning resolution form when status is `WARNING_PENDING_HUMAN_DECISION`.

## Warning Resolution Form

When validation status is `WARNING_PENDING_HUMAN_DECISION`, create:

- `warning_resolution_form.csv`;
- `docs/warning_resolution_form.html`.

Required columns:

- `question_id`;
- `topic`;
- `blocking_level`;
- `allowed_decisions`;
- `selected_decision`;
- `free_text_response`;
- `evidence_path`;
- `decided_by`;
- `decided_at`;
- `rerun_validation_required`.

The HTML form is for face validity and manual completion. It must not imply that decisions are saved automatically unless an implementation explicitly supports writing the CSV.

When a local helper is generated, it must:

- accept submitted answers from the HTML form;
- update only scaffold metadata such as `warning_resolution_form.csv`, `warning_resolution_answers.json` and validation checklist status;
- support a dry-run/test submission mode;
- avoid installing packages, accessing internet or touching raw data.
- when file uploads are enabled, stage uploaded files only under the active metadata root and create a plan-intake manifest plus Codex Plan Mode prompt.

The HTML form must include a no-helper fallback that exports answers to a local JSON or CSV file for manual upload or later processing.

## Plan Intake From Warning Forms

When the warning form is used as a Plan Mode intake, create these under the active metadata root:

- `pending_plan_intake/plan_intake.json`;
- `pending_plan_intake/plan_intake_manifest.csv`;
- `pending_plan_intake/codex_plan_prompt.md`;
- `pending_plan_intake/uploads/<timestamp>/` for uploaded evidence.

The prompt must instruct Codex to propose the next scaffold iteration in Plan Mode, not execute it. The helper must not move uploaded evidence into production locations or mark it verified.

## Plan Request Inbox

The preferred warning-form handoff is the safe Plan Request Inbox. On each submit, create a timestamped request under the active metadata root:

- `plan_requests/<timestamp>/request.json`;
- `plan_requests/<timestamp>/request_manifest.csv`;
- `plan_requests/<timestamp>/codex_plan_prompt.md`;
- `plan_requests/<timestamp>/REQUEST_STATUS.md`;
- `plan_requests/<timestamp>/uploads/` for request-specific uploaded evidence.

The request JSON must include `request_status = pending_codex_plan_review`. The HTML form should tell the analyst to write the short chat instruction `review latest scaffold plan request`. The helper must not launch Codex Desktop or the Codex CLI because that can create a separate, unaudited session. Older `pending_plan_intake/` artifacts may be retained for audit, but mark them `superseded_by_iteration` when a later scaffold iteration closes or replaces them.

## Global Status Consistency

Validation must compare the current scaffold status across:

- `config/project.yml`;
- `scaffold_validation_checklist.csv`;
- root or payload `README.md`;
- agent `MEMORY.md` when present;
- validation, architecture and transfer HTML reports;
- current Plan Request Inbox files;
- legacy `pending_plan_intake/` and `warning_resolution_answers.json`.

If a historical artifact contains an older status, it must either be updated or explicitly marked `superseded_by_iteration`. Otherwise the validation report must not claim `OK_SO_FAR`.

## Encoding Decisions

For text and delimited files, `encoding_decisions.csv` should distinguish:

- detection candidates from tools;
- candidate encodings actually tested;
- scoring evidence from previews;
- `encoding_recommended`;
- `semantic_readability_status`;
- final human decision status.

For `.dta`, `.sas7bdat`, `.sav` and similar statistical raw files, prefer metadata-preserving readers such as `haven` when available and approved. Do not treat these as plain text encoding problems.

## Transfer Guide Must Include

- `server_payload/` as the only online-to-offline code transfer source when mirror mode is used;
- what to copy to server code root;
- what to create or copy to protected data root;
- what must never be copied;
- how to handle agent artifacts;
- how to handle renv/package restoration;
- what must be manually validated before real-data use.

## Package Policy Placement

For online agent or mirror workflows, package policy must appear in:

- `AGENTS.md`;
- `MEMORY.md`;
- `docs/agent_context/package_policy.md`;
- `server_payload/docs/offline_package_policy.md`;
- `server_payload/.Rprofile`.

Allowed policy modes:

- `online_installs_allowed`: Codex may propose or install packages online, but must record them in package metadata.
- `package_requests_only`: Codex must document package requests and not install.
- `offline_existing_binaries_only`: Codex must assume the server has preinstalled binaries but renv still needs project-local restore or reinstall from those binaries.

Validation fails if the selected package policy is missing from any required location.

## Package Inventory Scope

Any package list must be classified as one of:

- `machine_universal_inventory`: complete package inventory for the server or PC;
- `project_renv_subset`: packages currently included in one project `renv`;
- `scope_unknown`: package list exists but its scope is not known.

If only `project_renv_subset` is available, validation must warn that the complete server/PC inventory is pending unless the analyst explicitly waives it. Do not infer that a package missing from a project `renv` subset is unavailable on the offline server.

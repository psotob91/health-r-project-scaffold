# <project_name>

## Purpose

Describe the study, data domain, population, period and expected analysis context before real-data use.

## Environment Model

- Decision path: `<online_agent | offline_no_mirror | offline_with_online_mirror>`
- Structure: `<reduced | extended>`
- Storage layout: `<single_protected_root | code_data_split>`
- Data status: `<simulated | real | unknown>`
- Package policy: `<online_installs_allowed | package_requests_only | offline_existing_binaries_only>`

## Data Safety

Treat all IDs, linkage keys, clinical dates, postal-code-like fields and private metadata as sensitive in the real workflow. Simulated mirrors must remain clearly labelled as simulated.

## Key Reports

- `docs/project_architecture.html`
- `docs/scaffold_validation_report.html`
- `docs/server_transfer_guide.html`
- `metadata/open_questions.csv`

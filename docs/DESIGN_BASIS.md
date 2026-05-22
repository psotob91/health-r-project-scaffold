# Design Basis

`health-r-project-scaffold` is a practical Codex skill for creating auditable R project scaffolds in health research. It is not a formal compliance framework and does not claim certification against any external standard. Instead, it combines and adapts well-established principles that are commonly useful in epidemiology, claims/EHR projects, registry studies, observational studies, and privacy-sensitive analytical workflows.

## Adapted Principles

### Reproducible Research Organization

The scaffold separates project roles so that a reviewer can quickly identify what belongs to source metadata, configuration, scripts, documentation, derived outputs, protected data, and validation artifacts. The goal is to make a project understandable before analysis starts.

### Raw-Data Immutability And Provenance

Raw data should be inventoried, classified, and documented before any transformation. The scaffold encourages source inventories, relocation plans, checksums when available, encoding decisions, and open questions. It avoids silent moves or silent reinterpretation of raw inputs.

### Metadata-First Health Data Stewardship

Health projects often fail later because table grain, identifiers, dates, codelists, code mappings, or package constraints were left implicit. This skill therefore creates metadata and decision artifacts early:

- source inventory;
- inferred or template data dictionary;
- package inventory or request template;
- open questions;
- relocation plan;
- encoding decisions;
- validation checklist;
- warning-resolution or Plan Request Inbox artifacts when needed.

### Sensitive-By-Design Field Treatment

The skill treats IDs, linkage keys, clinical dates, postal-code-like fields, facility identifiers, member identifiers, claim identifiers, local restricted codes, private paths, and small-cell notes as sensitive by design in real workflows. Simulated examples may be public, but they should preserve the same structural caution as the real workflow they represent.

### Offline And Mirror Workflows

Many health-data projects use an online laptop or workstation for planning and an offline server for protected data. The skill supports that pattern by separating:

- agent-only context in the online mirror;
- a curated `server_payload/` for code and public metadata transfer;
- protected server roots for raw data, private metadata, derived data, private outputs, and logs.

The core transfer rule is simple: only `server_payload/` is copied to the offline code server. Agent notes, prompts, exploratory drafts, uploaded planning evidence, and simulated mirror data stay outside the server-transferable payload unless explicitly approved.

### R And `renv` Reproducibility

The skill does not install R packages or create analysis code. It documents package policy and distinguishes:

- complete machine or server package inventories;
- project-specific `renv` subsets;
- package-request-only workflows;
- offline restoration from approved local binaries.

This distinction prevents a common mistake: assuming that a package missing from a project `renv` subset is unavailable on the offline server.

### Encoding-Aware Japanese Data Workflows

For Japanese and other encoding-sensitive sources, the skill requires encoding decisions to be documented separately from semantic readability. Detecting UTF-8 or another encoding is not enough; labels and metadata still need human review when readability or upstream mojibake is uncertain.

### Codex Skill Progressive Disclosure

The skill follows Codex skill design principles:

- `SKILL.md` stays operational and concise enough for normal use;
- detailed contracts live in `references/`;
- reusable output templates live in `assets/templates/`;
- public repo documentation lives outside the skill folder;
- validation scripts are repo-level release utilities, not part of the runtime skill contract.

## Workflow Algorithm

The scaffold workflow is intentionally conservative:

1. Inspect the target folder.
2. Classify available inputs on independent axes:
   - content;
   - package information;
   - data status;
   - environment.
3. Ask only blocking questions that cannot be answered from files.
4. Select environment path, storage layout, and structure level.
5. Create the scaffold and metadata artifacts.
6. Keep agent context outside server-transferable folders.
7. Validate the decision path, required artifacts, package policy, metadata status, transfer boundaries, and global status consistency.
8. Stop with one of three statuses:
   - `OK_SO_FAR`;
   - `WARNING_PENDING_HUMAN_DECISION`;
   - `BLOCKED`.

## Why The Folder Structure Looks This Way

The structure is designed around auditability and transfer safety rather than aesthetics.

- `config/` stores project and path configuration templates.
- `metadata-public/` stores public or simulated metadata that can travel with code.
- `metadata-private/` belongs in protected storage when metadata itself is restricted.
- `docs/` stores human-reviewable HTML reports and transfer guidance.
- `scripts/` is reserved for future production scripts, but this skill does not generate analysis scripts.
- `renv/` stores restore notes or future project reproducibility assets.
- `server_payload/` is the only online-to-offline code transfer root in mirror workflows.
- `raw/`, `derived/`, `analytic/`, `outputs-private/`, and `logs-private/` belong in protected server storage when real data are used.
- `AGENTS.md`, `MEMORY.md`, `.codex/`, and `docs/agent_context/` are agent-only mirror artifacts and must not enter `server_payload/`.

## Limitations

This skill creates a scaffold, not an analysis pipeline. It cannot decide whether real data are safe to publish, whether a codelist is scientifically valid, whether a statistical method is appropriate, or whether a server package policy is institutionally approved. Those decisions remain human responsibilities and should be recorded in the scaffold artifacts.

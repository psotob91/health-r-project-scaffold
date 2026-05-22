# Health R Project Scaffold

First public pilot release of a Codex skill for setting up auditable R project scaffolds for health research.

This skill creates project folders, metadata templates, package policy notes, offline/server transfer guidance, validation checklists, and simple HTML review reports. It is designed for epidemiology, claims/EHR, clinical registry, observational study, and related health-data projects where human review, reproducibility, and data-boundary clarity matter.

## What This Skill Does

- Sets up reduced or extended project scaffolds.
- Supports online-agent, offline-only, and offline-with-online-mirror workflows.
- Keeps agent context separate from server-transferable payloads.
- Creates metadata-first artifacts such as source inventories, relocation plans, package policy notes, encoding decision templates, open questions, and validation checklists.
- Uses a `server_payload/` transfer model for online mirror to offline server workflows.
- Supports a safe Plan Request Inbox pattern for warning-resolution form submissions.

## What This Skill Does Not Do

- It does not create R analysis, ingestion, modeling, or reporting code.
- It does not install R packages.
- It does not download dependencies.
- It does not move real raw data silently.
- It does not mark inferred metadata as verified without human review.

## Design Basis And Adapted Standards

This skill is not an arbitrary folder template. Its structure and workflow are adapted from a combination of reproducible research practice, R project organization, health-data stewardship, offline/server workflows, and Codex skill-design guidance.

The scaffold emphasizes:

- **Reproducible research structure**: keep code, metadata, documentation, derived outputs, and protected data roles explicit.
- **Raw-data immutability**: inventory and document raw inputs before any relocation or transformation.
- **Metadata-first setup**: create source inventories, dictionaries, open questions, package policy, and validation artifacts before analysis code.
- **Health-data safety**: treat IDs, linkage keys, clinical dates, postal-like fields, facility identifiers, local restricted codes, and private paths as sensitive by design.
- **Offline and mirror workflows**: support privacy-sensitive projects where online agent work must be separated from offline server code and protected data.
- **R reproducibility**: document package policy and `renv` strategy while distinguishing complete machine inventories from project-specific `renv` subsets.
- **Codex progressive disclosure**: keep `SKILL.md` operational, with detailed workflow contracts in `references/` and reusable templates in `assets/`.

See [docs/DESIGN_BASIS.md](docs/DESIGN_BASIS.md) for the fuller rationale and workflow algorithm.

## Workflow Algorithm

At a high level, the skill follows this workflow:

1. Inspect the target folder before asking questions.
2. Classify inputs on independent axes: content, package information, data status, and environment.
3. Ask only blocking questions that cannot be answered from files.
4. Select reduced or extended structure and single-root or code/data split storage.
5. Generate the scaffold, metadata templates, package policy, transfer guidance, and HTML reports.
6. Keep agent-only context outside server-transferable payloads.
7. Validate decision path, input axes, package policy, metadata, transfer boundaries, and global status consistency.
8. Stop at `OK_SO_FAR`, `WARNING_PENDING_HUMAN_DECISION`, or `BLOCKED`.

## Repository Layout

```text
skills/
  health-r-project-scaffold/
    SKILL.md
    references/
    assets/templates/
examples/
  minimal_empty_project/
  minimal_mirror_with_simulated_metadata/
INSTALL.md
CHANGELOG.md
LICENSE
```

## Quick Install

Copy the skill folder into your Codex skills directory:

```powershell
$source = "skills\health-r-project-scaffold"
$target = "$HOME\.codex\skills\health-r-project-scaffold"
New-Item -ItemType Directory -Force $target
Copy-Item -Recurse -Force "$source\*" $target
```

Restart Codex Desktop after installation.

Once published to GitHub, the same skill can be installed with:

```powershell
python "$HOME\.codex\skills\.system\skill-installer\scripts\install-skill-from-github.py" `
  --url "https://github.com/psotob91/health-r-project-scaffold/tree/main/skills/health-r-project-scaffold"
```

## Basic Usage

In a new or existing project folder, ask Codex to use the skill:

```text
Use the health-r-project-scaffold skill to set up this empty folder for an offline-with-online-mirror R health research project.
```

The skill should inspect the folder first, ask only blocking questions, create the scaffold, and produce validation and architecture reports.

## Public Release Safety

This repository intentionally excludes raw health data, private metadata, server package inventories, local paths, uploaded evidence files, and large generated project outputs. Keep those in local or protected project folders, not in this public skill repository.

## Release Validation

Before publishing or tagging a release, run:

```powershell
python scripts\validate_public_release.py
python "$HOME\.codex\skills\.system\skill-creator\scripts\quick_validate.py" skills\health-r-project-scaffold
```

These checks reduce drift by validating the skill frontmatter, UI metadata, installation instructions, and public-safety exclusions.

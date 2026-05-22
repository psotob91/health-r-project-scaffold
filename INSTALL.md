# Installation

## Requirements

- Codex Desktop or another Codex environment that supports local skills.
- Windows PowerShell for the commands below.

The skill itself does not install R packages and does not require internet access at runtime.

## Install From A Local Clone

From the repository root:

```powershell
$source = "skills\health-r-project-scaffold"
$target = "$HOME\.codex\skills\health-r-project-scaffold"
New-Item -ItemType Directory -Force $target
Copy-Item -Recurse -Force "$source\*" $target
```

Restart Codex Desktop.

## Install From GitHub

After this repository is published, install the skill directly from GitHub with the Codex skill installer helper:

```powershell
python "$HOME\.codex\skills\.system\skill-installer\scripts\install-skill-from-github.py" `
  --url "https://github.com/psotob91/health-r-project-scaffold/tree/main/skills/health-r-project-scaffold"
```

If the destination already exists, remove or rename the old local skill folder first:

```powershell
Remove-Item -Recurse -Force "$HOME\.codex\skills\health-r-project-scaffold"
```

Restart Codex Desktop after installation.

## Verify Installation

Create an empty test folder:

```powershell
$testProject = "$HOME\Desktop\health-r-scaffold-test"
New-Item -ItemType Directory -Force $testProject
```

Then ask Codex:

```text
Use the health-r-project-scaffold skill to initialize this empty folder as a reduced simulated R health research project.
```

Expected behavior:

- Codex reads the skill.
- Codex inspects the folder before asking questions.
- Codex asks only blocking setup questions.
- Codex creates a scaffold with metadata, documentation, validation, and HTML review reports.

## Updating The Skill

Pull the latest repository version, then rerun the copy command:

```powershell
$source = "skills\health-r-project-scaffold"
$target = "$HOME\.codex\skills\health-r-project-scaffold"
Copy-Item -Recurse -Force "$source\*" $target
```

Restart Codex Desktop after updating.

## Offline Use

For privacy-sensitive environments, copy the installed skill folder to the offline machine manually:

```text
%USERPROFILE%\.codex\skills\health-r-project-scaffold\
```

Do not copy real raw data, private metadata, tokens, machine-specific package inventories, or local path files into this public repository.

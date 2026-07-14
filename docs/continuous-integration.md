# Continuous Integration

## Overview

The Employee Directory repository uses GitHub Actions to run the pytest
suite automatically.

Continuous integration checks application changes before they are merged
into the permanent branches.

## Workflow file

```text
.github/workflows/ci.yml
```

## Triggers

The workflow runs on:

- pull requests targeting `develop`;
- pull requests targeting `main`;
- pushes to `develop`;
- pushes to `main`;
- manual workflow execution.

## CI process

```text
Checkout repository
        ↓
Set up Python
        ↓
Restore pip cache
        ↓
Install test dependencies
        ↓
Run pytest
        ↓
Report status
```

## Python version

The workflow explicitly selects Python 3.14 to align CI with the current
home-lab server environment.

The version should be updated deliberately rather than relying on the
runner's default Python version.

## Dependency files

CI installs:

```text
app/requirements-test.txt
```

That file includes:

```text
app/requirements.txt
```

Both files are included in the pip cache key.

## Permissions

The workflow declares:

```yaml
permissions:
  contents: read
```

The CI job only needs to read the repository.

It does not need write access.

## Branch protection

The following branches require the `Pytest` status check:

```text
develop
main
```

Application changes should reach these branches through pull requests.

## Relationship to Ansible

GitHub Actions and the Ansible test gate serve related but separate
purposes.

### GitHub Actions

Runs when code is proposed or pushed on GitHub.

It provides early feedback and a required pull-request status check.

### Ansible test gate

Runs immediately before a staging or production deployment.

It tests the exact revision selected by the target inventory.

Keeping both controls provides defence in depth.

## Manual local test

```bash
cd ~/projects/employee-directory

source app/venv/bin/activate
python -m pip install -r app/requirements-test.txt
python -m pytest -v
deactivate
```

## Failure handling

When CI fails:

1. open the failed workflow;
2. locate the failed step;
3. read the pytest assertion or dependency error;
4. reproduce the failure locally;
5. correct the application or test;
6. commit and push the fix;
7. wait for CI to run again.

Do not bypass a valid failing check simply to merge a change.

## GitHub Actions CI fails

Open:

```text
Repository → Actions → Application CI
```

Select the failed run and expand the failed step.

### Dependency installation failure

Confirm these files exist:

```text
app/requirements.txt
app/requirements-test.txt
```

Run locally:

```bash
python -m pip install -r app/requirements-test.txt
```

### pytest failure

Run locally:

```bash
source app/venv/bin/activate
python -m pytest -v
deactivate
```

Correct the failed application behaviour or outdated assertion.

### Python version unavailable

Check the `Set up Python` output.

Use an explicit Python version supported by GitHub's runner and compatible
with the application.

### Workflow does not run

Confirm the workflow is stored at:

```text
.github/workflows/ci.yml
```

Confirm the pull request targets either:

```text
develop
main
```

### Required status check is unavailable

Allow the workflow to complete successfully in the repository first.

Then return to the branch protection configuration and select:

```text
Pytest
```

### GitHub Actions passes but deployment fails

CI tests application functionality in a clean hosted runner.

The deployment may still fail because of:

- SSH connectivity;
- UFW;
- Ansible configuration;
- systemd;
- Nginx;
- target-host permissions;
- environment-specific runtime state.

Use the Ansible and server troubleshooting procedures.

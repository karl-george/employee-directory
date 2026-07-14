## Pull-request and CI requirements

Application changes must use the following workflow:

```text
Feature branch
      ↓
Pull request to develop
      ↓
GitHub Actions Pytest check
      ↓
Merge to develop
      ↓
Ansible staging deployment
      ↓
Staging approval
      ↓
Pull request from develop to main
      ↓
GitHub Actions Pytest check
      ↓
Merge to main
      ↓
Ansible production deployment
```

Both `develop` and `main` are protected branches.

Do not routinely merge or push directly to either branch from the command
line.

### CI validation

A pull request must show a successful:

```text
Pytest
```

status check before it is merged.

CI success proves that the application test suite passed on a clean
GitHub-hosted runner.

It does not replace staging validation or the Ansible deployment gate.

# Employee Directory Deployment Runbook

## Purpose

This document describes the manual deployment process for the Employee Directory application on the production server (`web01`).

---

## Prerequisites

- SSH access to `web01`
- Git installed
- Virtual environment present
- `employee-directory` systemd service exists
- Nginx is running

---

## Deployment Steps

1. SSH into the server.
2. Navigate to the application directory
3. Pull the latest code.
4. Activate the virtual environment.
5. Install or update Python dependancies. 
6. Restart the application service.
7. Verify the service is running.
8. Test the application in a browser.
9. Review the logs.

---

## Validation Commands

```bash
sudo systemctl status employee-directory
sudo systemctl status nginx
sudo nginx -t
curl http://localhost
```

---

## Rollback

If deployment fails:

1. Stop the deployment.
2. Check the application logs.
3. Revert to the previous Git commit.
4. Restart the service.
5. Verify the application is operational.

---

## Post-Deployment Checks

- Home page loads.
- No errors in `/var/log/nginx/error.log`
- Gunicorn is active.
- Nginx is active.
- CSS loads correctly.
## Request Flow

```text
Browser

↓

Nginx

↓

Gunicorn

↓

Flask

↓

SQLite
```

## Configuration

Configuration file

```

/etc/nginx/sites-available/employee-directory

```

Enabled using a symbolic link

```

/etc/nginx/sites-enabled/

```

---

## Important Directives

### listen 80

Accept HTTP traffic.

---

### server_name _

Respond to requests regardless of hostname.

---

### proxy_pass

Forward traffic to Gunicorn.

```
proxy_pass http://127.0.0.1:8000;
```

---

### proxy_set_header

Preserves client information.

```
proxy_set_header Host $host;
proxy_set_header X-Real-IP $remote_addr;
proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
```

---

## Validation

Always validate configuration before reloading.

```
sudo nginx -t
```

Expected output

```
syntax is ok
test is successful
```

---

## Reload

Configuration changes should be applied using

```
sudo systemctl reload nginx
```

rather than restart.

Reload avoids dropping existing connections.

---

## Logs

Access Log

```
/var/log/nginx/access.log
```

Error Log

```
/var/log/nginx/error.log
```

---

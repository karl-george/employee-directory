# Nginx Configuration 

Prevent browsers from MIME sniffing by enforcing declared Content-Type headers.
```
add_header X-Content-Type-Options "nosniff" always;
```

Prevent clickjacking attacks by only allowing this site to be embedded within frames from the same origin.
```
add_header X-Frame-Options "SAMEORIGIN" always;
```

Limit the amount of referrer information sent to other websites, especially https to http.
```
add_header Referrer-Policy "strict-origin-when-cross-origin" always;
```


## Validation Checklist 
```
sudo systemctl status nginx
sudo systemctl status employee-directory
sudo nginx -t
ss -tulnp | grep :80
ss -tulnp | grep :8000
```

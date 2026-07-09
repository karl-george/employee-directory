# Application Architecture

```          
           Client
             │
             ▼
         Nginx :80
             │
             ▼
   Gunicorn 127.0.0.1:8000
             │
             ▼
          Flask
             │
             ▼
          SQLite
```
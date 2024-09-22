# Introduction

Put description here

# Set up

## Secrets
You need to create the file tg/secrets.py, with the lines
```python
SECRET_KEY = 'YOUR_SECRET_KEY'
API_KEY = 'YOUR_API_KEY'
```

You can generate keys from the python runtime with
```python
import secrets
print(secrets.token_urlsafe(50))
```
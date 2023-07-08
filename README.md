# Install

- Create Virtual env: `python -m venv flask`
- Active the Virtual env: `source flask/bin/activate`
- Install deps: `pip install -r requirements.txt`
- RUN: `flask --app server run --host 0.0.0.0 --port 2000`

# Test

```shell
curl localhost:2000/v1/admin
curl localhost:2000/v1/admin/18
curl localhost:2000/v1/config/18
curl localhost:2000/v1/config/18
```

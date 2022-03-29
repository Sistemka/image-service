# image-service
Serve to serve images. Resize them and saves on disk

## Run app
with docker 
```bash
docker-compose up
```

or without docker
```bash
poetry install
poetry run python run.py
```

## API
docs available on ```http://0.0.0.0:8080/docs```

* **POST /api/v1/images**
```curl
curl -X 'POST' \
  'http://0.0.0.0:8080/api/v1/images' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@file.png;type=image/png'
```

* **GET /api/v1/images/{size}/{image_id}**
```curl
curl -X 'GET' \
  'http://0.0.0.0:8080/api/v1/images/original/ff8afde3-53db-46fe-9961-7273c7e322b9' \
  -H 'accept: application/json'
```
Available sizes lists in **settings.py** you can configure them by yourself.
Now there are **original**, **small**, **medium**

## Linters And Tests

linters:
```bash
poetry run flake8 .
```

tests:
```bash
poetry run pytest -v tests
```

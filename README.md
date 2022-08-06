# wiremockのmappingsを見やすくしたい

## build

```
docker-compose build
```

## run

start wiremock

```
docker-compose up -d wiremock
```

start converter 

```
docker-compose run converter > output.html
```

python server 

```
python -m http.server 
```

access http://localhost:8000/output.html
# Natural Language Search App
### Partially-documented Django app for querying Participant database and associated study responses.
---

# Run the app ->

## Docker:
#### Use docker-compose to build the image and run the container:
```
docker-compose up -d --build
```

## Create schema migrations:
```
docker-compose exec server python manage.py makemigrations prospectdb
```

## Apply the changes to the database:
```
docker-compose exec server python manage.py migrate
```

## Create a superuser in order to access the Admin panel:
```
docker-compose exec server python manage.py createsuperuser
```

## Access the Admin panel:
```
http://localhost:8003/admin/
```

## Access the full list of Prospects / Participants:
```
http://localhost:8003/api/v1/prospectdb/prospects/
```



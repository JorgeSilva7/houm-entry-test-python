# Houm entry test

Houm entry test developed with python and django rest framework with MVC pattern

## Environment vars

CREATE ENVIRONMENT FILE IN: houm_test/secrets/.project_secrets OR set environments with other method

```plaintext
#EXAMPLE SECRETS
JWT_SECRET_KEY=aasdasdsadsad12q3123123asdasdsada
ENV=local
SECRET_KEY=django-insecure-rl&9abukg_b7eu_pv_r^2kgp5^awd)9$*i=0m+2nj564c55e1)
DB_ENGINE=django.db.backends.postgresql
DB_NAME=houm_test
DB_USER=user
DB_PASSWORD=password
DB_HOST=db
DB_PORT=5432
```

## Execution

```plaintext

- docker-compose -f docker-compose.dev.yml up
- docker exec -it CONTAINER_NAME python migrate.py migrate

or manually (without docker)

- create python env: venv name_environment
- pip install -r requirements.txt
- python manage.py migrate
- python manage.py makemigrations
- python manage.py runserver 0.0.0.0:8002

For production:
docker build .

docker run -p 8002:8002 <id_of_builded>
```

## Tests

Execute tests with this commands on docker with 'exec' command or without docker

```
- coverage run --source='.' manage.py test houmer
- coverage report
```

## informacion adicional

Este proyecto fue programado con python bajo MVC. Por cosa de tiempo se decidió no utilizar una clean architecture ya que es mas larga la salida a mercado o entrega
con estas metodologías de desarrollo versus una mejora sustancial en la mantención y cambios futuros.
También, el dockerfile de producción no contempla GUNICORN, que es recomendable para levantar projectos con python.

Se supuso que el tiempo de "traslado" de cada houmer es el tiempo entre que finaliza una visita y comienza otra,
esto para simplificar, ya que podría ser otra lógica mas compleja que la que se abordo en esta Prueba.

Tambien, se supuso que cada houmer tiene sus propiedades y puede estar visitando una sola, para visitar otra es
necesario finalizar la visita en curso antes de comenzar con otra.

Finalmente, para calcular la velocidad de traslado, se utiliza el metodo de 'haversine' para calcular la distancia lineal
entre 2 propiedades y luego eso se divide por el tiempo de traslado entre estas 2 para obtener la velocidad en kilometros
por hora.

Entonces, con esto es necesario estar logueado como houmer, crear dos propiedades y luego realizar una visita, finalizar
la visita y luego visitar la otra propiedad para que se hagan los calculos al utilizar los endpoints.
Estos endpoints estan disponible en formato postman en el archivo Houm-test python.postman_collection.json para ser importados

Trabajo futuro

- swagger (me falto tiempo para crear los yml o autodetectando en código)
- test unitarios por methodos (me falto tiempo para estudiar test unitarios con django)

Proyecto también disponible con typescript, swagger, test, arquitectura hexagonal (clean) en: https://github.com/JorgeSilva7/houm-entry-test

Jorge Silva - 2022

# Houm entry test

Houm entry test developed with python and django rest framework with MVC pattern

## Endpoints documentation

- /api-docs (swagger)

## Environment vars

```plaintext
SECRET_JWT=strong_jwt_secret
ENV=dev
```

## Execution

```plaintext

- docker-compose -f docker-compose.dev.yml up

or manually (without docker)

- create python env: venv name_environment
- pip install -r requirements.txt
-

For production:
docker build .

docker run -p 8002:8002 <id_of_builded>
```

## Tests

Execute tests with this commands

```
- TODO
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
Estos endpoints estan disponible en formato postman en el archivo postman.json para ser importados o viendolos en swagger

Jorge Silva - 2022

# todo-rest
TODO Application REST API

## Configuration

To run the project Docker Compose is used, and some stuff have to be configured.

Make a copy of the file `Docker/.env_template` in the same directory, named `.env` and customize the content.

## Production

In order to run the project in Production mode use the following command from the Docker folder:

```
docker compose --file docker-compose.yml up --build
```

## Test

In order to run the project in Test mode use the following command from the Docker folder:

```
docker compose --file docker-compose-test.yml up --build
```

## Future implementations

- Prepare enhanced documentation with Sphinx (comment already predisposed)
- Implement a custom Validator (at the moment a very light validation is present)
- Implement a custom Serializer (at the moment and manual serialization is present)

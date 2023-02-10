# FastApi + Posgress

Correr la aplicación

```sh
docker-compose up -d

# Para windowns
.\env\Scripts\activate
pip freeze > requirements.txt
python main.py
deactivate
```
Para ver la documentación ingresar a  [http://localhost:5000/docs](http://localhost:5000/docs)
Para ver la documentación alternativa ingresar a  [http://localhost:5000/redoc](http://localhost:5000/redoc)

- SQLAlchemy : ORM de Python (mapeador relacional de objetos)
- Psycopg : un controlador PostgreSQL

# Links de interes

- [Home page FastApi](https://fastapi.tiangolo.com/)
- [Handling Errors](https://fastapi.tiangolo.com/tutorial/handling-errors/)
- [JSON Schema](https://json-schema.org/)
- [Tipos](https://fastapi.tiangolo.com/python-types/)
- [SQLAlchemy Schema](https://overiq.com/sqlalchemy-101/defining-schema-in-sqlalchemy-core/)
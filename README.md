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
- Alembic : gestor de migación de base de datos

# Alembic

```ssh
pip install alembic
alembic init alembic
```

- Cambiar en alembic.ini la variable sqlalchemy.url

- Agregar la siguientes lineas en env.py de alembic
```python
from config.database import Base
target_metadata = Base.metadata
```

- Crear una revisión
```ssh
alembic revision --autogenerate -m "Algún útil mensaje"
```

- realizar la migración
```ssh
# Subir a la última migración
alembic upgrade head

alembic upgrade 4firstIdVersion

# Regresar n migraciones abajo
alembic downgrade -n
```

# Links de interes

- [Home page FastApi](https://fastapi.tiangolo.com/)
- [Handling Errors](https://fastapi.tiangolo.com/tutorial/handling-errors/)
- [JSON Schema](https://json-schema.org/)
- [Tipos](https://fastapi.tiangolo.com/python-types/)
- [SQLAlchemy Schema](https://overiq.com/sqlalchemy-101/defining-schema-in-sqlalchemy-core/)
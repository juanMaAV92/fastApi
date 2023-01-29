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

- SQLAlchemy : ORM de Python (mapeador relacional de objetos)
- Psycopg : un controlador PostgreSQL
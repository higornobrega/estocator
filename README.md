# Estocator

## Criando banco de dados

```shell
(venv) $ export FLASK_APP=app
(venv) $ export FLASK_DEBUG=1
(venv) $ flask shell
>>> from app import db, create_app
>>> db.create_all()
```

## Documentação

[Documento de Visão](https://github.com/Kmiokande/estocator/blob/main/docs/REQUISITOS.md)

[Lista de User Stories](https://github.com/Kmiokande/estocator/blob/main/docs/USER_STORIES.md)

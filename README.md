# Estocator

## O servidor de desenvolvimento

Vamos verificar se ele funciona. Execute o seguinte comando:

```shell
python manage.py runserver
```

### Alterando a porta

Por padrão, o comando runserver inicia o servidor de desenvolvimento no IP interno na porta 8000.

Se você quer mudar a porta do servidor, passe ela como um argumento na linha de comando. Por exemplo, este comando iniciará o servidor na porta 8080:

```shell
python manage.py runserver 8080
```

## Criando o banco de dados

Para criar nosso banco, execute o seguinte comando:

```shell
python manage.py migrate
```

## Criando um usuário administrador

Primeiro temos que criar um usuário que possa acessar o site de administração. Execute o seguinte comando:

```shell
python manage.py createsuperuser
```

## Documentação

[Documento de Visão](/docs/REQUISITOS.md)

[Lista de User Stories](/docs/USER_STORIES.md)

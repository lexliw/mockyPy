# mockyPy
Mockando serviço com python flask, simples e rápido


## Comandos para subir uma aplicação python Flask no Heroku:

Renomear o nome da aplicação principal para **app.py**

```
python3 -m venv venv/

source venv/bin/activate

pip3 install flask
pip3 install gunicorn

pip3 freeze > requirements.txt
```

Criar o arquivo **Procfile** com o conteudo:

```
web: gunicorn app:app
```

Comandos git:
```
git init .
git add .
git commit -m "first commit"

heroku login
git push heroku master
```
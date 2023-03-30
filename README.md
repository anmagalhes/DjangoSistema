## Este projeto foi feito com:

* [Python 3.10.6](https://www.python.org/)
* [Django 4.1.7](https://www.djangoproject.com/)
* [Bootstrap 4.0](https://getbootstrap.com/)

## Como rodar o projeto?

* Clone esse repositório.
* Crie um virtualenv com Python 3.
* Ative o virtualenv.
* Instale as dependências.
* Rode as migrações.

```
git clone https://github.com/anmagalhes/DjangoSistema.git
cd DjangoSistema

python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
python contrib/env_gen.py

python manage.py migrate
python manage.py createsuperuser --username="admin" --email=""
```
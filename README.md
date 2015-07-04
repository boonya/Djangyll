# Under construction.
[Issues board on Trello](https://trello.com/b/dCVPojTQ/djangyll)

###Clone project:
`git clone git@github.com:boonya/Djangyll.git`

###Install all requirements:
`pip install -r requirements.txt`

###Configure DB...
- `brew install postgres`
- `postgres -D /usr/local/var/postgres`
- `createuser djangyll`
- `createdb --owner=djangyll djangyll`
- `createdb --owner=djangyll test_djangyll`

###Create migrations:
`./manage.py makemigrations`

###Apply migrations:
`./manage.py migrate`

###Create superuser:
`./manage.py createsuperuser`

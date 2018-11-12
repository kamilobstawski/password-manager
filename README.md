# password-manager

heroku: https://manager-passwords.herokuapp.com/

To run this server locally run `python manage.py runserver --settings=password_manager.settings-debug`.

For testing run `pyton manage.py test --settings=password_manager.settings-debug`.

Login and password fields could be saved to db as ForeignKey(User), but there is no reason to populate db with another table.
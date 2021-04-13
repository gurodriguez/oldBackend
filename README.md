# The Shopping Catalog backend
## For Testing By Gabriel R.



## Features

- Developed with Django and Django Rest Framework
- Open API Ready using Swagger
- AWS SES Email at create, update or delete a product
- Is a shopping store backend ready using SQL Lite!
 



## Demo

You can see it at:

- [Open API](http://apiluuna.promos-dev.com/swagger/)
- [Admin Panel](http://apiluuna.promos-dev.com/admin/)
- [Frontend](http://shoptest.promos-dev.com/#/)
- [Frontend Repo](https://github.com/gurodriguez/frontendtest)



## Installation

Python 3 is requiried to be installed previously.

Install steps

```sh
git clone https://github.com/gurodriguez/backendtest.git
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

For using edit first settings.py

```sh
vim setting.py
```
The next VARS:
#Email Setings usig AWS SES
DEFAULT_FROM_EMAIL = 'noreply@yourDomain.mx'
#system admin accounts to send notifications
SYSADMIN = ['mailacc@mail.com']

#AWS Credentials
AWS_ACCESS_KEY_ID = '<Your KEY>'
AWS_SECRET_ACCESS_KEY = '< YOUR SECRET>'

Now in your terminal:
```sh
 python manage.py makemigrations
 python manage.py migrate
 python manage.py createsuperuser
```

Final checks
```sh
python manage.py runserver
```

Thats all...


## License

MIT

**Free Software, Hell Yeah!**

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

 

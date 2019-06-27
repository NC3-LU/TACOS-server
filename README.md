# {APP_NAME}-server

## Presentation


## Installation

```bash
$ git clone https://github.com/CASES-LU/{APP_NAME}-server.git
$ cd {APP_NAME}-server/
$ pipenv install
$ pipenv shell
$ python src/manager.py db_create
$ python src/manager.py db_init
$ python src/manager.py retrieve_spam_from_misp
$ python src/runserver.py
```

On Heroku:

```bash
$ heroku create --region eu tacos
$ heroku addons:add heroku-postgresql:hobby-dev
$ heroku config:set APPLICATION_SETTINGS='heroku.cfg'
$ git push heroku master
$ heroku run init
$ heroku ps:scale web=1
```

Retrieving data from MISP:

```bash
$ heroku config:set MISP_URL=<MISP-instance-URL>
$ heroku config:set MISP_KEY=<MISP-token>
$ heroku run python src/manager.py retrieve_spam_from_misp
```



## License

This software is licensed under
[GNU Affero General Public License version 3](https://www.gnu.org/licenses/agpl-3.0.html)


* Copyright (C) 2019 Cédric Bonhomme
* Copyright (C) 2019 SMILE gie securitymadein.lu

For more information, the [list of authors and contributors](AUTHORS.md) is
available.

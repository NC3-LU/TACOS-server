# tacos-server

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

### Deploy on Heroku

```bash
$ heroku create --region eu tacos-backend
$ heroku addons:add heroku-postgresql:hobby-dev
$ heroku config:set APPLICATION_SETTINGS='heroku.cfg'
$ git push heroku master
$ heroku run init
$ heroku ps:scale web=1
```

#### Retrieving data from MISP

```bash
$ heroku config:set MISP_URL=<MISP-instance-URL>
$ heroku config:set MISP_KEY=<MISP-token>
$ heroku run python src/manager.py retrieve_spam_from_misp
```

#### Adding some source of news

```bash
heroku run python src/manager.py add_feed_set 'Luxembourg Greater Region' 'Feeds proposed by CASES Luxembourg.'
heroku run python src/manager.py add_feed CIRCL 'CIRCL News feed' https://www.circl.lu/rss.xml en 1
heroku run python src/manager.py add_feed 'BEE Secure' 'Bee Secure feed' https://www.bee-secure.lu/de/rss/news de 1

heroku run python src/manager.py add_feed_set 'World feed' 'Feeds from all other the world proposed by CASES Luxembourg.'
heroku run python src/manager.py add_feed 'CSO online' 'CSO online' https://www.csoonline.com/index.rss en 2
heroku run python src/manager.py add_feed 'SANS Institute Security Awareness Tip of the Day' 'SANS Institute Security Awareness Tip of the Day' https://feeds2.feedburner.com/security-awareness-tip-of-the-day en 2
heroku run python src/manager.py add_feed 'Cybersecurity & Digital Privacy Policy (Unit H.2)' 'Cybersecurity & Digital Privacy Policy (Unit H.2)'  http://ec.europa.eu/information_society/newsroom/cf/generaterss.cfm?tpa_id=16548&sub=1&pr=all en 2


heroku run python src/manager.py add_feed_set 'CASES news' 'News about CASES'
heroku run python src/manager.py add_feed 'CASES tools' 'CASES tools' https://open-source-security-software.net/organization/CASES/releases.atom en 3
heroku run python src/manager.py add_feed 'MONARC news' 'News about MONARC' https://www.monarc.lu/feeds/all.atom.xml en 3
```


## License

This software is licensed under
[GNU Affero General Public License version 3](https://www.gnu.org/licenses/agpl-3.0.html)


* Copyright (C) 2019 Cédric Bonhomme
* Copyright (C) 2019 SMILE gie securitymadein.lu

For more information, the [list of authors and contributors](AUTHORS.md) is
available.

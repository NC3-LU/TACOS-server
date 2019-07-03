Installation
------------

.. code-block:: bash

    $ git clone https://github.com/CASES-LU/tacos-server.git
    $ cd tacos-server/
    $ pipenv install
    $ pipenv shell
    $ python src/manager.py db_create
    $ python src/manager.py db_init
    $ python src/runserver.py


On Heroku:

.. code-block:: bash

    $ heroku create --region eu tacos-backend
    $ heroku addons:add heroku-postgresql:hobby-dev
    $ heroku config:set APPLICATION_SETTINGS='heroku.cfg'
    $ git push heroku master
    $ heroku run init
    $ heroku ps:scale web=1


Deployment
----------

Configuration variables
~~~~~~~~~~~~~~~~~~~~~~~

Deployment with WSGI
~~~~~~~~~~~~~~~~~~~~


Populating the database
-----------------------

Configuring some source of news
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

    # Creation of a set of feeds
    python src/manager.py add_feed_set 'Luxembourg Greater Region' 'Feeds proposed by CASES Luxembourg.' 1
    # Adding some news to the newly created set
    python src/manager.py add_feed 'BEE Secure' 'Bee Secure feed' https://www.bee-secure.lu/de/rss/news de 1
    python src/manager.py add_feed 'Silicon Luxembourg' 'Silicon Luxembourg' https://www.siliconluxembourg.lu/tag/cybersecurity/feed/ en 1


Retrieving phone numbers from MISP
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   $ heroku config:set MISP_URL=<MISP-instance-URL>
   $ heroku config:set MISP_KEY=<MISP-token>
   $ heroku run python src/manager.py retrieve_spam_from_misp

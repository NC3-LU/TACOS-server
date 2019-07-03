This sections describes the services provided by the back-end.

Spam
----

SpamListAPI
~~~~~~~~~~~

.. code-block:: bash

    $ curl http://127.0.0.1:5000/api/vi/spams
    {"nb_results": 187, "objects": [{"number": "+xxxxxxxx", "category": "Financial fraud", "created": "Wed, 19 Jun 2019 09:15:55 -0000"}, ...]}



FeedSet
-------

FeedSetListAPI
~~~~~~~~~~~~~~

.. code-block:: bash

    $ curl http://127.0.0.1:5000/api/vi/feeds_sets

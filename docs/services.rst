This sections describes the services provided by the back-end.

Spam
----

SpamListAPI
~~~~~~~~~~~

Request to get the list of spam reports:

.. code-block:: bash

    $ curl http://127.0.0.1:5000/api/vi/spams
    {"nb_results": 187, "objects": [{"number": "+xxxxxxxx", "category": "Financial fraud", "created": "Wed, 19 Jun 2019 09:15:55 -0000"}, ...]}


Request to create a new spam report:

.. code-block:: bash

    $ curl -d '{"number_hash":"1cd2e705e2e4f7ff213e521260fb77f54c2b3e40c130e196817335c11101b0d9424e9ca3a7a0db702751b0754e304deb23df93cde1a6220a39e8940bfcde34eb", "category":"Financial fraud"}' -H "Content-Type: application/json" -X POST http://127.0.0.1:5000/api/v1/spams
    {
      "spam": {
        "category": "Financial fraud",
        "date": "Thu, 11 Jul 2019 07:23:34 -0000",
        "number": null,
        "number_hash": "1cd2e705e2e4f7ff213e521260fb77f54c2b3e40c130e196817335c11101b0d9424e9ca3a7a0db702751b0754e304deb23df93cde1a6220a39e8940bfcde34eb",
        "source": "TACOS",
        "uuid": "6a4ed983-73dd-43ca-8ad8-ae91c30787ff"
      }
    }




FeedSet
-------

FeedSetListAPI
~~~~~~~~~~~~~~

.. code-block:: bash

    $ curl http://127.0.0.1:5000/api/vi/feeds_sets

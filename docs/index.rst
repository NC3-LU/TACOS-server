.. Server documentation master file, created by
   sphinx-quickstart on Wed Jun 19 11:23:50 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Presentation
============

.. toctree::
   :maxdepth: 2
   :caption: Contents:

Services
========

This sections describes the services provided by the back-end.

Spam
----
SpamListAPI
~~~~~~~~~~~

.. code-block:: bash

    $ curl /api/vi/spams
    {"nb_results": 187, "objects": [{"number": "+xxxxxxxx", "category": "Financial fraud", "created": "Wed, 19 Jun 2019 09:15:55 -0000"}]}


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

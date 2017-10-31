******
Docker container for `repec_pubdb`_
******

This is an attempt to container-ize the app built for REPEC

Prerequisites
-------------

Make sure you have installed the last version of `Docker <https://www.docker.com/get-docker>`_
and you have read some `Docker documentation <https://docs.docker.com>`_ (you'll only need 
`docker-compose <https://docs.docker.com/compose/>`_ to work out of the box)

Build
-----

Edit the file `app/local_config <https://github.com/giupo/beccalossi/blob/master/app/local_config.py>`_ (please supply a valid `REPEC_API_CODE`), provide also a valid `DOMAIN`.

then:

.. code-block:: bash

    $ docker-compose up

.. _repec_pubdb: https://gitlab.com/MichelJuillard/repec_pubdb

Config Addendum
---------------

The app uses `Flask-Security <https://pythonhosted.org/Flask-Security/configuration.html>`_ for security configuration which
requires a MTA on the host running the app for user registration. Let's see if we can integrate other Auth providers (WIP)

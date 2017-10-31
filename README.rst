******
Docker container for `repec_pubdb`_
******

.. image:: https://travis-ci.org/giupo/blocky.svg?branch=master
    :target: https://travis-ci.org/giupo/blocky

This is an attempt to container-ize the app built for REPEC

Prerequisites
----

 Make sure you have installed the last version of Docker
 https://www.docker.com/get-docker

 and you have read some docker documentation (you'll only need
 `docker-compose` to work out of the box):
 https://docs.docker.com/

Build
----

 Edit the file `app/local_config.py` (please supply a valid `REPEC_API_CODE`),
 provide also a valid `DOMAIN`.

 then:

 .. code-block:: bash
     $ docker-compose up


.. _repec_pubdb: https://gitlab.com/MichelJuillard/repec_pubdb

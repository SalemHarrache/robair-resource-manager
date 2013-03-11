HTTP resource manager for 2013 Robair project.

Demo : http://robair.quicker.fr


Installation
============

::

    make setup


Activate your virtualenv before going to the next step


::

    source ./env/bin/activate

Now, create database using the script manager

::

    ./manager.py initdb

Let's start !

::

    ./manager.py runserver
     * Running on http://127.0.1.1:9090/
     * Restarting with reloader


Test
====

Resource reservation:
---------------------

::

    $ curl http://127.0.0.1:9090/api/new?jid=test@test.com
    {
      "jid": "test@test.com",
      "end": [
        "2013-03-23",
        "13:44:17"
      ],
      "started": false,
      "start": [
        "2013-03-11",
        "23:57:38"
      ],
      "key": "1bde8bac8-f654-42d5-aa6f-558b790d7cc3",
      "error": false,
      "expired": false,
      "id": 1
    }

Another reservation starts after the last one:

::

    $ curl http://127.0.0.1:9090/api/new?jid=test2@test.com
    {
      "jid": "test2@test.com",
      "end": [
        "2013-04-04",
        "03:31:56"
      ],
      "started": true,
      "start": [
        "2013-03-23",
        "13:45:17"
      ],
      "key": "2b86b2ebe-e7f0-4617-84de-7ef7ab79323a",
      "error": false,
      "expired": false,
      "id": 2
    }

You need a valid jabber id to make a reservation:

::

    $ curl http://127.0.0.1:9090/api/new?jid=bad_jid
    {
      "error_message": "invalid jid",
      "error": true
    }

You must always check the "error" field property


Check key:
----------

::

    $ curl http://127.0.0.1:9090/api/check?key=1bde8bac8-f654-42d5-aa6f-558b790d7cc3
    {
      "jid": "test@test.com",
      "end": [
        "2013-03-23",
        "13:44:17"
      ],
      "started": false,
      "start": [
        "2013-03-11",
        "23:57:38"
      ],
      "valid": true,
      "key": "1bde8bac8-f654-42d5-aa6f-558b790d7cc3",
      "expired": false,
      "id": 1
    }

::

    $ curl http://127.0.0.1:9090/api/check?key=bad_key
    {
      "valid": false
    }

You must always check the "valid" field property

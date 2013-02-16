Portail de réservation HTTP pour le projet Robair 2013.

Demo : http://robair.quicker.fr


Installation
============

::

    make setup


Activer le virtualenv avant de continuer:


::

    source ./env/bin/activate


::

    ./manager.py initdb


::

    ./manager.py runserver
     * Running on http://127.0.1.1:9090/
     * Restarting with reloader


Test
====

New reservation:

::

    $ curl http://127.0.0.1:9090/api/new
    {
      "start": [
        "2013-02-14",
        "20:57:58"
      ],
      "end": [
        "2013-02-26",
        "10:44:37"
      ],
      "id": 2,
      "key": "215a3bf96-f937-4c55-a2e1-5fa00e996a3e",
      "error": false
    }

Check your key:

::

    $ curl http://127.0.0.1:9090/api/check?key=215a3bf96-f937-4c55-a2e1-5fa00e996a3e
    {
      "valid": true
    }

::

    $ curl http://127.0.0.1:9090/api/check?key=bad_key
    {
      "valid": false
    }

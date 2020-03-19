Ut Anagramma
============

Internet-facing web service accepting a single word and deriving all possible anagrams. (not permutations)

The application can be deployed into Google Cloud App Engine Standard.


Preparing for Development
-------------------------

1. Ensure ``pip`` and ``pipenv`` are installed
2. Clone repository
3. ``cd`` into repository
4. Fetch development dependencies ``make install``
5. Activate virtualenv: ``pipenv shell``

Usage
-----

There is a "cli.py" script as a Proof Of Concept of "main.py": python3 cli.py

::

The real script running with Flask is main.py


Running Tests
-------------

Run tests locally using ``make`` if virtualenv is active:

::

    $ make

If virtualenv isn’t active then use:

::

    $ pipenv run make

Deploying the application in GCP App Engine Standard
----------------------------------------------------

1. Enable Google App Engine Admin API
2. From src/ut_anagramma/ where the app's app.yaml: dev_appserver.py app.yaml
3. The development server is now running and listening for requests on port 8080.
4. From src/ut_anagramma/ where the app's app.yaml: gcloud app deploy
5. To launch your browser: gcloud app browse

Ut Anagramma
============

Internet-facing web service accepting a single word and deriving all possible anagrams. (not permutations)

The application can be deployed into Google Cloud App Engine Standard.


Usage
-----

There is a "cli.py" script as a Proof Of Concept of "main.py": python3 cli.py

::

The real script running with Flask is main.py


Deploying the application in GCP App Engine Standard
----------------------------------------------------

1. Enable Google App Engine Admin API
2. From src/ut_anagramma/ where the app's app.yaml: dev_appserver.py app.yaml
3. The development server is now running and listening for requests on port 8082.
4. From src/ut_anagramma/ where the app's app.yaml: gcloud app deploy
5. To launch your browser: gcloud app browse

Docker support
--------------

https://hub.docker.com/repository/docker/maolopez/ut_anagramma
docker pull maolopez/ut_anagramma:latest
docker run -it --name anagrama -p 8082:8082 Image_ID

Ut Anagramma
============

Internet-facing web service accepting a single word and deriving all possible anagrams. (not permutations). The application can be deployed into Google Cloud App Engine Standard.
 
https://ut-anagramma.uk.r.appspot.com/

Usage
-----

There is a "cli.py" script as a Proof Of Concept of "main.py": python3 cli.py

::

The real script running with Flask is main.py


Deploying the application in GCP App Engine Standard
----------------------------------------------------

1. Enable Google App Engine Admin API.
2. From src/ut_anagramma/ where the app's app.yaml: dev_appserver.py app.yaml
3. The development server is now running and listening for requests on port 8082.
4. From src/ut_anagramma/ where the app's app.yaml: gcloud app deploy.
5. To launch your browser: gcloud app browse.

Docker support
--------------

https://hub.docker.com/repository/docker/maolopez/ut_anagramma

docker pull maolopez/ut_anagramma:latest

docker run --restart always --name ut_anagramma -p 8082:8082 -d maolopez/ut_anagramma:latest

Deploying the application in AWS with Jenkins
---------------------------------------------

1. There is a manual option deployment in the pipeline.
2. Get some CloudFormation stack from https://github.com/maolopez/PipelineOnTheFly.
3. Get Docker plugins for Jenkins and Docker installed in your destination server.

Deploying the application in AWS and EKS
---------------------------------------------

1. https://github.com/maolopez/aws-capstone 
2. https://github.com/maolopez/aws-capstone-kubernetes

Deploying the application in GCP/GKE with GitLab
---------------------------------------------

1. There is a .gitlab-ci.yml file to support GitLab CI.
2. More details in https://gitlab.com/maolopez1/ut_anagramma .
3. More support in https://gitlab.com/maolopez1/ci_cd_terraform_and_gcp .
4. KUBERNETES DEPLOYMENTS: First create your GCK Kubernetes cluster
https://gitlab.com/maolopez1/kubernetes-for-gcp-with-terraform
Note: If you know what are you doing, check the manifests files inside
the kubernetes/ folder before running the manual pipeline stages.


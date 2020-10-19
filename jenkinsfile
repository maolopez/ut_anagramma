pipeline {
    agent any
    stages {
        stage('checkout') {
          deleteDir()
          checkout scm
        }
        stage('Build Docker Image') {
            when {
                branch 'develop'
            }
            steps {
                script {
                    app = docker.build("maolopez/ut_anagramma")
                    app.inside {
                        sh 'echo $(curl localhost:8080)'
                    }
                }
            }
        }
        stage('Push Docker Image') {
            when {
                branch 'develop'
            }
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', 'docker_hub') {
                        app.push("${env.BUILD_NUMBER}")
                        app.push("latest")
                    }
                }
            }
        }

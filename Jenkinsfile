pipeline {
    agent any
    stages {
        stage('Build Docker Image') {
            when {
                branch 'develop'
            }
            steps {
                script {
                    app = docker.build("maolopez/ut_anagramma")
                    app.inside {
                        sh 'echo $(curl localhost:8082)'
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
                        app.push("latest")
                    }
        stage('DeployToProduction') {
            when {
                branch 'develop'
            }
            steps {
                input 'Deploy to Production'
                milestone(1)
                withCredentials ([usernamePassword(credentialsId: 'webserver_login', usernameVariable: 'USERNAME', passwordVariable: 'USERPASS')]) {
                   script {
                       sh "sshpass -p '$USERPASS' -v ssh -o StrictHostKeyChecking=no $USERNAME@$prod_ip \"docker pull maolopez/ut_anagramma:latest\""
                       try {
                          sh "sshpass -p '$USERPASS' -v ssh -o StrictHostKeyChecking=no $USERNAME@prod_ip \"docker stop ut_anagramma\""
                          sh "sshpass -p '$USERPASS' -v ssh -o StrictHostKeyChecking=no $USERNAME@prod_ip \"docker rm ut_anagramma\""
                        } catch (err) {
                            echo: 'caught error: $err'
                        }
                        sh "sshpass -p '$USERPASS' -v ssh -o StrictHostKeyChecking=no $USERNAME@prod_ip \"docker run --restart always --name ut_anagramma -p 8082:8082 -d maolopez/ut_anagramma:latest\""
                        }
                      }
                    }
                  }
                }
            }
        }
    }
}

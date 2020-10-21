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
                }
            }
        }
        stage('DeployToProduction') {
        	when {
                 branch 'develop'
            }
            steps {
                input 'Deploy to Production'
                milestone(1)
                withCredentials(bindings: [sshUserPrivateKey(credentialsId: 'ec2sshkey', \
                                             keyFileVariable: 'Key')]) {
                   script {
                       sh "ssh -i $Key -o StrictHostKeyChecking=no ec2-user@${prod_ip} \"sudo docker pull maolopez/ut_anagramma:latest\""
                       try {
                          sh "ssh -i $Key -o StrictHostKeyChecking=no ec2-user@${prod_ip} \"sudo docker stop ut_anagramma\""
                          sh "ssh -i $Key -o StrictHostKeyChecking=no ec2-user@${prod_ip} \"sudo docker rm ut_anagramma\""
                        } catch (err) {
                            echo: 'caught error: $err'
                        }
                        sh "ssh -i $Key -o StrictHostKeyChecking=no ec2-user@${prod_ip} \"sudo docker run --restart always --name ut_anagramma -p 8082:8082 -d maolopez/ut_anagramma:latest\""
                    }
                }
            }
        }
    }
}

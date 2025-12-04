pipeline {
    agent any

    environment {
        IMAGE_NAME = "flask-message-app"
        DOCKERHUB_USER = "vamshiintech"   // your dockerhub username
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main', credentialsId: 'github-ssh', url: 'git@github.com:VamshiInTech/flask-message-app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t $DOCKERHUB_USER/$IMAGE_NAME:latest .'
                }
            }
        }

        stage('Login to Docker Hub') {
            steps {
                script {
                    sh 'echo "$DOCKER_PASSWORD" | docker login -u "$DOCKERHUB_USER" --password-stdin'
                }
            }
        }

        stage('Push Image') {
            steps {
                sh 'docker push $DOCKERHUB_USER/$IMAGE_NAME:latest'
            }
        }

        stage('Deploy Container') {
            steps {
                script {
                    sh '''
                    docker rm -f flask-app || true
                    docker run -d --name flask-app -p 5000:5000 $DOCKERHUB_USER/$IMAGE_NAME:latest
                    '''
                }
            }
        }
    }
}


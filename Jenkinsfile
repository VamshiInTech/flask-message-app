pipeline {
    agent any

    environment {
        DOCKER = credentials('dockerhub')
    }

    stages {
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t vamshi/flask-message-app:latest .'
            }
        }

        stage('Login to Docker Hub') {
            steps {
                sh '''
                    echo "$DOCKER_PSW" | docker login -u "$DOCKER_USR" --password-stdin
                '''
            }
        }

        stage('Push Image') {
            steps {
                sh 'docker push vamshi/flask-message-app:latest'
            }
        }
    }
}


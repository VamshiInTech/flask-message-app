pipeline {
    agent any

    environment {
        DOCKER_CREDS = credentials('dockerhub-creds')
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    credentialsId: 'github-ssh',
                    url: 'git@github.com:VamshiInTech/flask-message-app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t vamshi/flask-message-app:latest .'
            }
        }

        stage('Login to Docker Hub') {
            steps {
                sh '''
                    echo "$DOCKER_CREDS_PSW" | docker login -u "$DOCKER_CREDS_USR" --password-stdin
                '''
            }
        }

        stage('Push Image') {
            steps {
                sh 'docker push vamshi/flask-message-app:latest'
            }
        }

        stage('Deploy Container') {
            steps {
                sh '''
                    docker rm -f flask-app || true
                    docker run -d --name flask-app -p 5000:5000 vamshi/flask-message-app:latest
                '''
            }
        }
    }
}


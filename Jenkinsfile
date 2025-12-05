pipeline {
    agent any

    environment {
        IMAGE_NAME = "vamshiintech/flask-message-app"
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'git@github.com:VamshiInTech/flask-message-app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                    echo "Building Docker Image..."
                    docker build -t ${IMAGE_NAME}:latest .
                '''
            }
        }

        stage('Login to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds',
                                                 usernameVariable: 'DOCKER_USER',
                                                 passwordVariable: 'DOCKER_PASS')]) {
                    sh '''
                        echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                    '''
                }
            }
        }

        stage('Push Image') {
            steps {
                sh '''
                    echo "Pushing Docker Image to Docker Hub..."
                    docker push ${IMAGE_NAME}:latest
                '''
            }
        }

        stage('Deploy Container') {
            steps {
                sh '''
                    echo "Stopping old container (if exists)..."
                    docker stop flask-message-app || true
                    docker rm flask-message-app || true

                    echo "Running new container..."
                    docker run -d --name flask-message-app -p 5000:5000 ${IMAGE_NAME}:latest
                '''
            }
        }
    }

    post {
        success {
            echo "Pipeline executed successfully!"
        }
        failure {
            echo "Pipeline failed!"
        }
    }
}


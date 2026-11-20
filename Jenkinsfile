pipeline {
    agent {node{ label 'docker-node' }} // Runs this pipeline on any agent tagged with 'docker-node'
    
    environment {
        IMAGE_NAME = "docker.io/venkat4222/my-python-project"
    }

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        

        stage('Run Tests in Container') {
            steps {
            sh '''
                # Build your test container image
                docker build -t test-runner .
                # Run the test suite with pytest inside the container
                docker run --rm test-runner pytest
            '''
            }
        }

        stage('Build & Push Production Image') {
            steps {
                sh '''
                    docker build -t $IMAGE_NAME:latest .
                '''
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-credentials',
                    usernameVariable: 'DOCKERHUB_USERNAME',
                    passwordVariable: 'DOCKERHUB_TOKEN'
                )]) {
                    sh '''
                        set +x
                        trap 'docker logout docker.io >/dev/null 2>&1 || true' EXIT
                        printf '%s' "$DOCKERHUB_TOKEN" | docker login --username "$DOCKERHUB_USERNAME" --password-stdin docker.io
                        docker push "$IMAGE_NAME:latest"
                    '''
                }
            }
        }

        stage('Deploy to Production') {
            steps {
                sh '''
                    # Stop and remove any old running container
                    docker stop my-running-app || true
                    docker rm my-running-app || true

                    # Run the fresh container
                    docker run -d --name my-running-app -p 8000:8000 $IMAGE_NAME:latest
                '''
            }
        }
    }
}
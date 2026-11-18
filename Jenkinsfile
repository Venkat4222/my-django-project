pipeline {
    agent {node{ label 'docker-node' }} // Runs this pipeline on any agent tagged with 'docker-node'
    
    environment {
        IMAGE_NAME = "your-dockerhub-username/my-python-project"
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
            docker build -t test-runner .
            docker run --rm -e DJANGO_SETTINGS_MODULE=mysite.settings test-runner pytest
        '''
    }
}

        stage('Build & Push Production Image') {
            steps {
                sh '''
                    docker build -t $IMAGE_NAME:latest .
                    # If pushing to a registry, ensure docker login is configured on the agent
                    docker push $IMAGE_NAME:latest
                '''
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
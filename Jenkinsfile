pipeline {
    agent {node{ label 'docker-node' }} // Runs this pipeline on any agent tagged with 'docker-node'
    
    environment {
        IMAGE_NAME = "Admin/my-python-project"
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
                # Run Django's native test runner inside the container
                docker run --rm test-runner python manage.py test
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
pipeline {
    agent {node{ label 'docker-node' }} // Runs this pipeline on any agent tagged with 'docker-node'
    
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
    }
}
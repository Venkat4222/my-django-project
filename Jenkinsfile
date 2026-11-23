pipeline {
    agent none

    stages {
        stage('Test on AWS Agent') {
            agent { label 'aws-ec2-docker' }
            steps {
                checkout scm
                sh 'hostname && id && docker --version'
                sh 'if command -v pytest >/dev/null 2>&1; then pytest; else echo "pytest not installed on agent; skipping or run inside Docker"; fi'
            }
        }

        stage('Build & Push to Docker Hub') {
            agent { label 'aws-ec2-docker' }
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DH_USER', passwordVariable: 'DH_PASS')]) {
                    sh '''
                        echo "$DH_PASS" | docker login -u "$DH_USER" --password-stdin
                        docker build -t venkat4222/my-python-project:${BUILD_NUMBER} -t venkat4222/my-python-project:latest .
                        docker push venkat4222/my-python-project:${BUILD_NUMBER}
                        docker push venkat4222/my-python-project:latest
                    '''
                }
            }
        }
    }
}
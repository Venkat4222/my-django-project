pipeline {
    agent none

    stages {
        stage('Test on AWS Agent') {
            agent { label 'docker-node' }
            steps {
                checkout scm
                sh 'hostname && docker --version'
                sh 'pytest'
            }
        }

        stage('Build & Push to Docker Hub') {
            agent { label 'docker-node' }
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
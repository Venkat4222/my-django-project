def setGithubStatus(String state, String description) {
    withCredentials([string(credentialsId: 'github-status-token', variable: 'GH_TOKEN')]) {
        sh """
            curl -sS -X POST \\
              -H "Authorization: Bearer \$GH_TOKEN" \\
              -H "Accept: application/vnd.github+json" \\
              "https://api.github.com/repos/Venkat4222/my-django-project/statuses/${env.GIT_COMMIT}" \\
              -d '{\"state\": \"${state}\", \"target_url\": \"${env.BUILD_URL}\", \"description\": \"${description}\", \"context\": \"ci/jenkins-aws-docker\"}'
        """
    }
}



pipeline {
    agent none

    stages {
        stage('Notify Pending') {
            agent { label 'aws-ec2-docker' }
            steps {
                script {
                    setGithubStatus('pending', 'Jenkins build running on AWS agent')
                }
            }
        }

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
                withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials', usernameVariable: 'DH_USER', passwordVariable: 'DH_PASS')]) {
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

    post {
        success {
            script {
                setGithubStatus('success', "Build #${env.BUILD_NUMBER} succeeded")
            }
        }
        failure {
            script {
                setGithubStatus('failure', "Build #${env.BUILD_NUMBER} failed")
            }
        }
    }
}
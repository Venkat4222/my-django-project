pipeline {
    agent {
        label 'kubuntu-agent' // Tells Jenkins to run this on a specific agent
    }
    stages {
        stage('Check Environment') {
            steps {
                sh 'python3 --version'
                sh 'echo "Running build on agent machine!"'
            }
        }
    }
}
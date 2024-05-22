pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                echo 'Hello from Jenkins'
            }
        } 
        stage('Python Test') {
            steps {
                script {
                    sh 'python3 --version'
                    sh 'ls -lt $WORKSPACE'
                    sh 'python3 jenkins-docker/src/main.py'
                }
            }
        }    
    }
}
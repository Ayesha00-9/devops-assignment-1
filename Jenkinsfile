pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'feature/devops',
                    url: 'https://github.com/Ayesha00-9/devops-assignment-1.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t weather-advice-app .'
            }
        }
    }
}
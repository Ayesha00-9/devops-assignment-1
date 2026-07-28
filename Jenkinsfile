pipeline {
    agent any

    tools {
        sonarQube 'SonarQube'
    }

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'feature/devops',
                    url: 'https://github.com/Ayesha00-9/devops-assignment-1.git'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('SonarQube') {
                    sh '''
                    sonar-scanner \
                      -Dsonar.projectKey=weather-advice-app \
                      -Dsonar.projectName=weather-advice-app \
                      -Dsonar.sources=. \
                      -Dsonar.host.url=http://sonarqube:9000
                    '''
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t weather-advice-app .'
            }
        }
    }
}
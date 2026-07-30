pipeline {
    agent any

    tools {
        sonarRunner 'SonarScanner'
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
                          -Dsonar.host.url=$SONAR_HOST_URL \
                          -Dsonar.token=$SONAR_AUTH_TOKEN
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
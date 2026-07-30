pipeline {
    agent any

    environment {
        IMAGE_NAME = "weather-advice-app"
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
                        -Dsonar.sources=.
                    '''
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${IMAGE_NAME}:latest ."
            }
        }
    }

    post {
        success {
            echo "Pipeline completed successfully."
        }
        failure {
            echo "Pipeline failed."
        }
    }
}
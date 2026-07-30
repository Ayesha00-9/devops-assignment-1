pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Python Check') {
            steps {
                sh 'python3 --version'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip3 install --break-system-packages -r requirements.txt || echo "No requirements.txt"'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('sonarqube') {
                    sh 'sonar-scanner -Dsonar.projectKey=${JOB_NAME} -Dsonar.projectName=${JOB_NAME} -Dsonar.sources=. -Dsonar.host.url=http://sonarqube:9000'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t ${JOB_NAME} .'
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
